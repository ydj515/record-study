# Hibernate

## What is Hibernate?
- ORM(Object Relational Mapping) Framework

## What is ORM?
- DB에 영속성을 지닌 데이터를 저장하기 위한  **데이터베이스 객체를 자바 객체로 매핑함**으로써 객체 간의 관계를 바탕으로 **SQL을 자동으로 생성**해주는 Framework이다.

## Persistence Framework(SQL Mapper vs. ORM)

### SQL Mapper
- **SQL을 명시**
  - Mybatis, JdbcTemplates
- **단순히 필드를 매핑**시키는 것이 목적
  - SQL  <--- mapping ---> Object field

### ORM
- SQL 자동 생성
  - JPA, Hibernate
- 관계형 데이터베이스의 **"관계"** 를 바탕으로 **SQL 자동 생성**
  - DB  <--- mapping ---> Object field

## Hibernate
![11](https://user-images.githubusercontent.com/32935365/63075569-23888200-bf6d-11e9-84c5-8ea763b6a70d.PNG)  

### Configuration

#### pom.xml
```xml
<!-- https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator -->
<dependency>
  <groupId>org.hibernate.validator</groupId>
  <artifactId>hibernate-validator</artifactId>
  <version>6.0.8.Final</version>
</dependency>
```

#### hibernate.cfg.xml
```xml
<hibernate-configuration>
<session-factory>
  <property name="hibernate.dialect">org.hibernate.dialect.MySQL5Dialect</property>
  <property name="hibernate.connection.driver_class">com.mysql.jdbc.Driver</property>
  <property name="hibernate.connection.username">root</property>
  <property name="hibernate.connection.password">csedbadmin</property>
  <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/testdb?serverTimezone=UTC</property>

  <!-- console에 sql문을 찍어준다 -->
  <property name="show_sql">true</property>
  <property name="format_sql">false</property>
  <!-- db table을 만드는 것을 hibernate에게 위임한다. 수행될 때마다 table 생성-->
  <property name="hibernate.hbm2ddl.auto"> create </property>

  <mapping class="testHibernate.Product"/>
  <mapping class="testHibernate.Category"/>
  <mapping class="testHibernate.Person"/>
  <mapping class="testHibernate.License"/>

</session-factory>
</hibernate-configuration>
```

#### dao-context.xml
- DataSource Bean
```xml
<bean id="dataSource" class="org.apache.commons.dbcp2.BasicDataSource" destroy-method="close">
  <property name="driverClassName" value="${jdbc.driverClassName}" />
  <property name="url" value="${jdbc.url}" />
  <property name="username" value="${jdbc.username}" />
  <property name="password" value="${jdbc.password}" />
</bean>
```

- SessionFactory Bean
```xml
<bean id="sessionFactory" class="org.springframework.orm.hibernate5.LocalSessionFactoryBean">
  <property name="dataSource" ref="dataSource"></property>
  
  <!-- @Entity를 찾아 bean으로 등록-->
  <property name="packagesToScan">
    <list>
      <value>kr.ac.hansung.model</value>
    </list>
  </property>

  <property name="hibernateProperties">
    <props>
      <prop key="hibernate.dialect">org.hibernate.dialect.MySQL5Dialect</prop>
      <prop key="hibernate.hbm2ddl.auto">create</prop> <!-- app 실행때마다 재생성. update는 계속 갱신.(재생성x) -->
      <prop key="hibernate.show_sql">true</prop>
      <prop key="hibernate.format_sql">false</prop>
    </props>
  </property>
</bean>
```

- TransactionManager Bean
```xml
<tx:annotation-driven transaction-manager="transactionManager" />

<!-- @Transactional 사용(자동 commit) -->
<bean id="transactionManager" class="org.springframework.orm.hibernate5.HibernateTransactionManager">
  <property name="sessionFactory" ref="sessionFactory"></property>
</bean>
```



### Main
```java
private static SessionFactory sessionFactory; // application에서 하나만 만든다. => 다수의 session 만들 수 있다.

sessionFactory = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory();

Session session = sessionFactory.openSession(); // 세션을 만든다.
Transaction tx = session.beginTransaction();

session.save(category1);
tx.commit();
session.close();
```

## Entity Relationships
- @Entity 키워드르 붙혀서 DB 개체로 만든다

### Types of relationship multiplicities
- @OneToOne
- @OneToMany, @ManyToOne
- @ManyToMany

### Direction of a relationship
- bidirectional
- unidirectional

#### @OneToOne & unidirectional
-Person.java
```java
@Entity
public class Person {
  @Id
  @GeneratedValue
  @Column(name="person_id")
  private long id;

  private String firstName;
  private String lastName;

}
```

-License.java
```java
@Entity
public class License {

  @Id
  @GeneratedValue
  @Column(name=“license_id")
  private long id;

  private String license_number;
  private Date issue_date;

  @OneToOne(optional=false, cascade=CascadeType.ALL)
  @JoinColumn(unique=true, name="person_id")  
  private Person person;

}
```
**=> optional=false => 연관된 엔티티가 항상 있어야함을 의미**  
**=> unique=true => FK도 유일한 값을 가진다. OneToOne이기 때문**  
**=> cascade=CascadeType.ALL는 부모쪽에서 update, delete를 할 예정이라서 여기에 지정. Person이 저장될 때 license도 자동 저장**

#### @OneToOne & bidirectional
-Person.java
```java
@Entity
public class Person {
  @Id
  @GeneratedValue
  @Column(name="person_id")
  private long id;

  private String firstName;
  private String lastName;

  @OneToOne(mappedBy="person", cascade=CascadeType.ALL)
  private License license;
}
```
**=> mappedBy 키워드**  

-License.java
```java
@Entity
public class License {

  @Id
  @GeneratedValue
  @Column(name=“license_id")
  private long id;

  private String license_number;
  private Date issue_date;

  @OneToOne(optional=false, cascade=CascadeType.ALL)
  @JoinColumn(unique=true, name="person_id")  
  private Person person;

}
```

#### @OneToMany & unidirectional
-Product.java
```java
@Entity
@Table(name = "Product") // table 이름 지정. 만약 안해주면 class 이름으로 table 생성
public class Product {

	@Id // record의 PK
	@GeneratedValue // 자동 생성
	@Column(name = "product_id") // column 이름 지정. 지정 안해줄 시 변수 이름과 동일하게 column 이름 생성
	private int id;

	private String name;
	private int price;
	private String description;

	@ManyToOne
	@JoinColumn(name = "category_id") // FK
	private Category category;
}
```

-category.java
```java
@Entity
public class Category {

	@Id
	@GeneratedValue
	private int id;
	
	private String name;
}
```


#### @OneToMany & bidirectional
**=> Many 에서 One 쪽으로 가리키는게 좋다.**  
**Many에서 가리키게 하면 1개의 참조만 있으면 대지만 One 쪽에서 가리키면 여러개의 참조 pointer를 사용해아한다.**  
**실제로 DB상의 양방향은 아니다. 객체 사이(Java 코드)에서만 양방향으로 되는 것**

-Product.java
```java
@Entity
@Table(name = "Product") // table 이름 지정. 만약 안해주면 class 이름으로 table 생성
public class Product {

	@Id // record의 PK
	@GeneratedValue // 자동 생성
	@Column(name = "product_id") // column 이름 지정. 지정 안해줄 시 변수 이름과 동일하게 column 이름 생성
	private int id;

	private String name;
	private int price;
	private String description;

	@ManyToOne
	@JoinColumn(name = "category_id") // FK
	private Category category;

}
```

-category.java
```java
@Entity
public class Category {

	@Id
	@GeneratedValue
	private int id;
	
	private String name;
	
	// cascade=CascadeType.ALL : 연관된 객체까지 지우든 업데이트하든 같이 저장됨(persist, delete) -> product가 저장되면 연관된 Category도 자동 저장됨
	// mappedBy="category" : 필드 이름과 동일하게 넣으면 된다. 양방향 관계 설정시 관계의 주체가 되는 쪽에서 정의
	// fetch=FetchType.LAZY : Category 정보를 읽을 때 products의 모든 정보를 읽을 필요가 없다. 필요할 때만 읽는다. OneToMany, ManyToMany에선 default
	// fetch=FetchType.EAGER : Category 정보를 읽을 때 모든 product들의 정보를 읽는다. OneToOne, ManyToOne에선 default
	@OneToMany(mappedBy = "category", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
	private Set<Product> products = new HashSet<Product>();
	
}
```

#### @ManyToMany & bidirectional
-Author.java
```java
@Entity
public class Author {

	@Id // record의 PK
	@GeneratedValue // 자동 생성
	@Column(name = "author_id") // column 이름 지정. 지정 안해줄 시 변수 이름과 동일하게 column 이름 생성
	private int id;

  @Column(name = "author_name")
	private String name;
}
```

-Book.java
```java
@Entity
public class Book {

	@Id // record의 PK
	@GeneratedValue // 자동 생성
	@Column(name = "book_id") // column 이름 지정. 지정 안해줄 시 변수 이름과 동일하게 column 이름 생성
	private int id;

  @Column(name = "book_name")
	private String title;
  
  @ManyToMany(casecade = CascadeType.ALL)
  @JoinTable(name = "author_book", // Book -> Author, author_book이라는 table 생성
             joinColumns = { @JoinColumn(name = "book_id") }, //FK
             inverseJoinColumns = { @JoinColumn(name = "author_id") } //FK
  private set<Author> authors;
}
```
**=> JoinTable 키워드 : 해당 이름으로 테이블을 생성**  
