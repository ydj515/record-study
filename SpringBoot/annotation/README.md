# SpringBoot - annotation

## DI-Related Annotations
#### @Autowired
생성자 주입
#### @Bean
bean 등록
#### @Qualifier
bean 등록 시 특정 이름 등록

#### @Required
xml 등록으로 bean 주입
```java
@Required
void setColor(String color) {
    this.color = color;
}

```
```xml
<bean class="com.baeldung.annotations.Bike">
    <property name="color" value="green" />
</bean>
```
#### @Value
Spring 관리 Bean의 필드에 값을 할당하는 데 사용

- constructor injection
```java
Engine(@Value("8") int cylinderCount) {
    this.cylinderCount = cylinderCount;
}
```
- Setter injection
```java
@Autowired
void setCylinderCount(@Value("8") int cylinderCount) {
    this.cylinderCount = cylinderCount;
}
```
- Alternatively
```java
@Value("8")
void setCylinderCount(int cylinderCount) {
    this.cylinderCount = cylinderCount;
}
```
- Field injection
```java
@Value("8")
int cylinderCount;
```

####  @DependsOn
의존관계 순서 지정(a, b -> c 등록)
```java
@Component("A")
public class ComponentA {
	 // ...
}

@Component("B")
public class ComponentB {
	 // ...
}

@Component("C")
@DependsOn(value={"A", "B"})
public class ComponentC {
	 // ...
}
```
```java
@Component
public class TestComponent {
	@Bean("A")
	public void beanA() {
		// ...
	}
	
	@Bean("B")
	public void beanB() {
		// ...
	}
	
	@Bean("C")
	@DependsOn(value={"A", "B"})
	public void beanC() {
		// ...
	}
}
```

#### @Lazy
기본적으로 eager로 bean 주입이 되지만, lazy를 사용할 경우 해당 Component 객체를 호출해줘야 그 때 초기화되고 호출된다.

```java
@Configuration
@Lazy
class VehicleFactoryConfig {

    @Bean
    @Lazy(false)
    Engine engine() {
        return new Engine();
    }
}
```

#### @Lookup
singleton bean에게 prototype scope인 bean을 주입할 때 사용
https://www.baeldung.com/spring-lookup

```java
@Component
@Scope("prototype")
public class SchoolNotification {
    // ... prototype-scoped state
}
```

```java
@Component
public class StudentServices {

    // ... member variables, etc.

    @Lookup
    public SchoolNotification getNotification() {
        return null;
    }

    // ... getters and setters
}
```

```java
@Test
public void whenLookupMethodCalled_thenNewInstanceReturned() {
    // ... initialize context
    StudentServices first = this.context.getBean(StudentServices.class);
    StudentServices second = this.context.getBean(StudentServices.class);
       
    assertEquals(first, second); // singleton 이기에 동일
    assertNotEquals(first.getNotification(), second.getNotification()); // StudentServices.getNotification()은 proto이기 때문에 매번 달라짐
}
```
만약 위의 테스트 에서 `@Scope("prototype")`를 제거. 즉 singleton으로 놓고 테스트하면 에러가 발생한다.<br/>
StudentServices에서 onstructor 나 setter 방식으로 Notification이라는 bean을 주입받으면 주입은 잘 받아지나 고정이된다.<br/>
즉. prototype scope는 매번 필요할 때마다 application context가 새로 생성되야하는데 생성된걸 받질 못하는거다.<br/>
StudentServices 가 singleton으로 생성 되기 때문.



#### @Primary
동일 타입의 빈이 다수 존재할 때, 특정 빈에 우선순위를 높게 준다.

#### @Scope
@Component / @Bean의 scope(singleton, prototype, request, session, globalSession, custom scope) 정의<br/>
default는 singleton, prototype는 매번 객체 생성
<br/>

## Context Configuration Annotations
#### @Profile
런타임 환경설정 <br/>
환경에 따라서 쿼리가 다르다거나 할 경우에 쓰기 좋을 것 같다.(암호화 등)<br/>
혹은 운영환경에서만 사용하고 싶은 config 도 컨트롤 할 수 있다.<br/>
각 환경에 맞는 bean 설정<br/>
class level 에다가도 `profile` 지정 가능하다.<br/>

