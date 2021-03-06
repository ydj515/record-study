package differenceThreadAndRunnable;

import java.util.*;
import java.util.stream.*;

public class ExtendsThread {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		List<Thread> list = new ArrayList<>();

		System.out.print("입력 :  ");
		int n = scanner.nextInt();

		IntStream.range(0, n).forEach(i -> {
			Runnable r = new Mythread();
			list.add(new Thread(r));
		});

		list.stream().forEach(i -> {
			i.start();
		});

		scanner.close();
	}
}

class Mythread implements Runnable {

	@Override
	public void run() {
		for (int i = 0; i < 3; i++) {
			try {
				Thread.sleep((long) Math.random());
				System.out.println(this.hashCode());
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
		}

	}

}