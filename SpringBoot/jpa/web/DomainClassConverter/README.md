# SpringBoot - jpa doamin class converter
DomainClassConverter는 자동으로 ConverterRegistry 를 상속받고 있도록 등록되어 있음.<br/>
ConverterRegistry 에 들어가면, 스프링 MVC 에서 어떤 데이터를 바인딩 받을 때 등록된 것을 사용하게 된다. DomainClassConverter에는 크게 ToEntityConverter, ToIdConverter 가 등록됨.<br/>
id, Entity 간 상호 변화를 할 수 있도록 돕는다.


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
formatter,converter 둘다 등록해서 사용 가능하지만 
formatter를 사용하지 못하는 이유는 id타입이 long이기 때문.(무조건 문자열만 가능)
domainClassConverter가 동작함. formatter는 string만 동작.
```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @GetMapping("/posts/{id}")
    public String getPost(@PathVariable Long id) {
        Optional<Post> byId = postRepository.findById(id);
        Post post = byId.get();
        return post.getTitle();
    }

    @GetMapping("/posts/{id}") // 위의 getmapping과 동일하게 동작
    public String getPost(@PathVariable("id") Post post) {
        return post.getTitle();
    }
}
```

#### test code
```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class PostControllerTest {

    @Autowired
    MockMvc mockMvc;

    @Autowired
    PostRepository postRepository;

    @Test
    public void getPost() throws Exception {
        // Given
        Post post = new Post();
        post.setTitle("aaa");
        postRepository.save(post);

        // When
        mockMvc.perform(get("/posts/" + post.getId().toString()))
                .andDo(print())
                // Then
                .andExpect(status().isOk())
                .andExpect(content().string("aaa"))
        ;
    }
}
```


[출처]<br/>
https://docs.spring.io/spring-data/jpa/reference/repositories/core-extensions.html#core.web.basic.domain-class-converter