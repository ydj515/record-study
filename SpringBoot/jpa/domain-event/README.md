# SpringBoot - jpa domain event
ApplicationContext 는 BeanFactory 인터페이스를 상속받았고, ApplicationEventPublisher 인터페이스도 상속받은 인터페이스<br/>
이벤트는 ApplicationEvent 를 상속받아 만들면 되고, 리스너는 ApplicationListener를 구현하여 만들면 된다. 또는 스프링부트가 제공하는 어노테이션 @EventListener를 사용해도 된다.<br/>

1. event 구현
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

#### PostPublishEvent
```java
@Getter
public class PostPublishEvent extends ApplicationEvent {

    private final Post post;

    public PostPublishEvent(Object source) {
        super(source);
        this.post = (Post) source;
    }
}
```

#### PostListener
event listner
```java
public class PostListener {

    @EventListener
    public void onApplicationEvent(PostPublishEvent postPublishEvent) {
        System.out.println(postPublishEvent.getPost().getTitle() + " published.");
    }
}
```

#### PostRepositoryTestConfig
```java
@Configuration
public class PostRepositoryTestConfig {

    @Bean
    public PostListener postListener() {
       return new PostListener();
    }
}
```

#### test code
```java
@DataJpaTest
@Import(PostRepositoryTestConfig.class)
class PostRepositoryTest {

    @Autowired
    PostRepository postRepository;

    @Autowired
    ApplicationContext applicationContext;

    @Test
    public void event() {
          // Given
        Post post = new Post();
        post.setTitle("사내 휴일 공지 발표");
        PostPublishEvent event = new PostPublishEvent(post);

          // When
        applicationContext.publishEvent(event);
    }
}
```

2. spring data common이 제공하는 domain event
#### post entity
AbstractAggregateRoot에 이미 구현되어있는 아래의 annotation을 사용하기 위해 extends. <br/>
@DomainEvents: 이벤트를 모아놓음<br/>
@AfterDomainEventPublication: 모인 이벤트를 비움<br/>

```java
@Entity
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Post extends AbstractAggregateRoot<Post> {

    @Id
    @GeneratedValue
    private Long id;

    private String title;
    @Lob
    private String content;
    @Temporal(TemporalType.TIMESTAMP)
    LocalDateTime created;

    public Post publish() {
        this.registerEvent(new PostPublishEvent(this)); // event 등록
        return this;
    };
}
```

#### test code
```java
@DataJpaTest
// @Import(PostRepositoryTestConfig.class)
class PostRepositoryTest {

    @Autowired
    PostRepository postRepository;

    @Test
    public void crud() {
        Post post = new Post();
        post.setTitle("book");

        // Transient
        postRepository.contains(post);

        postRepository.save(post.publish()); // save 할때 AbstractAggregateRoot안에 있던 event를 발생 시킴.
        // Persistent
        postRepository.contains(post);

        postRepository.delete(post);
        postRepository.flush();
    }
}
```