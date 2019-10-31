package multiThreadEX;

public class Calculator {

	private int memory = 100;

	public int getMemory() {
		return memory;
	}

	// 동기화 필요
	public synchronized void setMemory(int memory) {

		this.memory += memory;

		System.out.println(Thread.currentThread().getName() + ": " + this.memory);
	}
}
