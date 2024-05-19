# JUnit 5
Java 언어에서 독립된 단위 테스트(Unit Test)를 지원해 주는 프레임워크<br/>
`JUnit5`는 `JUnit Platform`, `Jupiter`, `Vintage` 모듈이 결합된 형태

![junit](https://github.com/ydj515/record-study/assets/32935365/bb91e70d-8f5f-4587-8ad9-19ea52dcd4a1)


### 구성요소
- `JUnit Platform`
JUnit 테스트를 실행하는데 사용되는 실행환경<br/>
다양한 TestEngine 구현체를 실행하고 테스트 결과를 보고하는 역할을 수행<br/>

- `TestEngine Interface`
JUnit Platform에서 테스트 엔진을 정의하는 데 사용<br/>
이 인터페이스를 구현하여 사용자 정의 테스트 엔진을 만들 수 있음<br/>

- `TestEngine`
JUnit Platform에서 테스트를 실행하는 데 사용되는 구현체<br/>
 각각의 TestEngine은 특정한 테스트 프레임워크 또는 런처와 통합되어 동작하며, 테스트 수명주기 관리, 테스트 실행, 결과 보고 등의 기능을 제공<br/>

- `JUnit Jupiter`
JUnit 5에서 제공되는 새로운 프레임워크<br/>
테스트 작성과 실행을 위한 새로운 기능과 어노테이션을 제공하며, JUnit 4보다 더 강력하고 유연한 테스트 코드 작성이 가능<br/>

- `JUnit Vintage`
JUnit 4와의 하위 호환성을 제공하기 위한 모듈<br/>
JUnit 4로 작성된 테스트를 JUnit 5 플랫폼에서 실행할 수 있게 해줌<br/>

### 명명규칙
- `MethodName_StateUnderTest_ExpectedBehavior`
    - isAdult_AgeLessThan18_False
    - withdrawMoney_InvalidAccount_ExceptionThrown
    - admitStudent_MissingMandatoryFields_FailToAdmit

- `MethodName_ExpectedBehavior_StateUnderTest`
    - isAdult_False_AgeLessThan18
    - withdrawMoney_ThrowsException_IfAccountIsInvalid
    - admitStudent_FailToAdmit_IfMandatoryFieldsAreMissing

- `test[Feature being tested]`
    - testIsNotAnAdultIfAgeLessThan18
    - testFailToWithdrawMoneyIfAccountIsInvalid
    - testStudentIsNotAdmittedIfMandatoryFieldsAreMissing

- `Feature to be tested`
    - Should_ThrowException_When_AgeLessThan18
    - Should_FailToWithdrawMoney_ForInvalidAccount
    - Should_FailToAdmit_IfMandatoryFieldsAreMissing

- `When_StateUnderTest_Expect_ExpectedBehavior`
    - When_AgeLessThan18_Expect_isAdultAsFalse
    - When_InvalidAccount_Expect_WithdrawMoneyToFail
    - When_MandatoryFieldsAreMissing_Expect_StudentAdmissionToFail

- `Given_Preconditions_When_StateUnderTest_Then_ExpectedBehavior`


### JUnit life cycle
junit을 구성한 클래스를 구성으로 `@Test`를 수행하는 기준으로 순서 나열<br/>

- `Setup`
각 테스트 메서드가 실행되기 전에 필요한 설정 작업을 수행<br/>

- `Test`
실제 테스트가 진행되는 주요 단계<br/>
각 테스트 메서드는 개별적으로 실행되며, 코드의 예상 동작을 확인하기 위해 어설션(assertion) 또는 검증(verification)이 수행<br/>

- `Cleanup`
각 테스트 메서드가 실행된 후 필요한 정리 작업을 수행<br/>

- `Suite-level setup and cleanup`
테스트 스위트의 모든 테스트 메서드 실행 전후에 한 번씩 발생<br/>
테스트 스위트 전체에 적용되어야 하는 설정 또는 정리 작업을 수행하는 데 사용<br/>

- annotaion 형태로 나타내면 아래와 같이 수행
<strong> start -> @BeforeAll -> @BeforEach -> @Test A -> @AfterEach -> @BeforeEach -> @Test B -> @AfterEach -> @AfterAll -> End </strong>

### Given-when-then 패턴
테스트 케이스를 더 가독성 있고 유지보수하기 쉽게 구조화
- `Given` : 설정
테스트의 초기 상태 또는 사전 조건을 설정<br/>
입력 데이터나 테스트가 실행될 문맥을 지정<br/>

- `When` : 동작
테스트되는 동작 또는 이벤트를 설명<br/>
테스트되는 특정 메서드나 동작을 나타냄<br/>

- `Then` : 검증
`When`절에 설명한 동작으로 인해 기대되는 결과 또는 동작을 정의<br/>

- example
```java
@Test
void myTest() {
    // Given
    List<String> list = new ArrayList<>();

    // When
    list.add("one");
    list.add("two");
    list.add("three");

    // Then
    assertEquals(3, list.size());
    assertTrue(list.contains("three"));
    assertFalse(list.isEmpty());
}
```

### 기존의 annotation
JUnit 4에서 사용되던 annotation을 정리

- `@BeforeClass`
Test Class가 처음 시작 할 때 한 번 실행 ex) network connection, DB connection

