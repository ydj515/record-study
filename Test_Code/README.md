# test code
JUnit 5, mockito를 사용하여 테스트 코드 작성 하는 방법

### test double
실제 객체가 대신 테스트를 수행해주는 역할을 수행하는 객체<br/>
`테스트 대상(SUT: System Under Test)`을 테스트 대상이 의존하고 있는 구성요소(DOC: Depened-on Component) 로부터 분리하여 테스트하기 위해 사용<br/>
`test double`은 또한 테스트 격리를 위해서도 사용<br/>
예를 들어 Service 테스트에서 Dao를 Mocking하지 않고 실제 객체를 그대로 사용한다면 Service Layer 의 각 테스트는 실제 데이터베이스를 변화시킬 것 이고, 이 테스트는 비결정적 테스트가 됨.<br/>
하지만 Service가 사용하는 Dao를 Mocking 한다면, Service 는 데이터베이스 즉, 공유자원으로부터의 의존이 사라지고, 각각의 Service 테스트는 상호 영향을 끼치지 않는 격리된 상태가 됨.<br/>
따라서 Dummy, Fake, Stub, Spy, Mock 등의 `test double`을 사용하여 테스트들을 격리할 수 있음.<br/>
<br/>

- Dummy<br/>
Dummy는 아무런 동작도 하지 않음<br/>
인스턴스화된 객체만 필요하고, 기능까지는 필요하지 않은 경우 Dummy를 사용<br/>
주로 파라미터로 전달되기 위해 사용<br/>
예를 들어 로깅을 하는 객체는 테스트에서는 사용되지 않을 수 있음<br/>
```java
public interface Logger {
    void log();
}

public class LoggerDummy implements Logger {
    @Override
    public void log() {

    }
}
```

- Fake<br/>
Fake는 실제 동작하는 구현을 가지고 있지만, 프로덕션에서는 사용되기 적합하지 않은 객체<br/>
예를 들어 아래 그림처럼 LoginService 가 실제 프로덕션에서는 AccountDao 에 의존하여 데이터베이스를 사용<br/>
하지만 테스트코드에서는 데이터베이스 대신 HashMap 을 사용하는 FakeAccountDao 를 대신 LoginService 에 주입하여, 데이터베이스와 연결을 끊고 테스트할 수 있음<br/>

