package stringcalculator;

import org.junit.Before;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * 쉼표(,) 또는 콜론(:)을 구분자로 가지는 문자열을 전달하는 경우 구분자를 기준으로 분리한 각 숫자의 합을 반환 (예: “” => 0,
 * "1,2" => 3, "1,2,3" => 6, “1,2:3” => 6) 앞의 기본 구분자(쉼표, 콜론)외에 커스텀 구분자를 지정할 수
 * 있다. 커스텀 구분자는 문자열 앞부분의 “//”와 “\n” 사이에 위치하는 문자를 커스텀 구분자로 사용한다. 예를 들어
 * “//;\n1;2;3”과 같이 값을 입력할 경우 커스텀 구분자는 세미콜론(;)이며, 결과 값은 6이 반환되어야 한다. 문자열 계산기에 숫자
 * 이외의 값 또는 음수를 전달하는 경우 RuntimeException 예외를 throw한다.
 */
public class StringAddCalculatorTest {
    private StringAddCalculator cal;

    @Before
    public void setup() {
        cal = new StringAddCalculator();
    }

    @Test
    public void add_null_또는_빈문자() throws Exception {
        cal = new StringAddCalculator();
        assertEquals(0, cal.add(null));
        assertEquals(0, cal.add(""));
    }

    @Test
    public void add_숫자하나() throws Exception {
        cal = new StringAddCalculator();
        assertEquals(1, cal.add("1"));
    }

    @Test
    public void add_쉼표구분자() throws Exception {
        cal = new StringAddCalculator();
        assertEquals(3, cal.add("1,2"));
    }

    @Test
    public void add_쉼표_또는_콜론_구분자() throws Exception {
        cal = new StringAddCalculator();
        assertEquals(6, cal.add("1,2:3"));
    }

    @Test
    public void add_custom_구분자() throws Exception {
        cal = new StringAddCalculator();
        assertEquals(6, cal.add("//;\n1;2;3"));
    }

    @Test
    public void add_negative() throws Exception {
        cal = new StringAddCalculator();
        assertThrows(RuntimeException.class, () -> cal.add("-1,2,3"));
    }
}