# SpringBoot - hateos
Hypermedia As The Engine Of Application State <br/>
애플리케이션의 상태는 Hyperlink를 이용해 전이<br/>
클라이언트가 서버로부터 특정 요청을 할 때, 요청에 필요한 URI를 응답에 포함시켜 반환<br/>
접근 가능한 추가 API들이 `links`라는 이름으로 제공.<br/>
예를 들어서 GET요청 이후 수정, 삭제할 때 이러한 동작을 URI를 이용해 알려줌<br/>

#### 변경점
|변경 전          |변경 후                  |
|------------------|-------------------------------|
|ResourceSupport    |RepresentationModel                  |
|Resource       |EntityModel                   |
|Resources            |CollectionModel             |
|PagedResources         |PagedModel                    |	
	
	


#### pom.xml
```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-hateoas</artifactId>
</dependency>
```

#### post
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

#### repository
```java
public interface PostRepository extends JpaRepository<Post, Long> {
}
```

#### controller
```java
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PagedResourcesAssembler;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.Link;
import org.springframework.hateoas.PagedModel;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@RestController
@RequiredArgsConstructor
@RequestMapping("/posts")
public class PostController {

    private final PostRepository postRepository;

    @GetMapping
    public ResponseEntity<PagedModel<EntityModel<Post>>> getAllPosts(Pageable pageable, PagedResourcesAssembler<Post> assembler) {
        PagedModel<EntityModel<Post>> postModels = assembler.toModel(postRepository.findAll(pageable), post -> postToModel(post, false));
        return ResponseEntity.ok(postModels);
    }

    @GetMapping("/{id}")
    public ResponseEntity<EntityModel<Post>> getPost(@PathVariable("id") Post post) {
        EntityModel<Post> postModel = postToModel(post, true);
        return ResponseEntity.ok(postModel);
    }

    @PostMapping
    public ResponseEntity<EntityModel<Post>> createPost(@RequestBody Post newPost) {
        Post savedPost = postRepository.save(newPost);
        return ResponseEntity.created(linkTo(methodOn(PostController.class).getPost(savedPost)).toUri())
                .body(postToModel(savedPost, true));
    }

    @PutMapping("/{id}")
    public ResponseEntity<EntityModel<Post>> updatePost(@PathVariable("id") Post existingPost, @RequestBody Post updatedPost) {
        existingPost.setTitle(updatedPost.getTitle());
        existingPost.setContent(updatedPost.getContent());
        Post savedPost = postRepository.save(existingPost);
        return ResponseEntity.ok(postToModel(savedPost, true));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deletePost(@PathVariable("id") Post post) {
        postRepository.delete(post);
        return ResponseEntity.noContent().build();
    }

    private EntityModel<Post> postToModel(Post post, boolean includeAllActions) {
        List<Link> links = new ArrayList<>();
        links.add(linkTo(methodOn(PostController.class).getPost(post)).withSelfRel());
        links.add(linkTo(methodOn(PostController.class).getAllPosts(null, null)).withRel("all-posts"));

        // 추가로 필요한 링크를 여기에 추가
        if (includeAllActions) {
            links.add(linkTo(methodOn(PostController.class).updatePost(post, null)).withRel("update-post"));
            links.add(linkTo(methodOn(PostController.class).deletePost(post)).withRel("delete-post"));
        }

        return EntityModel.of(post, links);
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
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
class PostControllerTest {

    @Autowired
    MockMvc mockMvc;

    @Autowired
    PostRepository postRepository;

    @Test
    public void getAllPosts() throws Exception {
        createPosts();

        mockMvc.perform(get("/posts")
                        .param("page", "2")
                        .param("size", "10")
                        .param("sort", "created,desc")
                        .param("sort", "title"))
                .andDo(print())
                .andExpect(status().isOk())
//                .andExpect(jsonPath("$._embedded.postList[0].title", is(equalTo("Jack"))));
        ;
    }

    private void createPosts() {
        int postsCount = 100;

        while(postsCount > 0) {
            Post post = new Post();
            post.setTitle("Jack");
            postRepository.save(post);
            postsCount--;
        }
    }
}
```

#### response
아래와 같은 응답을 받을 수 있다. (link정보, page정보 등)
```json
{
  "_embedded": {
    "postList": [
      {
        "_links": {
          "all-posts": {
            "href": "http://localhost/posts"
          },
          "delete-post": {
            "href": "http://localhost/posts/58"
          },
          "self": {
            "href": "http://localhost/posts/58"
          },
          "update-post": {
            "href": "http://localhost/posts/58"
          }
        },
        "content": null,
        "created": null,
        "id": 58,
        "title": "Jack"
      },
      ...
    ]
  },
  "_links": {
    "first": {
      "href": "http://localhost/posts?page=0&size=10&sort=created,desc&sort=title,asc"
    },
    "last": {
      "href": "http://localhost/posts?page=9&size=10&sort=created,desc&sort=title,asc"
    },
    "next": {
      "href": "http://localhost/posts?page=3&size=10&sort=created,desc&sort=title,asc"
    },
    "prev": {
      "href": "http://localhost/posts?page=1&size=10&sort=created,desc&sort=title,asc"
    },
    "self": {
      "href": "http://localhost/posts?page=2&size=10&sort=created,desc&sort=title,asc"
    }
  },
  "page": {
    "number": 2,
    "size": 10,
    "totalElements": 100,
    "totalPages": 10
  }
}
```


#### todo..
http method도 같이 넣어 주고 싶으면 아래의 모델을 사용해보면 되지 않을까
```java
@Getter
@Setter
public class CustomEntityModel<T> extends EntityModel<T> {

    private String httpMethod;

    public CustomEntityModel(T content, Link... links) {
        super(content, List.of(links));
    }

    @Override
    public Links getLinks() {
        List<Link> links = (List<Link>) super.getLinks();
        if (httpMethod != null) {
            links.add(Link.of(httpMethod, "httpMethod"));
        }
        return Links.of(links);
    }
}
```
[출처]
https://docs.spring.io/spring-hateoas/docs/current/reference/html/