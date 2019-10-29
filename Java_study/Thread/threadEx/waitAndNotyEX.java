package threadEx;

import java.util.*;

public class waitAndNotyEX {

	public static SyncStack ss = new SyncStack();

	public static void main(String[] args) {

		// SyncStack에 5데이터삽입

		new PushRunnable('J').start();
		new PushRunnable('A').start();
		new PushRunnable('B').start();
		new PushRunnable('O').start();
		new PushRunnable('O').start();

		new PopRunnable().start();// O
		new PopRunnable().start();// O
		new PopRunnable().start();// B
		new PopRunnable().start();// A
		new PopRunnable().start();// J

		new PopRunnable().start();// 대기상태

		try {
			Thread.sleep(5000);
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("===== passed 5 seconds======");
		new PushRunnable('K').start();
	}

}

class SyncStack {

	private List<Character> buffer = new ArrayList<>();

	public synchronized char pop() {

		while (buffer.size() == 0) {
			try {
				System.out.println("stack대기:");
				
				this.wait(); // 공유 자원에 접근할 때 다른 스레드가 사용하고 있다면 기다리라
				
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

		Character c = buffer.get(buffer.size() - 1);
		buffer.remove(buffer.size() - 1);
		
		System.out.println("stack삭제:" + c);

		return c;
	}

	public synchronized void push(char c) {
		
		this.notify(); // wait하고 있는 스레드가 있다면 wait하는 스레드 시작하라고 noti

		buffer.add(c);

		System.out.println("stack삽입:" + c);
	}
}

class PopRunnable extends Thread {

	public void run() {
		waitAndNotyEX.ss.pop();
	}
}

class PushRunnable extends Thread {

	private char c;

	public PushRunnable(char c) {
		this.c = c;
	}

	public void run() {
		waitAndNotyEX.ss.push(c);
	}
}