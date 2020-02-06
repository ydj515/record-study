# Java API

## toString() vs String.valueOf()
### toString()
- 대상 값이 null이면 NPE를 발생시키고 Object에 담긴 값이 String이 아니여도 출력
### String.valueOf()
- 파라미터가 null이면 문자열 "null"을 만들어서 반환

```


```

## Comparable vs Comparator
### Comparable
- 클래스의 기본 정렬 기준을 설정하는 인터페이스

## Comparator
- 기본 정렬 기준과는 다르게 정렬하고 싶을 때 이용하는 클래스

```java
import java.lang.Comparable;
import java.util.Arrays; //퀵소트 사용하기 위해 import

class Student implements Comparable<Student> {
	String name; //이름
	int id; //학번
	double score; //학점
	public Student(String name, int id, double score){
		this.name = name;
		this.id = id;
		this.score = score;
	}
	public String toString(){ //출력용 toString오버라이드
		return "이름: "+name+", 학번: "+id+", 학점: "+score;
	}
	/* 기본 정렬 기준: 학번 오름차순 */
	public int compareTo(Student anotherStudent) {
		return Integer.compare(id, anotherStudent.id);
	}
}

public class Main{
	public static void main(String[] args) {
		Student student[] = new Student[5];
		//순서대로 "이름", 학번, 학점
		student[0] = new Student("Dave", 20120001, 4.2);
		student[1] = new Student("Amie", 20150001, 4.5);
		student[2] = new Student("Emma", 20110001, 3.5);
		student[3] = new Student("Brad", 20130001, 2.8);
		student[4] = new Student("Cara", 20140001, 4.2);
		Arrays.sort(student); //퀵소트
		for(int i=0;i<5;i++) //toString에 정의된 형식으로 출력
			System.out.println(student[i]);
	}
}

```

- 이렇게 구현해도 무방(내림차순)
```java
Arrays.sort(student, new Comparator<Student>(){
	@Override
	public int compare(Student s1, Student s2) {
		double s1Score = s1.score;
		double s2Score = s2.score;
		return Double.compare(s2Score, s1Score);//학점 내림차순
	}
});
```

- 학점내림차순 후 학번 오름차순
```java
Arrays.sort(student, new Comparator<Student>(){
	@Override
	public int compare(Student s1, Student s2) {
		double s1Score = s1.score;
		double s2Score = s2.score;
		if(s1Score == s2Score){ //학점이 같으면
			return Double.compare(s1.id, s2.id); //학번 오름차순
		}
		return Double.compare(s2Score, s1Score);//학점 내림차순
	}
});
```

- 전체 code
```java
import java.lang.Comparable;
import java.util.Arrays;
import java.util.Comparator; //Comparator 사용하기 위한 import

class Student implements Comparable<Student> {
	String name; //이름
	int id; //학번
	double score; //학점
	public Student(String name, int id, double score){
		this.name = name;
		this.id = id;
		this.score = score;
	}
	public String toString(){
		return "이름: "+name+", 학번: "+id+", 학점: "+score;
	}
	/* 기본 정렬 기준: 학번 오름차순 */
	public int compareTo(Student anotherStudent) {
		return Integer.compare(id, anotherStudent.id);
	}
}

public class Main{
	public static void main(String[] args) {
		Student student[] = new Student[5];
		//순서대로 "이름", 학번, 학점
		student[0] = new Student("Dave", 20120001, 4.2);
		student[1] = new Student("Amie", 20150001, 4.5);
		student[2] = new Student("Emma", 20110001, 3.5);
		student[3] = new Student("Brad", 20130001, 2.8);
		student[4] = new Student("Cara", 20140001, 4.2);
		
		Arrays.sort(student, new Comparator<Student>(){
			public int compare(Student s1, Student s2) {
				double s1Score = s1.score;
				double s2Score = s2.score;
				if(s1Score == s2Score){ //학점이 같으면
					return Double.compare(s1.id, s2.id); //학번 오름차순
				}
				return Double.compare(s2Score, s1Score);//내림차순
			}
		});
		for(int i=0;i<5;i++)
			System.out.println(student[i]);
	}
}
```





[출처]  
https://m.blog.naver.com/occidere/220918234464  
https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html  