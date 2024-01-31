# SpringBoot - jpa update with @Query

#### jpa update
update문을 사용하려면 다음과 같이 작성을 해야함.<br/>
주의사항으로는 캐시와 persistenceContext를 주의해야함.

```java
// clearAutomatically : persistence context에 쌓여있던 캐시를 비워주는 것
// flushAutomatically : persistence context에 쌓여있던 변경사항을 데이터베이스에 업데이트 해주는 것
Modifying(clearAutomatically = true, flushAutomatically = true)
@Query("UPDATE Post p SET p.title = ?2 WHERE p.id = ?1")
int updateTitle(Long id, String title);
```

#### test code
```java
@Test
public void updateTitle() {
    Post spring = savePost();

    String hibernate = "hibernate";
    int update = postRepository.updateTitle(hibernate, spring.getId());
    assertThat(update).isEqualTo(1);

    // spring 객체의 title은 여전히 spring 
    Optional<Post> byId = postRepository.findById(spring.getId());
    assertThat(byId.get().getTitle()).isEqualTo(hibernate);
}
```

아래와 같이 작성해야함.

```java
Post spring = savePost();
spring.setTitle("hibernate");

List<Post> all = postRepository.findAll(); // findAll을 해야 이전의 persistence context를 flush
assertThat(all.get(0).getTitle()).isEqualTo("hibernate");
```