- `@Before`
@Test가 있는 test method가 실행 되기 전에 실행

- `@AfterClass`
@Test Class가 최종 끝날 때 한 번 실행 ex) network connection close, DB connection close

- `@After`
@Test가 있는 test method가 실행 된 후에 실행

- `@Test`
test를 진행하고 싶은 내용 작성

- `@Ignore`
test case를 무시할 수 있음

### 추가된 annotation
JUnit 5 에 추가된 annotation을 정리<br/>

- `@TestFactory`
동적 테스트를위한 테스트 팩토리 메소드를 나타냄

- `@DisplayName`
테스트 클래스 또는 테스트 메소드의 사용자 정의 표시 이름을 정의<br/>
```java
@DisplayName("title")
public class Tests {
    @Test
    @DisplayName("I think this is most useful")
    public void test() {
        
    }
}
```

- `@Nested`
주석이 달린 클래스가 중첩 된 비 정적 테스트 클래스임을 나타냄<br/>
테스트 클래스 내에 중첩된 테스트 클래스를 정의<br/>
중첩 클래스는 외부 클래스와 독립적으로 설정 및 실행<br/>
```java
class NestedTest {

    @Test
    void outerTest() {
        int sum = 1 + 1;
        assertEquals(2, sum);
    }

    @Nested
    class InnerTest {
        @Test
        void innerTest() {
            int sum = 2 + 2;
            assertEquals(4, sum);
        }
    }
}
```

- `@Tag`
테스트에 태그를 지정하여 특정 태그의 테스트만 실행하거나 제외할 수 있음<br/>
```java
class TagTest {

    @Test
    @Tag("fast")
    void fastTest() {
        log.info("fast test");
    }

    @Test
    @Tag("slow")
    void slowTest() {
        log.info("slow test");
    }
}
```

- `@ExtendWith`
사용자 정의 확장명을 등록<br/>
```java
@ExtendWith(MockitoExtension.class)
class MockitoTest {

    @Mock
    private Dependency dependency;

    @InjectMocks
    private Service service;

    @Test
    void testService() {
        when(dependency.getData()).thenReturn("Mocked Data");
        String result = service.getData();
        assertEquals("Mocked Data", result);
    }

    // Example classes
    static class Dependency {
        String getData() {
            return "Real Data";
        }
    }

    static class Service {
        private final Dependency dependency;
        Service(Dependency dependency) {
            this.dependency = dependency;
        }
        String getData() {
            return dependency.getData();
        }
    }
}
```

- `@BeforeEach`
각 테스트 메서드 실행 전에 실행<br/>
애노테이션이 있는 메소드가 각 테스트 메소드 전에 실행됨 (이전 버전의 @Before)<br/>
```java
public class Tests {
    @BeforeEach
    public void setUp() {
        log.info("@BeforeEach");
    }
}
```

- `@AfterEach`
각 테스트 메서드 실행 에 실행<br/>
애노테이션이 있는 메소드가 각 테스트 메소드 후에 실행 (이전 버전의 @After)<br/>
```java
public class Tests {
    @AfterEach
    public void tearDown() {
        log.info("@AfterEach");
    }
}
```

- `@BeforeAll`
모든 테스트 메서드 실행 전에 한 번씩 실행<br/>
애노테이션이 있는 메소드가 현재 클래스의 모든 테스트 메소드보다 먼저 실행 (이전 버전의 @BeforeClass)<br/>
반드시 static으로 선언<br/>
```java
public class Tests {
    @BeforeAll
    public static void setupAll() {
        log.info("@BeforeAll");
    }
}
```

- `@AfterAll`
모든 테스트 메서드 실행 후에 한 번씩 실행<br/>
애노테이션이 있는 메소드가 현재 클래스의 모든 테스트 메소드보다 나중에 실행 (이전 버전의 @AfterClass)<br/>
반드시 static으로 선언<br/>
```java
public class Tests {
    @AfterAll
    public static void tearDownAll() {
        log.info("@AfterAll");
    }
}
```

