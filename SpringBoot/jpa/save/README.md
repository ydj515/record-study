# SpringBoot - jpa save


#### simpleJpaRepository
JpaRepository의 구현체인 simpleJpaRepository의 save 메소드<br/>
entity 상태에 따라 persist or merge를 진행<br/>
`transient` 상태의 객체는 `EntityManager.persist()`
`detached` 상태의 객체는 `EntityManager.merge()`

`transient` 인지 `detached` 판단은 entity의 @Id property값이 null이면 transient, id값이 not null 이면 detached로 판단

```java
@Transactional
@Override
public <S extends T> S save(S entity) {

   Assert.notNull(entity, "Entity must not be null");

   if (entityInformation.isNew(entity)) {
      em.persist(entity);
      return entity;
   } else {
      return em.merge(entity);
   }
}
```
#### EntityManager.persist()
`transient` => `persistent` <br/>
영속성 컨텍스트와 전혀 관계를 맺지 않고 있던 `새로운 Entity`를 영속성 컨텍스트에 저장하여 관리하도록 함<br/>

#### EntityManager.merge()
`detached` => `persistent`
기존에 영속성 컨텍스트에 의해 관리되다가 현재는 분리되어 관리되지 않는 `detached 상태의 entity`를 다시 영속(persistent)상태로 만듦<br/>
넘겨받은 `detached 상태의 entity`의 복사본을 만들고, 그 복사본을 다시 persistent 상태로 변경하고 그 복사본을 return <br/>

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
    // @GeneratedValue
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

#### test code

```java
@PersistenctContect
private EntityManager entityManager;

@Test
public void save() {
  Post post = Post.builder()
                  .title("aaa")
                  .build();
  Post savedPost = postRepository.save(post); // persist

  entityManager.contains(post); // true
  entityManager.contains(savedPost); // true
  // post == savedPost

  Post postUpdate = Post.builder()
                          .id(post.getId())
                          .title("bbb")
                          .build();
  Post updatedPost = postRepository.save(postUpdate); // merge

  entityManager.contains(postUpdate); // false
  entityManager.contains(updatedPost); // true => merge로 반환된 return 객체가 영속화
  // postUpdate != updatedPost

  List<Post> posts = postRepository.findAll(); // insert query 동작하기 위해
}
```

