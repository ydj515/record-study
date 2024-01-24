# SpringBoot - mybatis Pageable

### spring data의 pageable 사용
아래를 import한다.<br/>
org.springframework.data.domain.Pageable <br/>
org.springframework.data.web.PageableDefault <br/>

- request url
```localhost:8080/accounts?username=1&page=0&size=2&sort=id,ASC```

- pom.xml
```xml
<dependency>
    <groupId>org.springframework.data</groupId>
    <artifactId>spring-data-commons</artifactId>
</dependency>
```

- ReuqestParam
```java
@Builder
@Data
public class RequestParam<T> {

    private T data;
    private Pageable pageable;
}
```

- Account
```java
@Builder
@AllArgsConstructor
@Getter
@Setter
public class Account {
    Long id;
    String username;
    String password;
    String description;
    LocalDateTime createdAt;
    LocalDateTime updatedAt;
}
```

- controller
```java
@RequiredArgsConstructor
@RestController
@RequestMapping(value = "/accounts")
public class AccountController {

    private final AccountService accountService;

    @GetMapping("")
    public ResponseEntity<?> getAccounts(Account account,
                                         @PageableDefault(
                                                  size = 10
//                                                  ,
//                                                  sort = "id",
//                                                  direction = Sort.Direction.ASC
                                          ) Pageable pageable) {
        return ResponseEntity.ok(accountService.findAll(account, pageable));
    }
}
```

- service
```java
@Service
@RequiredArgsConstructor
public class AccountService {

    private final AccountMapper accountMapper;

    public Page<Account> findAll(Account account, Pageable pageable) {

        RequestParam<?> requestParam = RequestParam.builder()
                .data(account)
                .pageable(pageable)
                .build();

        List<Account> content = accountMapper.findAll(requestParam);
        int total = accountMapper.countAll(account);

        return new PageImpl<>(content, pageable, total);
    }
}
```

- mapper
```java
@Mapper
public interface AccountMapper {

    List<Account> findAll(RequestParam<?> requestParam);

    int countAll(Account board);
}
```

- mapper.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.demo.AccountMapper">

    <sql id="selectClause">
        SELECT
            id,
            username,
            password,
            description,
            created_at,
            updated_at
        FROM
            account account
    </sql>

    <sql id="whereClause">
        <where>
            <if test="data.username != null and data.username != ''">
                AND username LIKE CONCAT('%', #{data.username}, '%')
            </if>
            <if test="data.description != null and data.description != ''">
                AND description LIKE CONCAT('%', #{data.description}, '%')
            </if>
        </where>
    </sql>
    <sql id="orderByClause">
        <if test="pageable.sort != null and !pageable.sort.isEmpty()">
            ORDER BY
            <foreach collection="pageable.sort" item="order" separator=",">
                ${order.property} ${order.direction}
            </foreach>
        </if>
        <if test="pageable.sort == null or pageable.sort.isEmpty()">
            ORDER BY id
        </if>
    </sql>

    <select id="findAll" parameterType="com.example.demo.RequestParam" resultType="com.example.demo.Account">
            <include refid="selectClause"/>
            <include refid="whereClause"/>
            <include refid="orderByClause"></include>
        OFFSET #{pageable.offset} ROWS FETCH NEXT #{pageable.pageSize} ROWS ONLY
    </select>

    <select id="countAll" parameterType="com.example.demo.Account" resultType="int">
        SELECT
            COUNT(*) AS cnt
        FROM
            account
    </select>

</mapper>
```






### RowBounds
