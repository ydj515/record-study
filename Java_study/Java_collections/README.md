# Java Collections

![11](https://user-images.githubusercontent.com/32935365/67305920-19689e00-f531-11e9-92a3-ed4ac44c8395.PNG)

## 특징  
![22](https://user-images.githubusercontent.com/32935365/67306651-48cbda80-f532-11e9-9b20-38c548cb03c3.PNG)  

|Collection             |Ordering   |Random Access   |Key-value  | 중복 허용 | Null 허용 | Thread safe |
|-----------------------|-----------|----------------|-----------|----------|-----------|-------------|
|`ArrayList`            |:O:        |:O:             |           |:O:       |:O:        |             |
|`LinkedList`           |:O:        |                |           |:O:       |:O:        |             |
|`Vector`         	    |:O:        |:O:             |           |:O:       |:O:        |:O:          |
|`Stack`         	    |:O:        |                |           |:O:       |:O:        |:O:          |
|`HashSet`         	    |           |                |           |          |:O:        |             |
|`TreeSet`         	    |:O:        |                |           |          |           |             |
|`HashMap`          	|           |:O:             |:O:        |          |:O:        |             |
|`TreMap`          	    |:O:        |:O:             |:O:        |          |           |             |
|`Hashtable`            |           |:O:             |:O:        |          |:O:        |             |
|`Properties`           |           |:O:             |:O:        |          |:O:        |             |
|`CopyOnWriteArrayList` |:O:        |:O:             |           |:O:       |:O:        |:O:          |
|`CopyOnWriteArraySet`  |:O:        |                |           |          |:O:        |:O:          |
|`ConcurrentHashMap`    |:O:        |:O:             |           |          |           |:O:          |



## 접근 방법
### Random Access vs. Sequential Access
- Sequential Access는 LinkedList와 같이 무조건 순차 탐색으로 찾는다.
- Random Access는 바로 그 값을 찾는다.  
![KakaoTalk_20200408_153647850](https://user-images.githubusercontent.com/32935365/78808612-a8467580-7a00-11ea-9968-ad5e8d7e6604.png)  

## List
- 객체 자체를 저장x, 해당 인덱스에 객체의 주소를 참조하여 저장

### ArrayList
- index 자동증가
- 가장 simple하게 사용하지 보통
```java
List<Object> list = new ArrayList<>();
```
### Vector
- index 자동 증가
- **대용량의 자료**를 관리할 때 유리
- **ArrayList보다 느림**
- **동기화된 메소드로 구성**되어 있어서 Multi Thread가 동시에 메소드 사용 불가! => **Thread Safe**
```java
Vector<Object v = new Vector<>();
```

### LinkedList
- arraylist보다 **중간에 추가/삭제가 빠름**
- 나머지 순차적으로 **추가/삭제와 검색은 arraylist보다 느림**
```java
List<Object> list = new LinkedList();
```



## Set
- index로 저장 순서를 유지x
- **객체를 중복 저장할 수 x**, 하나의 Null만 존재

### HashSet
- **순서가 없고, 중복 x**
```java
Set<String> set = new HashSet<>();
```

- 로또 생성기및 숫자 중복해서 들어가면 안되는 곳에 사용
```java
private final int MAX_SIZE = 6;
private final int MAX_RANDOM_NUMBER_LIMIT = 45;

public List<Integer> createLottoNumbers() {

    Set<Integer> randomNumberSet = new HashSet<Integer>();

    while (randomNumberSet.size() != MAX_SIZE) {
        int randomNumber = (int) (Math.random() * MAX_RANDOM_NUMBER_LIMIT + 1);
        randomNumberSet.add(randomNumber);
        randomNumberSet.remove(0);
    }

    return new ArrayList<>(randomNumberSet);
}
```

### TreeSet
- **binary tree** 기반
- 객체를 저장하면 **자동으로 정렬**. 부모보다 낮은 것은 왼쪽, 높은것은 오른쪽 자식에 저장
```java
Set<String> set = new TreeSet();
```

## Map
- Key와 Value를 저장
- **Key는 중복 불가**
- **동일한 키로 값을 저장하면 기존 값은 없어지고, 새로운 값으로 대체**
- Key와 Value 모두 객체

### HashMap
- **Key는 주로 String** 사용
- Object는 모든 키가 될 수 있음
```java
Map<String, String> map = new HashMap<>();
```

### HashTable
- **동기화된 메소드**로 구성되어 있어 Multi Thread 환경에서 안전. => **Thread Safe**
```java
Map<String, String> map = new Hashtable<>();
```

### TreeMap
- **binary tree** 기반
- TreeSet과 거의 똑같음
- Key 값이 저장된 **Map.Entry를 저장**
```java
Map<String, String> map = new TreeMap<>();
```

### Properties
- **Key값은 무조건 String만 허용**
```java
Map<Object, Object> map = new Properties();
```

## String

### String.Join
- list 요소 중간 사이에  , 삽입등 중간에 넣을 수 있음
```java
String resultPrintString = String.join(", ", winnerList);
```

### String.split
- 구분자로 string을 나눔
- 배열 return

```java
String carName = scanner.nextLine();    
String split[];
split = carName.split(",");
```
- 바로 Arraylist로 변환도 가능
```java
new ArrayList<>(Arrays.asList(scanner.nextLine().split(","))); // List<String>
```

### String.concat
- 문자를 붙혀줌
- 인수로 추가되는 문자열의 길이가 0 이면 그냥 원래 문자열 그대로 return
```java
// list에 문자 한개씩 붙혀줌
List<String> names = Arrays.asList("yoo", "dong", "jin", "jjang");
names.parallelStream().map((x) -> { return x.concat("!");} ).forEach(x -> System.out.println(x)); // yoo!, dong!, jin!, jjang!
```

### String.contains
- 해당 string을 포함하는 string인지 true / false를 return
```java
// carNames에서 A라는 string이 포함된 것만 !!!를 붙힘
Stream<String> a = carNames.stream().filter(x -> x.contains("A")).map(x-> x.concat("!!!"));
a.forEach(x -> System.out.println(x));
```

### String.substring
- 문자열 자르기
- index 0부터 시작
```java
String.substring(start) //문자열  start위치부터 끝까지 문자열 자르기
String.substring(start,end) //문자열  start위치 부터 end전까지 문자열 발췌
		
String str = "ABCDEFG"; //대상 문자열
str.substring(3);  // DEFG
str.substring(3, 6); // DEF
```

```java
// 마지막 3글자 자르기
String str = "ABCDEFG"; 
String result = str.substring(str.length()-3, str.length()); // EFG
```

```java
// 특정문자 이후의 문자열 제거
String str = "ABCD/DEFGH";
String result = str.substring(str.lastIndexOf("/")+1); // DEFGH
```
```java
// 특정단어(부분)만 자르기
String str = "바나나 : 1000원, 사과 : 2000원, 배 : 3000원";
String target = "사과";
int tragetNum = str.indexOf(target); 
String result = str.substring(tragetNum,(str.substring(tragetNum).indexOf("원")+tragetNum)); // 2000
```

### String.replace
- 기존문자를 바꿀 문자로 치환
- replace([기존문자],[바꿀문자])
```java
String a = "무궁화. 삼천리. 화려강산. 대한사람. 대한으로. 길이. 보전하세 ";
a.replace(".", "/"); 무궁화/ 삼천리/ 화려강산/ 대한사람/ 대한으로/ 길이/ 보전하세
```


### Sring.replaceAll
- 기존문자를 바꿀 문자로 치환
- 정규식을 쓰기 때문에 특수문자 치환이 어려움
- replaceAll([정규식],[바꿀문자])

```java
String a = "무궁화. 삼천리. 화려강산. 대한사람. 대한으로. 길이. 보전하세 ";
a = a.replaceAll(".", "/"); // 결과 : /////////////////////////////////////
```

[이미지 출처]  
https://postitforhooney.tistory.com/entry/JavaCollection-Java-Collection-Framework%EC%97%90-%EB%8C%80%ED%95%9C-%EC%9D%B4%ED%95%B4%EB%A5%BC-%ED%86%B5%ED%95%B4-Data-Structure-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0  
https://coding-factory.tistory.com/126  
