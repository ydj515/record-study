package multiThreadEX;

public class UserThread2 extends Thread{

	private Calculator calculator;

	public void setCalculator(Calculator calculator) {
		this.setName("calcUser2");
		this.calculator = calculator;
	}

	public void run() {
		calculator.setMemory(50);
	}
}
