package threadEx;

public class ThreadGroupEX {

	public static void main(String args[]) throws Exception {
		
		ThreadGroup main = Thread.currentThread().getThreadGroup();
		ThreadGroup grp1 = new ThreadGroup("Group1");
		ThreadGroup grp2 = new ThreadGroup("Group2");

		// ThreadGroup(ThreadGroup parent, String name);
		ThreadGroup subGrp1 = new ThreadGroup(grp1, "SubGroup1");

		grp1.setMaxPriority(3);

		Runnable r = new Runnable() {
			public void run() {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
				}
			}
		};
		
		// Thread(ThreadGroup tg, Runnable r, String name)
		new Thread(grp1, r, "th1").start();
		new Thread(subGrp1, r, "th2").start();
		new Thread(grp2, r, "th3").start();
		
		System.out.println(">> List of TheadGroup : " + main.getName() + ", Active ThreadGroup: "
				+ main.activeGroupCount() + ", Active Thread: " + main.activeCount());
		main.list();
	}

}
