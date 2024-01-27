# SpringBoot - jpa


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
