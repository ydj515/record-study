package stringcalculator;

import java.util.*;
import java.util.regex.*;

public class StringAddCalculator {

    private static final String REG_EXPRESSION = "//(.)\\n(.*)";
    private static final String DEFAULT_SEPARATOR = ",|:";

    public int add(String inputString) {

        if (isNullOrEmpty(inputString)) {
            return 0;
        }

        List<String> numbers = separateStringBySeparator(inputString);
        validPositiveNumbers(numbers);

        return sumNumbers(numbers);
    }

    private boolean isNullOrEmpty(String inputString) {
        if (inputString == null || inputString.length() == 0) {
            return true;
        }
        return false;
    }

    private List<String> separateStringBySeparator(String inputString) {

        Pattern pattern = Pattern.compile(REG_EXPRESSION);
        Matcher matcher = pattern.matcher(inputString);

        String separator = DEFAULT_SEPARATOR;
        String restString = inputString;

        if (matcher.find()) {
            separator = matcher.group(1); // 구분자
            restString = matcher.group(2); // 나머지 string
        }

        return new ArrayList<String>(Arrays.asList(restString.split(separator)));
    }

    private void validPositiveNumbers(List<String> numbers) {
        if (numbers.stream().filter(i -> Integer.parseInt(i) < 0).count() > 0) {
            throw new RuntimeException();
        }
    }

    private int sumNumbers(List<String> numbers) {
        return numbers.stream().filter(i -> Integer.parseInt(i) >= 0).mapToInt(j -> Integer.parseInt(j)).sum();
    }
}