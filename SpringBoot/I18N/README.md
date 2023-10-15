# SpringBoot - I18N

### 파일 작성
resources 디렉토리 밑에 messages.properties를 만들고 각 언어별 properties를 만들면 자동으로 bundle.
수동으로 bean 등록도 가능
![11111](https://github.com/ydj515/record-study/assets/32935365/cc627a02-a209-4be3-8537-5cfcabf94e80)

#### 자동 bean
- messages.properties
```properties
greeting=Hello, {0}
```

- messages_ko_KR.properties
```properties
greeting=안녕, {0}
```

- Apprunner.java
```java
@Component
public class AppRunner implements ApplicationRunner {

    @Autowired
    MessageSource messageSource;
 
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println(messageSource.getMessage("greeting", new String[]{ "dj"}, Locale.KOREA)); // 안녕, dj
        System.out.println(messageSource.getMessage("greeting", new String[]{ "dj"}, Locale.getDefault())); // Hello, dj
    }
}
```

#### 수동 bean
```java
@Bean
public MessageSource messageSource() {
    var messageSource = new ResourceBundleMessageSource();
    messageSource.setBasename("messages");
    messageSource.setDefaultEncoding("UTF-8");
 
    return messageSource;
}
```


### message resource reload
run 중에 build만 해주면 됨
```java
@Bean
public MessageSource messageSource() {
    var messageSource = new ReloadableResourceBundleMessageSource();
    messageSource.setBasename("classpath:/messages");
    messageSource.setDefaultEncoding("UTF-8");
    messageSource.setCacheSeconds(3); // 캐시 설정
 
    return messageSource;
}

```