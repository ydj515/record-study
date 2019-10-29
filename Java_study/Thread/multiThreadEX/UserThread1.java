package multiThreadEX;

public class UserThread1 extends Thread {

	private Calculator calculator;

	public void setCalculator(Calculator calculator) {
		this.setName("calcUser1");
		this.calculator = calculator;
	}

	public void run() {
		calculator.setMemory(100);
	}
}