- repo를 다르게 bean 등록하는 예시
```java
@Configuration
public class Config {

    @Bean
    @Profile("prod")
    public ProdRepository prodRepository() {
        return new ProdRepository();
    }

    @Bean
    @Profile({"test", "dev"})
    public LocalRepository localRepository() {
        return new LocalRepository();
    }

    @Bean
    @Profile("!prod & !dev & !test")
    public OtherRepository otherRepository() {
        return new OtherRepository();
    }
}
```

- redis 설정이 prod, dev 다른 예시
```java
@Configuration
public class RedisConfig {

    @Value("${spring.data.redis.host}")
    private String host;
    @Value("${spring.data.redis.port}")
    private int port;

    @Bean
    @Profile("dev")
    public RedisConnectionFactory redisConnectionFactory() {
        return new LettuceConnectionFactory(host, port);
    }

    @Bean
    @Profile("prod")
    public RedisConnectionFactory redisConnectionFactoryProd() {
        LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory(host, port);
        connectionFactory.setPassword(String.valueOf(RedisPassword.of("암호")));
        return connectionFactory;
    }

}
```

- 환경설정
`application.yml`에 active profile 지정 혹은 jvm 옵션으로 추가
```yml
spring:
    profiles:
        active: dev
```
```
-Dspring.profiles.active="dev"
```

- 확인
AppRuner를 통해 확인
```java
@Component
public class AppRunner implements ApplicationRunner {

    @Autowired
    ApplicationContext ctx;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        Environment environment = ctx.getEnvironment();
        System.out.println("=================================================");
        System.out.println(Arrays.toString(environment.getActiveProfiles()));
        System.out.println(Arrays.toString(environment.getDefaultProfiles()));
    }
}
```
#### @Import
config의 그루핑

- AS-IS
appconf1, appconf2를 모두 사용하기 위해서는 `ctx = new AnnotationConfigApplicationContext(AppConf1.class, AppConf2.class);` 이렇게 가져와야한다.
```java
@Configuration
public class AppConf1 {

	@Bean
	public MemberDao memberDao() {
		return new MemberDao();
	}
	
	@Bean
	public MemberPrinter memberPrinter() {
		return new MemberPrinter();
	}
}
@Configuration
public class AppConf2 {

	@Bean
	public MemberInfoPrinter memberInfoPrinter() {
		return new MemberInfoPrinter();
	}
}
```

- TO-BE
import 사용시에 `ctx = new AnnotationConfigApplicationContext(AppConf1.class);` 이런식으로 가져오는것이 가능

```java
@Configuration
@Import(AppConf2.class)
public class AppConf1 {

	@Bean
	public MemberDao memberDao() {
		return new MemberDao();
	}
	
	@Bean
	public MemberPrinter memberPrinter() {
		return new MemberPrinter();
	}
}
```

annotation에도 설정이 가능하다.
```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Documented
@Import({AppConf1.class, AppConf2.class})
public @interface EnableConfig {
    boolean show() default true;
}

public class AppConf1 {
  @Bean
  public String hello1() {
    return "enable import Hello";
  }
}

public class AppConf2 {
  @Bean
  public String world1() {
    return "enable import World";
  }
}
```
또한 아래와 같이 ImportAware 구현하기 위해서 @configuration도 달아줘야함.
```java
@Configuration
public class AppConf2 implements ImportAware {

  boolean show;

  @Bean
  public String world1() {
    if(show) {
      return "show";
    }
    return "hide";
  }

  @Override
  public void setImportMetadata(AnnotationMetadata annotationMetadata) {
    Map<String, Object> metaData = annotationMetadata.getAnnotationAttributes(EnableConfig.class.getName());
    this.show = (boolean)metaData.get("show");
  }
}
```

