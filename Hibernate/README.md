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

### Configuration - pom.xml

```xml
<!-- https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator -->
<dependency>
  <groupId>org.hibernate.validator</groupId>
  <artifactId>hibernate-validator</artifactId>
  <version>6.0.8.Final</version>
</dependency>
```

### Configuration - pom.xml
```xml
<hibernate-configuration>
<session-factory>
 <property name="hibernate.dialect">org.hibernate.dialect.MySQL5Dialect</property>
 <property name="hibernate.connection.driver_class">com.mysql.jdbc.Driver</property>
 <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/testDB</property>
 <property name="hibernate.connection.username">root</property>
 <property name="hibernate.connection.password">yourDBPassword</property>

 <!-- show mysql queries output in console -->
 <property name="hibernate.show_sql">true</property>

 <!-- manage automatic database creation -->
 <property name="hibernate.hbm2ddl.auto">create</property>

 <!-- mappings for annotated classes -->
 <mapping class="testHibernate.Category"/>
 <mapping class="testHibernate.Product"/>
</session-factory>
</hibernate-configuration>
```
