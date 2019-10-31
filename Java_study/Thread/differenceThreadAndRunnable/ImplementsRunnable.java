package differenceThreadAndRunnable;

import java.util.*;
import java.util.stream.*;

public class ImplementsRunnable {

	public static void main(String args[]) {

		Scanner scanner = new Scanner(System.in);

		List<Thread> list = new ArrayList<>();

		System.out.print("입력 :  ");
		int n = scanner.nextInt();

		IntStream.range(0, n).forEach(i -> {
			list.add(new MyThread2());
		});

		list.stream().forEach(i -> {
			i.start();
		});

		scanner.close();
	}
}

class MyThread2 extends Thread {

	@Override
	public void run() {
		for (int i = 0; i < 3; i++) {
			try {
				sleep((long) Math.random());
				System.out.println(this.getName());
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

		}

	}

}