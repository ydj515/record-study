package multiThreadEX;

public class Calculator {

	private int memory;

	public int getMemory() {
		return memory;
	}

	// 동기화 필요
	public synchronized void setMemory(int memory) {

		this.memory = memory;

		try {
			Thread.sleep(2000); // 2초간 sleep
		} catch (Exception e) {
			e.printStackTrace();
		}

		System.out.println(Thread.currentThread().getName() + ": " + this.memory);
	}
}
