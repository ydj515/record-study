# SpringBoot - jpa hateoas

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

#### PostController
```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @GetMapping("/posts")
    public PagedModel<EntityModel<Post>> getPosts(Pageable pageable, PagedResourcesAssembler<Post> assembler) {
      return assembler.toModel(postRepository.findAll(pageable));
    }
}
```

#### test code
```java
@Test
public void getPosts() throws Exception {
  createPosts();

  mockMvc.perform(get("/posts")
                  .param("page", "2")
                  .param("size", "10")
                  .param("sort", "created,desc")
                  .param("sort", "title"))
    .andDo(print())
    .andExpect(status().isOk())
    .andExpect(jsonPath("$._embedded.postList[0].title", is(equalTo("Jack"))));
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
```

#### result
아래의 결과를 얻을 수 있다.
```
MockHttpServletResponse:
           Status = 200
    Error message = null
          Headers = [Content-Type:"application/hal+json"]
     Content type = application/hal+json
             Body = {"_embedded":{"postList":[{"id":59,"title":"Jack","content":null,"created":null},{"id":76,"title":"Jack","content":null,"created":null},{"id":61,"title":"Jack","content":null,"created":null},{"id":63,"title":"Jack","content":null,"created":null},{"id":54,"title":"Jack","content":null,"created":null},{"id":94,"title":"Jack","content":null,"created":null},{"id":93,"title":"Jack","content":null,"created":null},{"id":92,"title":"Jack","content":null,"created":null},{"id":91,"title":"Jack","content":null,"created":null},{"id":89,"title":"Jack","content":null,"created":null}]},"_links":{"first":{"href":"http://localhost/posts?page=0&size=10&sort=created,desc&sort=title,asc"},"prev":{"href":"http://localhost/posts?page=1&size=10&sort=created,desc&sort=title,asc"},"self":{"href":"http://localhost/posts?page=2&size=10&sort=created,desc&sort=title,asc"},"next":{"href":"http://localhost/posts?page=3&size=10&sort=created,desc&sort=title,asc"},"last":{"href":"http://localhost/posts?page=9&size=10&sort=created,desc&sort=title,asc"}},"page":{"size":10,"totalElements":100,"totalPages":10,"number":2}}
    Forwarded URL = null
   Redirected URL = null
          Cookies = []
```

body를 자세히보면 pagenation을 할 수 있는 link 정보와, 실제 데이터값 list, page 내용들이 담겨있다.
```json 
{
  "_embedded": {
    "postList": [
      {
        "id": 59,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 76,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 61,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 63,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 54,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 94,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 93,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 92,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 91,
        "title": "Jack",
        "content": null,
        "created": null
      },
      {
        "id": 89,
        "title": "Jack",
        "content": null,
        "created": null
      }
    ]
  },
  "_links": {
    "first": {
      "href": "http://localhost/posts?page=0&size=10&sort=created,desc&sort=title,asc"
    },
    "prev": {
      "href": "http://localhost/posts?page=1&size=10&sort=created,desc&sort=title,asc"
    },
    "self": {
      "href": "http://localhost/posts?page=2&size=10&sort=created,desc&sort=title,asc"
    },
    "next": {
      "href": "http://localhost/posts?page=3&size=10&sort=created,desc&sort=title,asc"
    },
    "last": {
      "href": "http://localhost/posts?page=9&size=10&sort=created,desc&sort=title,asc"
    }
  },
  "page": {
    "size": 10,
    "totalElements": 100,
    "totalPages": 10,
    "number": 2
  }
}
```


[출처]
https://docs.spring.io/spring-hateoas/docs/current/reference/html/