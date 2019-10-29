package threadEx;

public class ThreadEX1 {

	public static void main(String args[]) {

		// Thread 클래스 상속
		MyThread t1 = new MyThread();

		// Runnable 구현
		Runnable r = new MyRunnable();
		Thread t2 = new Thread(r); // 생성자 Thread(Runnable target)

		t1.start(); // 쓰레드 실행
		t2.start(); // 쓰레드 실행
		
		try {
			// thread를 다시 start하려면 생성자로 new 해주어야 다시 start를 돌릴 수 있음
			t1 = new MyThread();
			t1.start();
			
			t2 = new Thread(r);
			t2.start();
			
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}

class MyThread extends Thread {

	@Override
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println(getName());
		}
	}
}

class MyRunnable implements Runnable {

	@Override
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println(Thread.currentThread().getName());
		}
	}
}
