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

[참조]<br/>
https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.testing.spring-boot-applications.autoconfigured-tests<br/>
https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da<br/>