# SpringBoot - jpa annotation

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
