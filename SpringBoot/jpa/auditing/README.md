# SpringBoot - jpa auditing

#### main
```java
@EnableJpaAuditing // 추가
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

#### BaseEntity
```java
@Getter
@Setter
@MappedSuperclass // JPA의 엔티티 클래스가 상속받을 경우 자식 클래스에게 매핑 정보를 전달
@EntityListeners(AuditingEntityListener.class) // auditing listener 추가
public abstract class BaseEntity {

    @CreatedDate
    @Column(updatable = false)
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;
    
}
```

#### Post
`CreatedBy`와 `LastModifiedBy`를 사용하기 위해서는 AuditorAware 구현 필수. <br/>
spring security의 User 사용<br/>
```java
@Getter
@Setter
@AllArgsConstructor
@Entity
public class Post extends BaseEntity {

    @Id
    @GeneratedValue
    private Long id;

    private String comment;

    ManyToOne(fetch = FetchType.LAZY)
    private Post post;

    @CreatedBy
    @ManyToOne
    private User createdBy;

    @LastModifiedBy
    @ManyToOne
    private User updatedBy;
}
```

#### AccountAuditAware
bean으로 등록 필수
```java
@Service
class SpringSecurityAuditorAware implements AuditorAware<User> { // spring security User class

  @Override
  public Optional<User> getCurrentAuditor() {

    return Optional.ofNullable(SecurityContextHolder.getContext())
            .map(SecurityContext::getAuthentication)
            .filter(Authentication::isAuthenticated)
            .map(Authentication::getPrincipal)
            .map(User.class::cast);
  }
}
```

#### 번외
번외로 model 안에 callback으로 jpa lifecycle을 이용한 `PrePersist`로도 동작 가능하다.<br/>
```java
  @Prepersist
  public void prePersist() {
    ...
  }
```


[참조]
https://www.baeldung.com/jpa-entity-lifecycle-events