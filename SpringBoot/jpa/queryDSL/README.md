# SpringBoot - jpa query DSL
환경 설정은 springboot2와 3이 다름.<br/>
Optional<T> findOne(Predicate) <br/>
List<T>|Page<T>|Iterable<T> ... findAll(Predicate) <br/>

#### pom.xml(boot2)
```xml
<dependency>
  <groupId>com.querydsl</groupId>
  <artifactId>querydsl-apt</artifactId>
</dependency>
<dependency>
  <groupId>com.querydsl</groupId>
  <artifactId>querydsl-jpa</artifactId>
</dependency>
...

<plugin>
    <groupId>com.mysema.maven</groupId>
    <artifactId>apt-maven-plugin</artifactId>
    <version>1.1.3</version>
    <executions>
    <execution>
        <goals>
        <goal>process</goal>
        </goals>
        <configuration>
        <outputDirectory>target/generated-sources/java</outputDirectory>
        <processor>com.querydsl.apt.jpa.JPAAnnotationProcessor</processor>
        </configuration>
    </execution>
    </executions>
</plugin>
```

#### pom.xml(boot3)
```xml
<dependency>
    <groupId>com.querydsl</groupId>
    <artifactId>querydsl-apt</artifactId>
    <version>5.0.0</version>
    <classifier>jakarta</classifier>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>com.querydsl</groupId>
    <artifactId>querydsl-jpa</artifactId>
    <version>5.0.0</version>
    <classifier>jakarta</classifier>
</dependency>
```

1. 기본적인 query DSL
#### entity
```java
@Getter
@Setter
@Entity
public class Account {

    @Id
    @GeneratedValue
    private Long id;
    private String username;
    private String firstName;
    private String lastName;
}
```

#### QAccount
maven - compile을 하게 되면 target 하위 폴더에 `Q`로 시작하는 entity가 만들어짐

```java
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QAccount extends EntityPathBase<Account> {

    private static final long serialVersionUID = 760879443L;

    public static final QAccount account = new QAccount("account");

    public final NumberPath<Long> id = createNumber("id", Long.class);

    public final StringPath name = createString("name");

    public QAccount(String variable) {
        super(Account.class, forVariable(variable));
    }

    public QAccount(Path<? extends Account> path) {
        super(path.getType(), path.getMetadata());
    }

    public QAccount(PathMetadata metadata) {
        super(Account.class, metadata);
    }

}
```

#### AccountRepository
```java
public interface AccountRepository extends JpaRepository<Account, Long>, QuerydslPredicateExecutor<Account> {
}
```

#### test code
```java
@DataJpaTest
class AccountRepositoryTest {

    @Autowired
    AccountRepository accountRepository;

    @Test
    public void crud() {
        Predicate predicate = QAccount.account.firstName.containsIgnoreCase("dongjin")
                            .and(QAccount.account.lastName.startsWith("yoo"));

        Optional<Account> one = accountRepository.findOne(predicate);
        assertThat(one).isEmpty();
    }
}
```

2. customrepository 사용하였다면 아래와 같이 적용
customrepository를 사용했다면 기본적으로 아래의 내용을 반드시 추가해줘야 querydslexecutor가 읽을 수 있다.

#### PostRepository
```java
public interface PostRepository extends MyRepository<Post, Long>, QuerydslPredicateExecutor<Post > {
}
```

SimpleJpaRepository -> QuerydslJpaRepository로 변경
#### SimpleMyRepository
```java
public class SimpleMyRepository<T, ID extends Serializable> extends QuerydslJpaRepository<T, ID> implements MyRepository<T, ID> {

    private EntityManager entityManager;

    public SimpleMyRepository(JpaEntityInformation<T,ID> entityInformation, EntityManager entityManager) {
        super(entityInformation, entityManager);
        this.entityManager = entityManager;
    }

    @Override
    public boolean contains(T entity) {
        return entityManager.contains(entity);
    }

    @Override
    public List<T> findAll() {
        System.out.println("custom findAll");
        return super.findAll();
    }
}
```

#### test code
```java
@DataJpaTest
class PostRepositoryTest {

    @Autowired
    private PostRepository postRepository;

    @Test
    public void crud() {
        Post post = new Post();
        post.setContent("myContent");
        
        postRepository.save(post);
        
        Predicate predicate = QPost.post.content.containsIgnoreCase("my");
        Optional<Post> one = postRepository.findOne(predicate);
    }

}
```