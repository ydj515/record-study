# SpringBoot - jpa custom repository


## custom repository
jpa repository를 사용하면서 기능 추가 및 override 가능

#### post entity
```java
@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Post {

    @Id
    @GeneratedValue
    private Long id;

    private String title;
    @Lob
    private String content;
    @Temporal(TemporalType.TIMESTAMP)
    LocalDateTime created;
}
```

1. 기능 추가
#### PostRepository
```java
public interface PostRepository {
    List<Post> findMyPosts();
}
```

#### PostRepository
```java
public interface PostCustomRepository {
    List<Post> findMyPosts();
}

```

#### PostCustomRepositoryImpl
naming convention 유지 필수.(postfix로 Impl 넣어줘야함) 아래와 같이 repositoryImplementationPostfix의 default 값이 `Impl`이기 때문

```java
@SpringBootApplication
@EnableJpaRepositories(repositoryImplementationPostfix = "Impl")
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
```

```java
@Repository
@Transactional
public class PostCustomRepositoryImpl implements PostCustomRepository {

    @Autowired
    EntityManager entityManager;

    @Override
    public List<Post> findMyPosts() {
        return entityManager.createQuery("SELECT p FROM Post AS p", Post.class).getResultList();
    }
}
```


#### PostRepository
기존 JpaRepository와 내가 custom한 repository extends
```java
public interface PostRepository extends JpaRepository<Post, Long>, PostCustomRepository {
}
```

2. 기능 override
#### PostCustomRepository
```java
public interface PostCustomRepository<T> {
    List<Post> findMyPosts();

    void delete(T entity);
}
```

#### PostCustomRepositoryImpl
```java
@Repository
@Transactional
public class PostCustomRepositoryImpl implements PostCustomRepository {

    @Autowired
    EntityManager entityManager;

    @Override
    public List<Post> findMyPosts() {
        return entityManager.createQuery("SELECT p FROM Post AS p", Post.class).getResultList();
    }

    @Override
    public void delete(Object entity) {
        entityManager.detach(entity);
    }
}
```

#### PostRepository
```java
public interface PostRepository extends JpaRepository<Post, Long>, PostCustomRepository<Post> {
}
```

#### test code
delete query의 로그는 보이지 않는다. 그 이유는 @transactional 이 붙은 스프링의 모든 테스트는 rollback transaction 이기 때문에 delete를 하지않기때문. <br/>
hibernate의 경우 rollback transaction의 경우 필요 없는 query는 실행하지 않음. <br/>
delete query를 보고 싶다면 강제로 `flush()`를 진행한다.<br/>
기본적으로 select query는 반드시 보이게 되지만, insert의 경우는 보일 수도 안보일 수도 있다.<br/>
예를 들어서 insert 후 바로 그 객체를 delete 한다면 hibernate는 필요하지않은 query라고 판단해 실행하지 않기 때문이다.<br/>
```java
@DataJpaTest
class PostRepositoryTest {

    @Autowired
    private PostRepository postRepository;

    @Test
    public void crud() {
        Post post = new Post();
        post.setContent("myContent");

        postRepository.save(post); // insert query 보임
        postRepository.findMyPosts(); // select query 보임
        postRepository.delete(post); // delete query 안보임. removed 상태로 됨.
        postRepository.flush(); 

    }

}
```

3. 모든 repository에 공통적 기능 추가
- entity가 persistance context에 들어가 있는지 체크 하는 기능 추가

#### MyRepository
```java
@NoRepositoryBean
public interface MyRepository<T, ID extends Serializable> extends JpaRepository<T, ID> {

    boolean contains(T entity);
}
```


#### SimpleMyRepository
```java
public class SimpleMyRepository<T, ID extends Serializable> extends SimpleJpaRepository<T, ID> implements MyRepository<T, ID> {

    private EntityManager entityManager;

    public SimpleMyRepository(JpaEntityInformation<T, ?> entityInformation, EntityManager entityManager) {
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

#### main
```java
@SpringBootApplication
@EnableJpaRepositories(repositoryBaseClass = SimpleMyRepository.class)
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
```

#### PostRepository
```java
public interface PostRepository extends MyRepository<Post, Long> {
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
        postRepository.contains(post) // transient 상태
        postRepository.save(post); // insert query 보임
        postRepository.contains(post) // persistent 상태
        postRepository.findMyPosts(); // select query 보임
        postRepository.delete(post); // delete query 안보임. removed 상태로 됨.
        postRepository.flush(); 

    }

}
```