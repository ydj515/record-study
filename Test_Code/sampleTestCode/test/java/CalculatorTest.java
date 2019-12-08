import static org.junit.Assert.assertEquals;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Test;

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
