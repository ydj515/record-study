package dish;

import java.util.*;
import java.util.stream.*;

public class Main {

	public static void main(String[] args) {
		
		List<Dish> menu = Arrays.asList(
				  new Dish("pork", false, 800, Dish.Type.MEAT),
				  new Dish("beef", false, 700, Dish.Type.MEAT),
				  new Dish("chicken", false, 400, Dish.Type.MEAT),
				  new Dish("french fries", true, 530, Dish.Type.OTHER),
				  new Dish("rice", true, 350, Dish.Type.OTHER),
				  new Dish("season fruit", true, 120, Dish.Type.OTHER),
				  new Dish("pizza", true, 550, Dish.Type.OTHER),
				  new Dish("prawns", false, 300, Dish.Type.FISH),
				  new Dish("salmon", false, 450, Dish.Type.FISH)
				);
		
		menu.stream().filter(Dish::isVegetarian)			// dish -> dish.isVegetarian()
						.collect(Collectors.toList())		// List형태로 collect
						.forEach(i -> {
							System.out.println(i.getName()); //french fries rice season fruit pizza
						});

		System.out.println("=================================");
		
		List<Integer> numbers = Arrays.asList(1, 2, 1, 3, 3, 2, 4);
		numbers.stream().filter(i -> i % 2 == 0)		// 짝수만 filtering, 2,2,4
				.distinct()								// 중복 제거
				.forEach(System.out::println);			// 2 4
		
		System.out.println("=================================");
	
		List<Integer> someNumbers = Arrays.asList(1, 2, 3, 4, 5);
		Optional<Integer> firstSquareDivisibleByThree = someNumbers.stream()
																	.map(i -> i * i) // 1*1, 2*2, 3*3, 4*4, 5*5의 값을 다음 filter i 에 넘김
																	.filter(i -> i % 3 == 0) // map에서 받은 i를 filtering
																	.findFirst(); // 첫번째 요소만 찾음
		System.out.println(firstSquareDivisibleByThree.get()); // 9

		// 불가능
		int calories = menu.stream()
                    .map(Dish::getCalories)	//Stream<String>
					.sum();	// sum() 메서드 존재 X
					
		// boxed : 특화 스트림을 일반 스트림으로 변환
		Stream<Integer> calories = menu.stream()
                                		.mapToInt(Dish::getCalories)
                                		.boxed();
	}

}