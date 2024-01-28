# SpringBoot - jpa 
springboot3.x
java17


#### application.yml
```yml
spring:
  jpa:
    properties:
      hibernate:
        show_sql: true
        format_sql: true
        use_sql_comments: true
logging:
  level:
    org:
      hibernate:
        type:
          descriptor:
            sql: trace
```