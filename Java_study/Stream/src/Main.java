import java.util.*;

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
	}

}
