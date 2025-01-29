# SpringBoot - jpa annotation

### @Embedded, @Embeddable

entity안의 값을 더 의미있게 표현하는 방법

```java
@Table(name = "shipments")
@Entity
public class Shipment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Embedded
    private Address address;
}

@Embeddable
public class Address {
    @Comment("도시")
    private String city;

    @Comment("로")
    private String street;

    @Comment("우편번호")
    private String zipcode;
}
```

### @Enumerated

enum값을 엔티티값과 매칭 시켜주는 역할.<br/>
`EnumType.ORDINAL` : default값으로 enum의 선언된 순서(int)를 저장( 1부터 시작) <br/>
`EnumType.STRING` : enum의 name값으로 저장 <br/>

```java
@Entity
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Enumerated(EnumType.STRING) // enum name값으로 db에 저장. ex) INIT, CANCELED...
    // @Enumerated(EnumType.ORDINAL) // enum의 순서를 db에 저장. ex) INIT : 1, CANCELED : 2
    @Comment("주문 상태")
    private OrderStatus orderStatus;
}

public enum OrderStatus {
    INIT("주문생성"),
    CANCELED("주문취소"),
    PAYMENT_COMPLETED("결제완료"),
    PAYMENT_FAILED("결제실패"),
    RECEIVED("판매자 주문접수"),
    COMPLETED("처리완료");

    public final String displayName;
}
```

@ManyToOne
fetch : eager
주인

@OneToMany
fetch : lazy
하인
mappedBy를 써야 DB에 반영(주인이 아닌쪽에 사용해야함)

- @EntityGraph = left outer join

- @Query Fetch Join = inner join

annotation
https://www.digitalocean.com/community/tutorials/jpa-hibernate-annotations#jpa-annotations-hibernate-annotations

N+1
https://velog.io/@jinyoungchoi95/JPA-%EB%AA%A8%EB%93%A0-N1-%EB%B0%9C%EC%83%9D-%EC%BC%80%EC%9D%B4%EC%8A%A4%EA%B3%BC-%ED%95%B4%EA%B2%B0%EC%B1%85

### Converter
JPA 엔티티 필드를 `변환기(AttributeConverter<T, R>)`를 통해 데이터베이스 컬럼과 매핑할 수 있음

```java

@Embeddable
public class Money {
    private BigDecimal amount;
    private String currency;

    protected Money() {
    }

    public Money(BigDecimal amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public String getCurrency() {
        return currency;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Money money = (Money) o;
        return Objects.equals(amount, money.amount) && Objects.equals(currency, money.currency);
    }

    @Override
    public int hashCode() {
        return Objects.hash(amount, currency);
    }

    @Override
    public String toString() {
        return "Money{" + "amount=" + amount + ", currency='" + currency + '\'' + '}';
    }
}

@Converter(autoApply = true)
public class MoneyConverter implements AttributeConverter<Money, String> {
    @Override
    public String convertToDatabaseColumn(Money attribute) {
        return attribute.getAmount() + ":" + attribute.getCurrency();
    }

    @Override
    public Money convertToEntityAttribute(String dbData) {
        String[] parts = dbData.split(":");
        return new Money(new BigDecimal(parts[0]), parts[1]);
    }
}

@Entity
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Convert(converter = MoneyConverter.class)
    private Money price;

    protected Order() {
    }

    public Order(Money price) {
        this.price = price;
    }

    public Long getId() {
        return id;
    }

    public Money getPrice() {
        return price;
    }

    public void setPrice(Money price) {
        this.price = price;
    }
}
```

- **주의사항**
`equals`를 구현하지 않으면 의도하지않은 동작이 발생할 수 있음을 유의

아래의 경우 Money 객체가 equals를 구현하지않으면 JPA는 price 필드의 변경을 감지할 수 없음

```java
Order order = orderRepository.findById(1L).orElseThrow();
order.setPrice(new Money(new BigDecimal(100), "USD"));
```

그 이유는 JPA 내부에서는 아래와 같은 방식으로 변경 여부를 확인하기 때문

```java
if (snapshot.price != current.price) {
    markAsDirty()
}
```
- snapshot.price와 current.price가 다른 객체로 간주되면 UPDATE 수행
- `equals()`가 없으면, 같은 값이어도 다른 객체로 인식하여 불필요한 업데이트가 발생하거나 반대로 변경을 감지하지 못해 업데이트가 누락될 수 있음