#### @ImportResource
xml파일들을 @Configuration에 의해 component scan 시점에 파일들이 import 되어 configuration으로 설정
```java
@Configuration
@ImportResource(value = {
		"classpath*:appConfig.xml",
		"classpath*:appLogger.xml"
})
public class ExternalConfig {
}
```

#### @PropertySource
property 설정 파일 적용
```java
@Configuration
@PropertySource("classpath:/annotations.properties")
@PropertySource("classpath:/vehicle-factory.properties")
class VehicleFactoryConfig {}
```

#### @PropertySources
property 설정 파일 multiple 적용
```java
@Configuration
@PropertySources({ 
    @PropertySource("classpath:/annotations.properties"),
    @PropertySource("classpath:/vehicle-factory.properties")
})
class VehicleFactoryConfig {}
```

## Spring Web Annotations
#### @RequestMapping
@controller 에 작성하며 class level, method leve로 작성 가능
```java
@Controller
@RequestMapping(value = "/vehicles", method = RequestMethod.GET)
class VehicleController {

    @RequestMapping("/home")
    String home() {
        return "home";
    }
}
```
#### @RequestBody
http request body's object를 매핑
```java
@PostMapping("/save")
void saveVehicle(@RequestBody Vehicle vehicle) {
    // ...
}
```

#### @PathVariable
http 경로에 있는 것을 매핑, required 옵션 가능
```java
@RequestMapping("/{id}")
Vehicle getVehicle(@PathVariable(required = false) long id) {
    // ...
}
```

#### @RequestParam
Http 요청 파라미터의 이름으로 바인딩하여 그 값을 변수에 저장
```java
@RequestMapping("/buy")
Car buyCar(@RequestParam(defaultValue = "5") int seatCount) {
    // ...
}
```

#### @ResponseBody
http body에 매핑하여 return
```java
@ResponseBody
@RequestMapping("/hello")
String hello() {
    return "Hello World!";
}
```
#### @ExceptionHandler
custom error handler method를 선언 가능
```java
@ExceptionHandler(IllegalArgumentException.class)
void onIllegalArgumentException(IllegalArgumentException exception) {
    // ...
}
```

#### @ResponseStatus
http response를 특정해서 return해줄 수 있음
```java
@ExceptionHandler(IllegalArgumentException.class)
@ResponseStatus(HttpStatus.BAD_REQUEST)
void onIllegalArgumentException(IllegalArgumentException exception) {
    // ...
}
```

#### @Controller
spring controller
```java
@Controller
class VehicleRestController {
    // ...
}
```

#### @RestController
`@Controller` + `@ResponseBody`
```java
@Controller
@ResponseBody
class VehicleRestController {
    // ...
}
```
위를 아래와 같이 사용 가능하다.
```java
@RestController
class VehicleRestController {
    // ...
}
```


#### @ModelAttribute
method leve, method parameter level에 적용 가능</br>
`vehicle`라는 이름을 지정해서 매핑 가능
```java
@PostMapping("/assemble")
void assembleVehicle(@ModelAttribute("vehicle") Vehicle vehicleInModel) {
    // ...
}
```
defualt로도 사용 가능
```java
@PostMapping("/assemble")
void assembleVehicle(@ModelAttribute Vehicle vehicle) {
    // ...
}
```
아래와 같이 method level에 적용한다면 return할때 model.addAttribute와 같은 효과를 준다.
```java
@ModelAttribute("vehicle")
public void case1(Model model) {
    model.addAttribue("value1", "hi");
}

@ModelAttribute("value2")
public String case2() {
    return "hello";
}

@RequestMapping(value="/", method = RequestMethod.GET)
public String test(Model model) {
    return "test";
}
```
아래의 view에서 사용 가능
```html
<p th:text="${value1}">
<p th:text="${value2}">
```


