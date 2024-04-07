# SpringBoot - jpa annotation

@ManyToOne
fetch : eager
주인

@OneToMany
fetch : lazy
하인
mappedBy를 써야 DB에 반영(주인이 아닌쪽에 사용해야함)


- @EntityGraph = left outer join

- @Query Fetch Join = inner join 

annotation
https://www.digitalocean.com/community/tutorials/jpa-hibernate-annotations#jpa-annotations-hibernate-annotations

N+1
https://velog.io/@jinyoungchoi95/JPA-%EB%AA%A8%EB%93%A0-N1-%EB%B0%9C%EC%83%9D-%EC%BC%80%EC%9D%B4%EC%8A%A4%EA%B3%BC-%ED%95%B4%EA%B2%B0%EC%B1%85




[출처]<br/>
https://www.baeldung.com/spring-data-annotations



https://github.com/KimByeongKou/fastcampus-pay

https://blog.neonkid.xyz/284