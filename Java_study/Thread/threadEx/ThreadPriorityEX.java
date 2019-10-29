package threadEx;

public class ThreadPriorityEX {

	public static void main(String args[]) {

		MyThread1 th1 = new MyThread1();
		MyThread2 th2 = new MyThread2();

		// 스레드의 우선순위 지정
		// 1 ~ 10(default : 5)
		// 숫자가 높을 수록 우선순위가 높음
		th2.setPriority(7);

		System.out.println("Priority of th1(-) : " + th1.getPriority());
		System.out.println("Priority of th2(|) : " + th2.getPriority());
		th1.start();
		th2.start();
	}
}

class MyThread1 extends Thread {
	public void run() {
		for (int i = 0; i < 300; i++) {
			System.out.print("-");
			for (int x = 0; x < 10000000; x++)
				;
		}
	}
}

class MyThread2 extends Thread {
	public void run() {
		for (int i = 0; i < 300; i++) {
			System.out.print("|");
			for (int x = 0; x < 10000000; x++)
				;
		}
	}
}