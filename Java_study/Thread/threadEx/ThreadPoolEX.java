package threadEx;

import java.util.*;
import java.util.concurrent.*;
import java.util.stream.*;

public class ThreadPoolEX {

	public static void main(String[] args) {

		List<MyThreadPool> threadPools = new ArrayList<>();

		IntStream.range(0, 5).forEach(i -> {
			threadPools.add(new MyThreadPool("thread" + i));
		});

		// 스레드 풀 갯수 제한
		ExecutorService executorService = Executors.newFixedThreadPool(3);

		// 현재 5개를 넣엇지만 3개까지만 돌릴 수 있으므로 나머지 2개는 실행중인 스레드가 끝날 때 까지 대기
		threadPools.forEach(i -> {
			executorService.execute(i);
		});

		// MyThreadPool runnable1 = new MyThreadPool("thread1");
		// MyThreadPool runnable2 = new MyThreadPool("thread2");
		// MyThreadPool runnable3 = new MyThreadPool("thread3");
		// MyThreadPool runnable4 = new MyThreadPool("thread4");
		// MyThreadPool runnable5 = new MyThreadPool("thread5");
		//
		// ExecutorService executorService = Executors.newFixedThreadPool(3);
		// executorService.execute(runnable1);
		// executorService.execute(runnable2);
		// executorService.execute(runnable3);
		// executorService.execute(runnable4);
		// executorService.execute(runnable5);

		// shutdown()은 실행중인 작업 뿐만 아니라 작업 큐에 대기하고 있는 모든 작업들을 다 '처리'하고 쓰레드풀을 중지
		executorService.shutdown();

		try {
			if (!executorService.awaitTermination(5, TimeUnit.MINUTES)) { // .awaitTermination은 shutdown()메서드 호출이후 해당
																			// 시간만큼안에 쓰레드풀의 작업이 전부 수행하지 못하면 실행중이던 쓰레드에
																			// 인터럽트를 발생시키고 false 반환
				executorService.shutdownNow();
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
			executorService.shutdownNow();
		}
	}

}

class MyThreadPool implements Runnable {

	private static final String MSG_TEMPLATE = "출력중 [%s][%d회]";
	private final String threadName;

	public MyThreadPool(String threadName) {
		this.threadName = threadName;
	}

	public void run() {
		for (int i = 1; i <= 100; i++) {
			System.out.println(String.format(MSG_TEMPLATE, threadName, i));
		}
	}

}
