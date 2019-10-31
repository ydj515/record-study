package multiThreadEX;

import java.util.stream.IntStream;

public class UserThread2 extends Thread {

	private Calculator calculator;

	public void setCalculator(Calculator calculator) {
		this.setName("calcUser2");
		this.calculator = calculator;
	}

	public void run() {
		IntStream.range(0, 100).forEach(i -> {
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			calculator.setMemory(-1);
		});
	}
}
