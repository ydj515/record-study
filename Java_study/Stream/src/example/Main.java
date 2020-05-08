import java.util.*;
import java.util.stream.*;

public class Main {

	public static void main(String[] args) {

		List<Integer> integerList = new ArrayList<>();
		int[] intArr = { 1, 2, 3, 4, 5 };

		// Integer List -> String List
		List<String> stringList = integerList.stream().map(i -> i.toString()).collect(Collectors.toList());
줌
		// int array -> Integer List
		List<Integer> list = Arrays.stream(intArr).boxed().collect(Collectors.toList());

		// Car 객체 예제
		String inputString = "AAA,BBB,CCC";

		// List<Car> cars = parseCar(inputString);
		List<String> carNames = Arrays.asList(inputString.split(","));
		List<Car> newCarList = carNames.stream().map(name -> new Car(name)).collect(Collectors.toList());

		// carNames에서 A라는 string이 포함된 것만 !!!를 붙힘
		Stream<String> a = carNames.stream().filter(x -> x.contains("A")).map(x-> x.concat("!!!"));
		a.forEach(x -> System.out.println(x));

		// list에 문자 한개씩 붙혀줌
		List<String> names = Arrays.asList("yoo", "dong", "jin", "jjang");
		names.parallelStream().map((x) -> { return x.concat("!");} ).forEach(x -> System.out.println(x)); // yoo!, dong!, jin!, jjang!
	
		// 내림차순 정렬
		List<String> lang = Arrays.asList("Java", "Scala", "Groovy", "Python", "Go", "Swift");
		lang.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList()); // [Swift, Scala, Python, Java, Groovy, Go]
	
		//  list -> set
		Set<Integer> set = list.stream().collect(Collectors.toSet());
	
		// String[] stockOneArray -> String list
		// 이런식으로 map 여러번 쓸 수 있음
		Arrays.stream(stockOneArray).map(i -> i.replace("'", "")).map(i -> i.replace("(", ""))
									.map(i -> i.replace(")", "")).collect(Collectors.toList());
	}

	public static List<Car> parseCar(String fullString) {
		List<String> carNames = Arrays.asList(fullString.split(","));
		return carNames.stream().map(name -> new Car(name)).collect(Collectors.toList());
	}

}

class Car {
	private String carName;
	private int position;

	public Car(String carName) {
		this.carName = carName;
	}

	public String getCarName() {
		return carName;
	}

	public int getPosition() {
		return position;
	}

}