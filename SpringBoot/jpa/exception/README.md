## could not initialize proxy - no Session exception

### 상황

아래와 같은 상황이 있다고 가정.

- member entity

```java
@Entity
public class Member extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // ... //

    @OneToMany(mappedBy = "seller", cascade = CascadeType.ALL)
    private List<Product> products;

    public boolean isMySellingProduct(Product product) {
        return (this.products != null) && (products.contains(product));
    }

}
```

- 제품 삭제 로직

```java
@Override
@Transactional
public ProductResponse deleteProduct(Long productId) {
    Product product = productRepository.findById(productId).orElseThrow(() ->
            new ProductNotFoundException("해당 id를 가진 제품이 없습니다.")
    );

    Member member = memberRepository.findByUserId("admin").orElseThrow(() ->
            new MemberNotFoundException("해당 id를 가진 사용자가 없습니다.")
    );

    if (!member.isMySellingProduct(product)) {
        throw new ProductException("해당 상품의 판매자가 다릅니다.");
    }

    product.deleted();
    Product updatedProduct = productRepository.save(product); // 명시적 save

    return ProductMapper.INSTANCE.toProductResponse(updatedProduct);
}
```

아래의 조건문에서 `failed to lazily initialize a collection of role: org.example.jpasample.member.model.entity.Member.products: could not initialize proxy - no Session` exception 발생한다.

```java
if (!member.isMySellingProduct(product)) {
    throw new ProductException("해당 상품의 판매자가 다릅니다.");
}
```

그 이유는 OneToMany의 FetchType은 default가 LazyLoading이기에 때문에 exception 발생한다.

```java
@Target({ElementType.METHOD, ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
public @interface OneToMany {
    Class targetEntity() default void.class;

    CascadeType[] cascade() default {};

    FetchType fetch() default FetchType.LAZY;

    String mappedBy() default "";

    boolean orphanRemoval() default false;
}
```

### 해결 방법

1. Eager Loading
   member 와 product의 연관관계를 lazy -> eager로 변경

```java
@OneToMany(fetch = FetchType.EAGER, mappedBy = "member")
private List<Product> products;
```

2. Hibernate.initialize()
   명시적으로 products collection을 초기화

```java
@Override
@Transactional
public ProductResponse deleteProduct(Long productId, Member loginUser) {
    Product product = productRepository.findById(productId).orElseThrow(() ->
            new ProductNotFoundException("해당 id를 가진 제품이 없습니다.")
    );

    // 지연 로딩된 컬렉션 초기화
    Hibernate.initialize(loginUser.getProducts());

    // 로그인된 user가 판매하고 있는 상품인지 check
    if (!loginUser.isMySellingProduct(product)) {
        throw new ProductException("해당 상품의 판매자가 다릅니다.");
    }
    product.deleted();
    Product updatedProduct = productRepository.save(product); // 명시적 save

    return ProductMapper.INSTANCE.toProductResponse(updatedProduct);
}
```

3. fetch join 사용
   repository query 에서 fetch join 사용

```java
public interface MemberRepository extends JpaRepository<Member, Long> {

    @Query("SELECT m FROM Member m LEFT JOIN FETCH m.products WHERE m.id = :id")
    Optional<Member> findByIdWithProducts(@Param("id") Long id);
}
```

### Hibernate.initialize() vs. fetch join

- hibernate.initialize()

  - 장점
    1. 명시적 초기화: 지연 로딩된 컬렉션을 명시적으로 초기화하여 필요한 시점에 데이터를 로드 가능
    2. 성능 최적화: 필요한 시점에만 데이터를 로드하므로 불필요한 데이터 로드를 피할 수 있음.
    3. 간단한 코드 변경: 코드 변경이 간단하고, 기존의 엔티티 매핑을 크게 변경할 필요가 없음.
  - 단점
    1. 추가 코드 필요: 각 지연 로딩된 컬렉션을 사용할 때마다 초기화 코드를 추가해야함.
    2. 연결된 세션 필요: 초기화 시점에 Hibernate 세션이 열려 있어야 하므로, 서비스 계층에서 세션을 유지하는 신경써야함.
    3. N+1 문제: 여러 지연 로딩된 컬렉션을 초기화할 때 N+1 문제를 발생시킬 수 있음. 이는 성능 문제로 이어질 수 있음.

- fetch join
  - 장점
    1. 한 번의 쿼리로 로드: Fetch Join을 사용하면 한 번의 쿼리로 관련된 데이터를 모두 로드할 수 있어, 지연 로딩으로 인한 N+1 문제를 방지할 수 있음.
    2. 간단한 초기화: 명시적인 초기화 코드 없이도 데이터를 사용할 수 있음.
    3. 일관된 데이터 접근: 필요한 모든 데이터를 한 번에 가져오기 때문에 세션과 관련된 오류를 피할 수 있음.
  - 단점
    1. 복잡한 쿼리: Fetch Join을 사용한 쿼리는 복잡해질 수 있으며, 큰 데이터셋을 다룰 때 성능 저하를 초래할 수 있음.
    2. 데이터 중복: Fetch Join을 사용하여 여러 관계를 함께 로드할 때 중복된 데이터가 포함될 수 있음.
    3. 제한 사항: Hibernate에서 Fetch Join의 사용에 제한이 있을 수 있음. 예를 들어, 페이징 처리와 함께 사용하기 어려움.