#### @CrossOrigin
webmvc config로 할수도 있지만 cors 설정을 할 수 있다.<br/>
origins, originPatterns, allowedHeaders, methods, allowCredentials, maxAge등 설정 가능
- annotation config
```java
@CrossOrigin(maxAge = 3600)
@RestController
@RequestMapping("/account")
public class AccountController {

    @CrossOrigin("http://example.com")
    @RequestMapping(method = RequestMethod.GET, "/{id}")
    public Account retrieve(@PathVariable Long id) {
        // ...
    }

    @RequestMapping(method = RequestMethod.DELETE, path = "/{id}")
    public void remove(@PathVariable Long id) {
        // ...
    }
}
```

```java
@EnableWebSecurity
public class WebSecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.cors().and()...
    }
}
```

- java config
```java
@Configuration
@EnableWebMvc
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**");
    }
}
```

## Spring Boot Annotations

#### @SpringBootApplication
spring boot main class marks<br/>
@Configuration, @EnableAutoConfiguration, @ComponentScan을 포함<br/>
스프링 부트는 bean을 2번 등록한다. `ComponentScan`(@Configuration, @Repository, @Service, @Controller, @RestController ...)으로 한번, 그 다음 `EnableAutoConfiguration`을 통해 추가적인 bean을 읽어서 등록

```java
@SpringBootApplication
class VehicleFactoryApplication {

    public static void main(String[] args) {
        SpringApplication.run(VehicleFactoryApplication.class, args);
    }
}
```

#### @EnableAutoConfiguration
springboot의 meta 파일을 읽어 미리 정의되어 있는 자바 설정파일(@Configuration)들을 빈으로 등록<br/>
spring.factories파일에 springboot meta가 정의되어있음.(META-INF 폴더 밑에 존재)

#### @ConditionalOnClass
특정 Class 파일이 존재하면 Bean 을 등록
```java
@Configuration
@ConditionalOnClass(DataSource.class)
class MySQLAutoconfiguration {
    //...
}
```

#### @ConditionalOnBean / @ConditionalOnMissingBean
특정 bean이 존재하면 Bean 을 등록
```java
@Bean
@ConditionalOnBean(name = "dataSource")
LocalContainerEntityManagerFactoryBean entityManagerFactory() {
    // ...
}
```

#### @ConditionalOnProperty
application.properties 구성 정보와 값에 따라 특정한 Bean을 등록하는데 사용
```java
@Bean
@ConditionalOnProperty(
    name = "usemysql", 
    havingValue = "local"
)
DataSource dataSource() {
    // ...
}
```

#### @ConditionalOnResource
config resource file의 구성 정보와 값에 따라 특정한 Bean을 등록하는데 사용
```java
@ConditionalOnResource(resources = "classpath:mysql.properties")
Properties additionalProperties() {
    // ...
}
```

#### @ConditionalOnWebApplication / @ConditionalOnNotWebApplication
현재 Application이 Web Application이라면~~~
```java
@ConditionalOnWebApplication
HealthCheckController healthCheckController() {
    // ...
}
```

#### @ConditionalExpression
SpEL 표현식을 통해 작성된 검증로직이 true인 경우라면~~~
```java
@Bean
@ConditionalOnExpression("${usemysql} && ${mysqlserver == 'local'}")
DataSource dataSource() {
    // ...
}
```

#### @Conditional
복잡한 구성을 할 수 있다. 아래는 vmoption `-Dmemory=on`으로 주고 테스트 하는 과정이다. <br/>
MemoryConfig를 등록하기전에 조건인 MemoryCondition class를 확인한다. MemoryCondition이 true라면 MemoryConfig는 bean으로 등록된다.
```java
@Configuration
@Conditional(MemoryCondition.class)
public class MemoryConfig {
    @Bean
    public MemoryController memoryController(){
        return new MemoryController(memoryFinder());
    }

    @Bean
    public MemoryFinder memoryFinder(){
        return new MemoryFinder();
    }
}

public class MemoryCondition implements Condition {
    @Override
    public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
        String memory = context.getEnvironment().getProperty("memory");// vm option
        return "on".equals(memory);
}
```


[출처]<br/>
https://www.baeldung.com/spring-core-annotations<br/>
https://wonwoo.me/218<br/>
https://xephysis.tistory.com/25