# SpringBoot - jpa pageable

스프링 MVC의 HandlerMethodArgumentResolver 는 스프링 MVC 핸들러 메소드에서 매개변수로 받을 수 있는 객체를 확장하고 싶을 때 사용할 수 있는 인터페이스. <br/>
Pageable, Sort 파라미터를 받을 수 있음. <br/>

#### Post
```java
@Entity
@Getter
@Setter
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

#### PostRepository
```java
public interface PostRepository extends JpaRepository<Post, Long> {
}
```

#### PostController
```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @GetMapping("/posts")
    public Page<Post> getPosts(Pageable pageable) { // default size : 20
        return postRepository.findAll(pageable);
    }
}
```

#### test code
`localhost:8080?page=0&size=10&sort=created,desc&sort=title`
```java
@Test
public void getPosts() throws Exception {
  // Given
  Post post = new Post();
  post.setTitle("Jack");
  postRepository.save(post);

  // When
  mockMvc.perform(get("/posts")
                  .param("page", "0")
                  .param("size", "10")
                  .param("sort", "created,desc") // 첫번째 정렬 옵션
                  .param("sort", "title")) // 두번째 정렬 옵션
    .andDo(print())
    // Then
    .andExpect(status().isOk())
    .andExpect(jsonPath("$.content[0].title", is(equalTo("Jack"))));
  ;
}
```