- `@Disable`
테스트 클래스 또는 메소드를 비활성화 (이전 버전의 @Ignore)<br/>
```java
public class Tests {
	@Test
    @Disabled("Not implemented yet")
    void testNotImplemented() {
    }

    @Test
    void testImplemented() {
    	log.info("testImplemented");
    }
}
```

- `@ParameterizedTest`
파라미터를 사용한 테스트를 정의<br/>
다양한 소스(@ValueSource, @MethodSource, @CsvSource 등)에서 파라미터를 제공받을 수 있음<br/>
```java
class ParameterizedTestExample {

    @ParameterizedTest
    @ValueSource(strings = {"apple", "banana", "cherry"})
    void testWithStrings(String fruit) {
        log.info(fruit);
    }
}
```

### assertion
`org.junit.jupiter.api.Assertions` 클래스에 포함되어 있음<br/>
테스트가 예상대로 동작하는지 검증하는데 사용<br/>

- `assertEquals`
두 값이 동일한지 확인<br/>
```java
@Test
void testEquals() {
    int actual = 2 + 2;
    int expected = 4;
    assertEquals(expected, actual);
}
```

- `assertNotEquals`
두 값이 동일하지 않은지 확인<br/>
```java
@Test
void testNotEquals() {
    int actual = 2 + 2;
    int expected = 5;
    assertNotEquals(expected, actual);
}
```

- `assertTrue`
조건이 참인지 확인<br/>
```java
@Test
void testTrue() {
    assertTrue(5 > 3);
}
```

- `assertFalse`
조건이 거짓인지 확인<br/>
```java
@Test
void testFalse() {
    assertFalse(5 < 3);
}
```

- `assertNull`
객체가 null인지 확인<br/>
```java
@Test
void testNull() {
    String str = null;
    assertNull(str);
}
```

- `assertNotNull`
객체가 null이 아닌지 확인<br/>
```java
@Test
void testNotNull() {
    String str = "Hello";
    assertNotNull(str);
}
```

- `assertThrows`
예외가 발생하는지 확인<br/>
```java
@Test
void testThrows() {
    assertThrows(ArithmeticException.class, () -> {
        int result = 1 / 0;
    });
}
```

- `assertDoesNotThrow`
예외가 발생하지 않는지 확인<br/>
```java
@Test
void testDoesNotThrow() {
    assertDoesNotThrow(() -> {
        int result = 1 + 1;
    });
}
```

- `assertAll`
모든 assertion이 통과하는지 확인<br/>
그룹화된 assertion을 한 번에 확인할 수 있음<br/>
```java
@Test
void testAll() {
    assertAll(
        () -> assertEquals(4, 2 + 2),
        () -> assertTrue(5 > 3),
        () -> assertEquals("Hello", "Hello")
    );
}
```

- `assertIterableEquals`
두 컬렉션의 요소가 동일한 순서로 동일한지 확인<br/>
두 Iterable이 동일한 유형이 다르더라도 상관 없음<br/>
```java
@Test
void testIterableEquals() {
    List<String> actual = List.of("a", "b", "c");
    List<String> expected = List.of("a", "b", "c");
    assertIterableEquals(expected, actual);

    Iterable<String> al = new ArrayList<>(asList("Java", "Junit", "Test"));
    Iterable<String> ll = new LinkedList<>(asList("Java", "Junit", "Test"));
    assertIterableEquals(al, ll);
}
```

- `assertArrayEquals`
두 배열의 요소 및 순서가 동일한지 확인<br/>
```java
@Test
void testArrayEquals() {
    int[] actual = {1, 2, 3};
    int[] expected = {1, 2, 3};
    assertArrayEquals(expected, actual);
}
```

- `assertTimeout`, `assertTimeoutPreemptively`
`assertTimeout은` 특정 시간 안에 실행이 끝나는지 확인<br/>
`assertTimeoutPreemptively은` 지정한 시간 내 끝나지 않으면 바로 종료<br/>

```java
@Test
void testTimeout() {
    assertTimeout(Duration.ofSeconds(1), () -> {
        // Code that should complete within 1 second
        Thread.sleep(500);
    });
}

@Test
void testTimeoutPreemptively() {
    assertTimeoutPreemptively(Duration.ofSeconds(1), () -> {
        // Code that should complete within 1 second
        Thread.sleep(500);
    });
}
```

- `fail`
테스트를 실패 처리하며 실패 메시지를 함께 출력<br/>
개발이 완료되지 않은 테스트를 표시할 때 유용<br/>
```java
@Test
public void whenFailingATest_thenFailed() {
    // Test not completed
    fail("FAIL - test not completed");
}
```

[참조] <br/>
https://dzone.com/articles/7-popular-unit-test-naming <br/>