### Join Table, Join Column

join table은 아래와 같이 구성되어있음.<br/>
장점 : n:m 관계의 경우 join table의 entity를 따로 만들지 않아도 자동생성됨. <br/>
단점 : 조인테이블에 컬럼이 추가되는 경우 @JoinTable 전략을 사용하지 못함. <br/>

```java
@Target({ElementType.METHOD, ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface JoinTable {
    String name() default ""; // 사용할 조인 테이블의 테이블 명을 설정
    String catalog() default "";
    String schema() default "";
    JoinColumn[] joinColumns() default {}; // 현재 Entity에서 참조할 외래키(fk)를 설정
    JoinColumn[] inverseJoinColumns() default {}; // 반대 방향 Entity를 참조할 외래키(fk)를 설정
    ForeignKey foreignKey() default @ForeignKey(ConstraintMode.PROVIDER_DEFAULT);
    ForeignKey inverseForeignKey() default @ForeignKey(ConstraintMode.PROVIDER_DEFAULT);
    UniqueConstraint[] uniqueConstraints() default {};
    Index[] indexes() default {};
}
```

entity 관계별 설정은 아래와 같이 한다.<br/>

1. 1:1

```java
public class User {
    @Id
    @Column(name = "user_id")
    private Long id;

    @Column(name = "name")
    private String name;

    @OneToOne
    @JoinTable(name = "user_user_info",
    joinColumns = {@JoinColumn(name = "user_id", referencedColumnName = "user_id")},
    inverseJoinColumns = {@JoinColumn(name = "user_info_id", referencedColumnName = "user_info_id")})
    private UserInfo userInfo;

    ...
    // getter, setter
}

@Entity
public class UserInfo {
    @Id
    @Column(name = "user_info_id")
    private Long id;

    @Column(name = "address")
    private String address;

    //단방향일 경우 없어도 되는 코드
    @OneToOne(mappedBy = "userInfo")
    private User user;

    ...
    // getter, setter
}
```

2. 1:N

```java
@Entity
public class Board {
    @Id
    @Column(name = "board_id")
    private Long id;

    @Column(name = "title")
    private String title;

    @OneToMany
    @JoinTable(name = "board_comment",
            joinColumns = @JoinColumn(name = "board_id"),
            inverseJoinColumns = @JoinColumn(name = "comment_id"))
    private List<Comment> comments = new ArrayList<Comment>();

    ...
    // getter, setter
}

@Entity
public class Comment {
    @Id
    @Column(name = "comment_id")
    private Long id;

    @Column(name = "contents")
    private String contents;

    ...
    // getter, setter
}
```

3. N:1

```java
@Entity
public class Player {
    @Id
    @Column(name = "player_id")
    private Long id;

    @Column(name = "name")
    private String name;

    @ManyToOne(optional = false)
    @JoinTable(name = "player_grade",
            joinColumns = @JoinColumn(name = "player_id"),
            inverseJoinColumns = @JoinColumn(name = "grade_id"))
    private Grade grade;

    ...
    // getter, setter
}

@Entity
public class Grade {
    @Id
    @Column(name = "grade_id")
    private Long id;

    @Column(name = "code")
    private String code;

    @OneToMany(mappedBy = "grade")
    private List<Player> players = new ArrayList<Player>();

    ...
    // getter, setter
}
```

4. N:M

```java
@Entity
public class Student {
    @Id
    @Column(name = "student_id")
    private Long id;

    @Column(name = "name")
    private String name;

    @ManyToMany
    @JoinTable(name = "student_class",
            joinColumns = @JoinColumn(name = "student_id"),
            inverseJoinColumns = @JoinColumn(name = "class_id"))
    private List<Class> classes = new ArrayList<Class>();

    ...
    // getter, setter
}

@Entity
public class Class {
    @Id
    @Column(name = "class_id")
    private Long id;

    @Column(name = "name")
    private String name;

    ...
    // getter, setter
}
```

[출처]<br/>
https://www.baeldung.com/spring-data-annotations <br/>

https://github.com/KimByeongKou/fastcampus-pay <br/>

https://blog.neonkid.xyz/284 <br/>
