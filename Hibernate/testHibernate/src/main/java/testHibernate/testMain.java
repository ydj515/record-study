package testHibernate;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class testMain {

	private static SessionFactory sessionFactory; // application에서 하나만 만든다. => 다수의 session 만들 수 있다.
	
	public static void main(String[] args) {

		Configuration conf = new Configuration();
		conf.configure("hibernate.cfg.xml"); // 설정 // "hibernate.cfg.xml"가 default 파일 이름이라 conf.configure(); 도 가능
		sessionFactory = conf.buildSessionFactory();
	
		//sessionFactory = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory(); 위의 세 줄과 동일
		
		Category category1 = new Category();
		category1.setName("Computer");
		
		Category category2 = new Category();
		category1.setName("Car");
		
		Product product1 = new Product();
		product1.setName("notebook");
		product1.setPrice(1000);
		product1.setDescription("Powerfull notebook!!!");
		product1.setCategory(category1);
		
		category1.getProducts().add(product1); // 양방향 설정
		
		Product product2 = new Product();
		product2.setName("Desktop");
		product2.setPrice(800);
		product2.setDescription("Powerfull Desktop!!!");
		product2.setCategory(category1);
		
		category1.getProducts().add(product2); // 양방향 설정
		
		Product product3 = new Product();
		product3.setName("Sonata");
		product3.setPrice(1000000);
		product3.setDescription("대중적인 자동차!!!");
		product3.setCategory(category2);
		
		category2.getProducts().add(product3); // 양방향 설정
		
		
		/*-------------------------------------------------------------------*/
		Person person1 = new Person();
		person1.setFirstName("Namyun");
		person1.setLastName("Kim");
		
		License license1 = new License();
		license1.setLicenseNumber("12345");
		license1.setIssueDate(new Date());
		license1.setPerson(person1);
		
		person1.setLicense(license1);
		
		Person person2 = new Person();
		person2.setFirstName("Alice");
		person2.setLastName("Lee");
		
		License license2 = new License();
		license2.setLicenseNumber("453256");
		license2.setIssueDate(new Date());
		license2.setPerson(person2);
		
		person1.setLicense(license2);
		

		Session session = sessionFactory.openSession(); // 세션을 만든다.
		Transaction tx = session.beginTransaction();
		
		session.save(category1);
		session.save(category2);
		session.delete(category1);
		
		//session.save(product1); // db에 저장
		//session.save(product2); // db에 저장
		//session.save(product3); // db에 저장
		
		//session.delete(product3); // product3를 지우면 연관된 category2도 자동삭제된다
		//session.delete(product1); // product1을 지우면 연관된 category1도 삭제된다? > 안된다!! category1은 product2도 연관되어 있기 때문
		
		// 만약 product1을 삭제하고 싶다면
		//product1.setCategory(null); // product1의 category를 null로 바꾸어 주고 삭제하면 된다.
		//session.delete(product1);	
		
		
		session.save(person1);
		session.save(person2);
		
		
		tx.commit();
		session.close(); 
		
	}

}