![fake](https://github.com/ydj515/record-study/assets/32935365/d4771826-9fe9-4a3f-92b6-f00314bbf0b8)

```java
@Profile("transient")
public class FakeAccountRepository implements AccountRepository {
       
       Map<User, Account> accounts = new HashMap<>();
       
       public FakeAccountRepository() {
              this.accounts.put(new User("john@bmail.com"), new UserAccount());
              this.accounts.put(new User("boby@bmail.com"), new AdminAccount());
       }
       
       String getPasswordHash(User user) {
              return accounts.get(user).getPasswordHash();
       }
}
```

- Stub<br/>
<strong>상태 검증</strong><br/>
Stub은 Dummy가 마치 실제로 동작하는 것 처럼 보이게 만든 객체<br/>
미리 반환할 데이터가 정의되어 있으며, 메소드를 호출하였을 경우 그것을 그대로 반환하는 역할만 수행<br/>

![stub](https://github.com/ydj515/record-study/assets/32935365/25d5a09b-5018-4dac-9eab-4aca2f02a380)

```java
public class GradesService {
    private final Gradebook gradebook;
    
    public GradesService(Gradebook gradebook) {
        this.gradebook = gradebook;
    }
    
    Double averageGrades(Student student) {
        return average(gradebook.gradesFor(student));
    }
}

public class GradesServiceTest {
    private Student student;
    private Gradebook gradebook;

    @Before
    public void setUp() throws Exception {
        gradebook = mock(Gradebook.class);
        student = new Student();
    }

    @Test
    public void calculates_grades_average_for_student() {
        when(gradebook.gradesFor(student)).thenReturn(grades(8, 6, 10)); //stubbing gradebook
        double averageGrades = new GradesService(gradebook).averageGrades(student);
        assertThat(averageGrades).isEqualTo(8.0);
    }
}
```
- Spy<br/>
실체 객체를 부분적으로 Stubbing 하면서 동시에 약간의 정보를 기록하는 객체<br/>
기록하는 정보에는 메소드 호출 여부, 메소드 호출 횟수 등이 포함됨<br/>
<br/>

- Mock<br/>
<strong>헹위 검증</strong><br/>
호출에 대한 기대를 명세할 수 있고, 그 명세 내용에 따라 동작하도록 설계된 객체<br/>
Mock 외의 것은 개발자가 임의로 코드를 사용하여 생성할 수 있지만, Mock은 Mocking 라이브러리에 의해 동적으로 생성됨<br/>
또한 설정에 따라 Mock은 충분히 Dummy, Stub, Spy 처럼 동작할 수 있게할 수 있음<br/>

![mock](https://github.com/ydj515/record-study/assets/32935365/47c95560-dfa0-4717-adec-5b0f8c3c5b1d)

```java
public class SecurityCentral {
    private final Window window;
    private final Door door;

    public SecurityCentral(Window window, Door door) {
        this.window = window;
        this.door = door;
    }

    void securityOn() {
        window.close();
        door.close();
    }
}

public class SecurityCentralTest {
    Window windowMock = mock(Window.class);
    Door doorMock = mock(Door.class);

    @Test
    public void enabling_security_locks_windows_and_doors() {
        SecurityCentral securityCentral = new SecurityCentral(windowMock, doorMock);
        securityCentral.securityOn();
        verify(doorMock).close();
        verify(windowMock).close();
    }
}
```

### stub
`상태 검증`(state verification) 을 사용<br/>
상태를 노출하는 메서드가 많이 추가될 수 있음<br/>
더미 객체를 생성하고 실제로 동작하는것처럼 보이게 만든 가짜 객체<br/>
호출된 요청에 대한 응답값을 미리 만들어놓고 전달<br/>
객체의 최소한의 기능만을 임의로 구현<br/>

```java
StateClass stateClass = new StateClass();
stateClass.doSomething();

assertThat(stateClass.getStatus()).isEqualTo(true);
```

### Mock
`행위 검증`(behavior verification) 을 사용<br/>
특정 메서드의 호출 등을 검증하기 때문에 구현에 의존적<br/>
특정 동작을 수행하는지(= 메소드를 제대로 콜 하는지)에 대한 검증<br/>
즉 행위검증을 추구한다는 점에서 다른 `test double`들과 구분됨<br/>

```java
BehaviorClass behaviorClass = new BehaviorClass();

verify(behaviorClass).doBehavior();
```

### WebMvcTest
웹에서 테스트하기 힘든 컨트롤러를 테스트 하는데 적합<br/>
웹상에서 요청과 응답에 대해 테스트 할 수 있을 뿐만 아니라 security 혹은 filter 까지 자동으로 테스트하며 수동으로 추가/삭제까지 가능<br/>
@Controller, @RestController 가 설정 된 클래스들을 찾아 메모리에 생성<br/>
security, @Controller, @ControllerAdvice, @JsonComponent, Filter, WebMvcConfigurer, HandlerMethodArgmentResolver만 로드되기 때문에, 실제 구동되는 어플리케이션과 똑같이 컨텍스트를 로드하는 @SpringBootTest어노테이션보다 가볍게 테스트 할 수 있음<br/>
@Service, @Repository, @Component는 사용 불가<br/>
MockMvc도 빈 등록해줌<br/>

- security를 활성화한 상태에서 `WithMockUser`를 활용하여 테스트 진행
```java
@WebMvcTest(MyController.class)
public class MyControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    @WithMockUser(username = "user", roles = {"USER"})
    public void testGetEndpoint() throws Exception {
        mockMvc.perform(get("/my-endpoint"))
                .andExpect(status().isOk());
    }
}
```

- security 비활성화한 후 진행
```java
@WebMvcTest(controllers = MyController.class, excludeFilters = {
    @ComponentScan.Filter(type = FilterType.ASSIGNABLE_TYPE, classes = WebSecurityConfigurerAdapter.class)
})
public class MyControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void testGetEndpoint() throws Exception {
        mockMvc.perform(get("/my-endpoint"))
                .andExpect(status().isOk());
    }
}
```

- service를 사용한 예시
```java
@WebMvcTest(MyController.class)
public class MyControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private MyService myService;

    @Test
    public void testGetEndpoint() throws Exception {
        // Mocking the service
        when(myService.getData()).thenReturn("Some data");

        // Performing the request and verifying the response
        mockMvc.perform(get("/my-endpoint"))
                .andExpect(status().isOk());
    }
}
```

- 단순 ExtendWith를 사용하는 예시
filter, interceptor, controlleradvice등의 기능이 필요없는 단순 request/response 테스트에 적합. spring mvc 기능이 로드가 안됨
```java
@ExtendWith({MockitoExtension.class})
class AuthControllerTest {

    @Mock
    private AuthService authService;

    @Mock
    private MemberService memberService;

    @InjectMocks
    private AuthController authController;

    private MockMvc mockMvc;

    @BeforeEach
    public void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(authController).build();
    }

    @Test
    void testLogin() throws Exception {
        // Given
        LoginRequest loginRequest = new LoginRequest("user", "password");
        when(authService.login(any(LoginRequest.class))).thenReturn(new LoginResponse("token"));

        // When & Then
        mockMvc.perform(post("/auth/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content(new ObjectMapper().writeValueAsString(loginRequest)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.token").value("token"));
    }
}
```
### AutoConfigureMockMvc
`@WebMvcTest`와 다른 점은 `@Service`나 `@Repository`가 붙은 객체들도 모두 메모리에 올린다는 것

### SpringBootTest
`@SpringBootTest`를 사용할 경우 MockMvc를 사용 할 수 없어 `@AutoConfigureMockMvc`같이 선언해서 사용해야함<br/>

```java
@SpringBootTest
@AutoConfigureMockMvc
class MyMockMvcTest {
    @Autowired
    private MockMvc mockMvc
}
```

### @DataJpaTest
JPA 관련 테스트를 하는데 사용<br/>
@Entity 클래스를 스캔 및 JPA과 관련된 설정만 등록<br/>
@Transactional 어노테이션이 자동으로 포함되어 있기 때문에 각각의 테스트는 자동으로 롤백처리<br/>
Transactional 기능이 필요하지 않으면 @Transactional(propagation = Propagation.NOT_SUPPORTED) 를 추가해주면 됨<br/>
기본적으로 in-memory embedd database에 대한 테스트를 진행<br/>
실제 DB를 사용하여 테스트를 하고 싶은 경우 @AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE) 를 추가해주면 됨<br/>

```java
// in-memory DB 사용
@DataJpaTest
class MyDataJpaTests {
}

// 실제 DB 사용
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
class MyDataJpaTests {
}

// roll back하지 않게 하려면 @Rollback(false) 사용
@Test
@Rollback(false)
public void Member_Join() throws Exception {
    // given
    Member member = new Member();
    member.setName("youngchulshin");

    // when
    Long savedId = memberService.join(member);

    // then
    Assert.assertEquals(member, memberRepository.findOne(savedId));
}
```

### @RestClientTest
Rest 통신이 예상대로 응답을 반환하는지 테스트<br/>
Jackson, GSON, Jsonb support, RestTemplateBuilder, MockRestServiceServer를 자동 구성<br/>
예를 들면, Apache HttpClient 나 Spring RestTemplate을 사용하여 외부 서버에 웹 요청을 보내는 경우에 이에 응답할 가상의 Mock서버를 만들어 테스트를 진행<br/>
```java
@RestClientTest
class MyRestClientTests {
    @Autowired
    private MockRestServiceServer mockRestServiceServer;
}
```

## test 코드 작성 방법

### 완벽하게 제어
제어 가능하게 코드를 작성하여야한다. 예를 들어 `LocalDateTime.now()` 등은 상위에서 주입받아 사용하게 작성하여야한다.<br/>
아래의 코드를 보면 `Order.create`의 입장에서는 `LocalDateTime.now()`을 인자로 받아와서 함수호출을 진행한다.<br/>
그러나 test code의 `registeredDateTime`메소드 입장에서는 이미 given절에 제어가 불가능한 `LocalDateTime.now()`가 사용되었다.<br/>
즉. 테스트를 수행하는 시점마다 계속 바뀌는 것이다. 따라서 고정값으로 test code를 작성하여야한다.<br/>
제어 불가능한 `현재시간`같은 경우는 test code에서 지양한다.<br/>

- as is
```java
@DisplayName("주문 생성 시 주문 등록 시간을 기록한다.")
@Test
void registeredDateTime() {
    // given
    LocalDateTime registeredDateTime = LocalDateTime.now();
    List<Product> products = List.of(
            createProduct("001", 1000),
            createProduct("002", 2000)
    );

    // when
    Order order = Order.create(products, registeredDateTime);

    // then
    assertThat(order.getRegisteredDateTime()).isEqualTo(registeredDateTime);
}
```

- to be
```java
@DisplayName("주문 생성 시 주문 등록 시간을 기록한다.")
@Test
void registeredDateTime() {
    // given
    LocalDateTime registeredDateTime = LocalDateTime.of(2024, 5, 15, 12, 9, 25);
    List<Product> products = List.of(
            createProduct("001", 1000),
            createProduct("002", 2000)
    );

    // when
    Order order = Order.create(products, registeredDateTime);

    // then
    assertThat(order.getRegisteredDateTime()).isEqualTo(registeredDateTime);
}
```

### 테스트 환경 독립성 보장
stock이라는 entity가 있다고 가정하자. `deductQuantity`는 재고의 수량을 차감하는 기능을 수행한다.<br/>
```java
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
public class Stock extends BaseEntity {
    public void deductQuantity(int quantity) {
        if (isQuantityLessThan(quantity)) {
            throw new IllegalArgumentException("차감할 재고 수량이 없습니다.");
        }
    this.quantity -= quantity;
    }
}
```

아래의 테스트 코드에서 given 절에 수량을 감소하는 로직이 들어가 있음을 확인할 수 있다. 이는 given절에서 충분히 test가 깨질 수 있음을 야기한다.<br/>
예를 들어서 `stock1.deductQuantity(5);`로 바꾸면 `IllegalArgumentException`이 given절에서 터지게될 것이다.<br/>
이는 지금 현재 테스트 코드에서 테스트 하고자 하는 관심사는  `orderService.createOrder` 이지만 `stock1.deductQuantity(1);`라는 재고 차감이라는 다른 행위가 혼합되어있다.<br/>
또한 given절에 로직이 추가되면서 given절을 이해하기 위해서는 맥락을 이해해야하는 허들이 생김.<br/>
given 절에는 builder or constructor로만 작성하자.(팩토리 메소드도 지양한다. - 목적을 가지고 팩토리 메소드를 만들었을 것이기 때문. => 이것 또한 맥락을 이해해야하는 허들이 생길 가능성이 있다.)<br/>

- as is
```java
@DisplayName("재고가 부족한 상품으로 주문을 생성하려는 경우 예외가 발생한다.")
@Test
void createOrderWithNoStock() {
    // given
    LocalDateTime registeredDateTime = LocalDateTime.now();

    Product product1 = createProduct(BOTTLE, "001", 1000);
    Product product2 = createProduct(BAKERY, "002", 3000);
    Product product3 = createProduct(HANDMADE, "003", 5000);
    productRepository.saveAll(List.of(product1, product2, product3));

    Stock stock1 = Stock.create("001", 2);
    Stock stock2 = Stock.create("002", 2);
    stock1.deductQuantity(1); // 재고차감 로직이 추가되면서 생각을 하게함.
    stockRepository.saveAll(List.of(stock1, stock2));

    OrderCreateServiceRequest request = OrderCreateServiceRequest.builder()
            .productNumbers(List.of("001", "001", "002", "003"))
            .build();

    // when // then
    assertThatThrownBy(() -> orderService.createOrder(request, registeredDateTime)) // 이 테스트의 관심사
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessage("재고가 부족한 상품이 있습니다.");
}

private Product createProduct(ProductType type, String productNumber, int price) {
    return Product.builder()
            .type(type)
            .productNumber(productNumber)
            .price(price)
            .sellingStatus(SELLING)
            .name("메뉴 이름")
            .build();
}
```

- to be
```java
@DisplayName("재고가 부족한 상품으로 주문을 생성하려는 경우 예외가 발생한다.")
@Test
void createOrderWithNoStock() {
    // given
    LocalDateTime registeredDateTime = LocalDateTime.now();

    Product product1 = createProduct(BOTTLE, "001", 1000);
    Product product2 = createProduct(BAKERY, "002", 3000);
    Product product3 = createProduct(HANDMADE, "003", 5000);
    productRepository.saveAll(List.of(product1, product2, product3));

    Stock stock1 = Stock.create("001", 1);
    Stock stock2 = Stock.create("002", 2);
    stockRepository.saveAll(List.of(stock1, stock2));

    OrderCreateServiceRequest request = OrderCreateServiceRequest.builder()
            .productNumbers(List.of("001", "001", "002", "003"))
            .build();

    // when // then
    assertThatThrownBy(() -> orderService.createOrder(request, registeredDateTime)) // 이 테스트의 관심사
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessage("재고가 부족한 상품이 있습니다.");
}

private Product createProduct(ProductType type, String productNumber, int price) {
    return Product.builder()
            .type(type)
            .productNumber(productNumber)
            .price(price)
            .sellingStatus(SELLING)
            .name("메뉴 이름")
            .build();
}
```
### 테스트 간 동립성 보장
하나 이상의 테스트가 공유자원을 쓰지않게 해라.<br/>
공유자원을 사용하면 테스트가 수행되어야하는 순서가 생길 수 있다.<br/>

- as is
```java
private static final Stock stock = Stock.create("001", 1);

@DisplayName("재고의 수량이 제공된 수량보다 작은지 확인한다.")
@Test
void createOrderWithNoStock() {
    // given
    int quantity = 2;

    // when

    boolean result = stock.isQuantityLessThan(quantity);

    // then
    assertThat(result).isTrue();
}

@DisplayName("재고를 주어진 개수만큼 차감할 수 있다.")
@Test
void createOrderWithNoStock() {
    // given
    int quantity = 1;

    // when

    stock.deductQuantity(quantity);
    
    // then
    assertThat(result).isTrue();
}
```

- to be
```java
@DisplayName("재고의 수량이 제공된 수량보다 작은지 확인한다.")
@Test
void createOrderWithNoStock() {
    // given
    Stock stock = Stock.create("001", 1);
    int quantity = 2;

    // when

    boolean result = stock.isQuantityLessThan(quantity);

    // then
    assertThat(result).isTrue();
}

@DisplayName("재고를 주어진 개수만큼 차감할 수 있다.")
@Test
void createOrderWithNoStock() {
    // given
    Stock stock = Stock.create("001", 1);
    int quantity = 1;

    // when

    stock.deductQuantity(quantity);
    
    // then
    assertThat(result).isTrue();
}
```

### test fixture
테스트를 위해 원하는 상태로 고정시킨 `given` 또는 `@BeforeEach`로 표현할 수 있는 일련의 객체를 의미<br/>
다음과 같은 사항을 고려해야함.

- 각 테스트 입장에서 아예 몰라도 테스트 내용을 이해하는데 문제가 없는가
- 수정해도 모든 테스트에 영향을 주지 않는가

### test fixture cleansing
test fixture에서 정한 룰 대로 테스트가 끝나면 초기화 해주는 과정을 의미<br/>
`@AfterEach`문에서 사용시에 fk 제약 조건을 확인하면서 순서대로 삭제 처리하여야함.<br/>

```java
@AfterEach
void tearDown() {
    orderProductRepository.deleteAllInBatch();
    productRepository.deleteAllInBatch();
    orderRepository.deleteAllInBatch();
    stockRepository.deleteAllInBatch();
}
```
=> 여기서 `deleteAll()`을 사용하지 않은 이유는 `deleteAll()`은 `findAll()`한 결과로 얻은 결과값을 한 row씩 삭제하여서 `deleteAllInBatch()`를 사용. <br/>

* 여기서 `@Trasactional`을 사용하면 위의 코드의 과정을 사용하지 않아도 된다. 그러나 이는 test code에서 트랜잭션 보장일 뿐, production 코드에서는 트랙잭션 보장이 아님을 유의해서 사용해야함.<br/>
* `@DataJpaTest`의 경우는 `@Trasactional`을 내장






[참조]<br/>
https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.testing.spring-boot-applications.autoconfigured-tests<br/>
https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da<br/>
https://martinfowler.com/articles/mocksArentStubs.html<br/>