# Java API

## toString() vs String.valueOf()
### toString()
- 대상 값이 null이면 NPE를 발생시키고 Object에 담긴 값이 String이 아니여도 출력
### String.valueOf()
- 파라미터가 null이면 문자열 "null"을 만들어서 반환

```java
String s = null;
System.out.println((String) s); // 'null' text return
System.out.println(String.valueOf(s)); // 'null' text return
System.out.println(s.toString()); // NullPointException
```

## Integer.parseInt() vs Integer.valueOf()
### Integer.parseInt()
- Integer 클래스로 리턴되어 산술 연산을 할 수 x => int 형변환 해줘야함
- 음수 인식
### Integer.valueOf()
- int를 리턴하여 null값이 들어가서는 안됨
- 음수 인식 x
- 내부에서 parseInt()를 사용

```java

```

## Collections.EMPTY_LIST vs Collections.emptyList()
- 둘다 empty list를 반환

### Collections.EMPTY_LIST
```java
List list = Collections.EMPTY_LIST;
Set set = Collections.EMPTY_SET;
Map map = Collections.EMPTY_MAP;
```
- 위의 3줄은 타입을 지정하려면 아래와 같이 캐스팅 해줘야함
```java
List<String> list = (List<String>) Collections.EMPTY_LIST;
Set<Long> set = (Set<Long>) Collections.EMPTY_SET;
Map<Date, String> map = (Map<Date, String>) Collections.EMPTY_MAP;
```

### Collections.emptyList()
- emptyList()는 아래와 같이 바로 타입 지정 가능
- **Collections.EMPTY_LIST보다 권장되는 방법**
```java
List<String> s = Collections.emptyList();
Set<Long> l = Collections.emptySet();
Map<Date, String> d = Collections.emptyMap();
```

## Arrays.sort() vs Collections.sort()의 차이
### Arrays.sort()
- 배열 정렬의 경우
Ex) byte[], char[], double[], int[], Object[], T[] 등 * Object Array에서는 TimSort(**Merge Sort + Insertion Sort**)를 사용
- Object Array: 새로 정의한 클래스에 대한 배열 * Primitive Array에서는 Dual Pivot QuickSort(**Quick Sort + Insertion Sort**)를 사용
- Primitive Array: 기본 자료형에 대한 배열

### Collections.sort()
- List Collection 정렬의 경우
- Ex) ArrayList, LinkedList, Vector 등은 내부적으로 Arrays.sort()를 사용

## 배열 -> list
```java
ArrayList<String> list = new ArrayList<>(Arrays.asList(array));
```
```java
ArrayList<String> list = new ArrayList<>();
Collections.addAll(list, arr);
```
```java
List list = Arrays.stream(arr).collect(Collectors.toList());
```

## list -> 배열
```java
String[] arr = list.toArray(new String[list.size()]);
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

## Map 정렬
### key를 기준으로 정렬(TreeMap을 이용)
- TreeMap을 대해 <a href="https://github.com/ydj515/record-study/blob/master/Java_study/Java_collections/README.md">여기</a>에 써 놓았음
```java
System.out.println("------------sort 전 -------------");
Iterator it1 = hashMap.keySet().iterator();
while (it1.hasNext()) {
	int temp = (int) it1.next();
	System.out.println(temp + " = " + hashMap.get(temp));
}
TreeMap<Integer, String> tm = new TreeMap<Integer, String>(hashMap);
System.out.println("------------sort 후 -------------");
while (it1.hasNext()) {
	int temp = (int) it1.next();
	System.out.println(temp + " = " + hashMap.get(temp));
}
// Iterator<Integer> iteratorKey = tm.keySet().iterator(); // 키값 오름차순 정렬(기본)
```

### value를 기준으로 정렬
```java
Iterator it2 = sortByValue(hashSet).iterator();

public static List sortByValue(final Map map) {

		List<String> list = new ArrayList();

		list.addAll(map.keySet());

		Collections.sort(list, new Comparator() {

			public int compare(Object o1, Object o2) {

				Object v1 = map.get(o1);

				Object v2 = map.get(o2);

				return ((Comparable) v2).compareTo(v1);
			}
		});
	// Collections.reverse(list); // 주석시 오름차순

	return list;
}
```

## Priority Queue vs. List sort
- 알고리즘 문제를 풀다 보면 list sort를 사용하면 시간 초과가 나지만 Priority Queue를 사용하여 해결할 수 있다.
- 그 이유는 **priority Queue는 heap상태로 정렬을 유지하기 때문에 시간이 훨씬 단축**된다.
- Priority Queue TopN을 유지하지만, TopN에서 완전한 Sort가 이루어지지 않는 다.
- 아래는 quick sort와 priority Queue의 시간차이다.(참고용)  
![image](https://user-images.githubusercontent.com/32935365/80867701-88893100-8cd0-11ea-88b1-33eeb3ab0df8.png)  

### Priority Queue
```java
PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
PriorityQueue<Integer> priorityQueue2 = new PriorityQueue<>(Collections.reverseOrder()); // 내림차순

priorityQueue.offer(123);
priorityQueue.poll(123);
```

### List sort
```java
List<Integeer> list = new ArrayList<>();
Collections.sort(list); // 오름차순

List<Integeer> list2 = new ArrayList<>();
list.sort(Collections.reverseOrder()); // 내림차순
```

[출처]  
https://m.blog.naver.com/occidere/220918234464  
https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html  
https://gbsb.tistory.com/247  
https://www.joinc.co.kr/w/Site/Test/PqueueVsQsort  
ttps://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html  