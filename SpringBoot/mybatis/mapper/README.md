# SpringBoot - mybatis mapper

```xml
<sql id="whereClause">
    <where>
        <!-- mysql -->
        <if test="data.username != null and data.username != ''">
            AND username LIKE CONCAT('%', #{data.username}, '%')
        </if>
        <!-- oracle -->
        <if test="data.description != null and data.description != ''">
            AND description LIKE '%' || #{data.description} || '%'
        </if>
    </where>
</sql>
```
