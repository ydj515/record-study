# Test Code

## JUnit
### 단위 테스트 도구
- 단위 테스트 FrameWork 중 한가지
- 외부 테스트 프로그램(케이스)를 작성하여 번거롭게 디버깅 하지 않아도 됨

### Cofiguration
- maven
- pom.xml에 denpendency 추가
```xml
<dependencies>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.8.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.hamcrest</groupId>
        <artifactId>hamcrest-all</artifactId>
        <version>1.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
- Compile Dependencies가 있는 JUnit은 hamcrest를 같이 추가해 주어야함

### Annotation
- @BeforeClass
Test Class가 처음 시작 할 때 한 번 실행 ex) network connection, DB connection

- @Before
@Test가 있는 test method가 실행 되기 전에 실행

- @AfterClass
@Test Class가 최종 끝날 때 한 번 실행 ex) network connection close, DB connection close

- @After
@Test가 있는 test method가 실행 된 후에 실행

- @Test
test를 진행하고 싶은 내용 작성

- @Ignore
test case를 무시할 수 있음

### Assert Method
- assertArrayEquals(a,b)
**배열** a와b가 일치함을 확인한다.
- assertEquals(a,b)
객체 a와b의 **값이 같은지** 확인한다.
- assertSame(a,b)
객체 a와b가 **같은 객체**임을 확인한다.
- assertTrue(a)
a가 **참인지** 확인한다.
- assertFalse(a)
a가 거짓인기 확인한다.
- assertNotNull(a)
a객체가 **Null이 아님**을 확인한다.

![flow](https://user-images.githubusercontent.com/32935365/70370382-158ab280-190a-11ea-8158-368a3bdf7956.PNG)


### Example

- Calculator.java
```java
public class Calculator {

	public int sum(int a, int b) {
		return a + b;
	}

	public int minus(int a, int b) {
		return a - b;
	}

	public int multiply(int a, int b) {
		return a * b;
	}

	public int divide(int a, int b) {
		return a / b;
	}
}
```

- CalculatorTest.java
```java
import static org.junit.Assert.assertEquals;

import org.junit.*;

public class CalculatorTest {

	Calculator calculator;

	@BeforeClass
	public static void 한번만돌림판() {
		System.out.println("Test class가 한번 돌 때 한번만 실행");
	}

	@Before
	public void setUp() {
		System.out.println("setup : @Test가 돌기 전에 한번씩 돌림판");
		calculator = new Calculator();

	}

	@Test
	public void sumTest() {
		assertEquals(3, calculator.sum(1, 2));
	}

	@Test
	public void minusTest() {
		assertEquals(0, calculator.minus(1, 1));
	}

	@Test
	public void multipleTest() {
		assertEquals(2, calculator.multiply(1, 2));
	}

	@Test
	public void divideTest() {
		assertEquals(3, calculator.divide(9, 3));
	}

	@After
	public void tearDown() {
		System.out.println("end test : @Test 끝날 때마다 실행");
	}

	@AfterClass
	public static void 테스트종료후한번돌림판() {
		System.out.println("Test class가 한번 돌 때 한번만 실행");
	}

    @Ignore
	public void ignoreMethod() {
		System.out.println("무시됨됨이야");
	}

}
```

## TDD
### What is TDD
- Test Driven Development
- 짧은 개발 서클의 반복에 의존하는 소프트웨어 개발 프로세스
- 테스트 코드 작성을 주도하는 개발 방식
- **Simple Code**를 작성하게끔 도와준다
- **Test당 개념 1개!!**

### TDD's flow
- 무엇을 테스트 할 것인가 생각
- 실패하는 테스트 작성
- 통과하는 테스트 작성
- code refactoring
- 구현해야 할 것이 있을 때까지 위의 작업을 반복  
![tdd](https://user-images.githubusercontent.com/32935365/70371341-1412b780-1915-11ea-9050-f74202a296a5.PNG)

### Strongness
- 해당 기능의 요구사항과 명세에 집중할 수 있도록 도와줌
- user requirement에 맞춰서 code 작성

### Weakness
- 늘어나는 코드량
- Business Logic, Code Design에 시간을 쏟고 Test Code 작성에도 시간을 투자해야함
- TDD, Test Code를 작성하는 방법 학습에 쏟는 시간


[출처]
https://nesoy.github.io/articles/2017-02/JUnit  