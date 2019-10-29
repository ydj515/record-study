package multiThreadEX;

public class Main {

	public static void main(String[] args) {
		
		Calculator calculator = new Calculator();

		UserThread1 user1 = new UserThread1();
		user1.setCalculator(calculator);
		user1.start();

		UserThread2 user2 = new UserThread2();
		user2.setCalculator(calculator);
		user2.start();
	}

}
