# Optional

## What is Optional
- Optional<T> 클래스는 T타입의 객체를포장해 주는 **Wrpper Class**
- **NullPointerException를 메소드로 회피 가능**
- **조건문 없어도** null 예외 처리 가능
- **명시적으로 해당 변수가 null일수도 있다는 가능성 표현**

## 사용방법
### 변수 선언
```java
Optional<String> optionalString;
Optional<Member> optionalMember;
```

## 메소드

### empty()
- null을 담고 있는 **비어있는 객체**
- 내부적으로 싱글턴 인스턴스
- 아무런 값도 가지지 않는 비어있는 Optional 객체를 반환
```java
Optional<Member> optionalMember = Optional.empty();
```

### of()
- null이 아닌 명시된 값을 가지는 Optional 객체를 반환함
- null이 아닌 객체를 담고 있는 Optional 객체를 생성
- null이 담기면 NullPointerException가 발생
```java
Optional<Member> optionalMember = Optional.of(aMember);
```

### ofNullable()
- null일 수도 있는 객체를 담고 있는 Optional 객체를 생성
- null이 담기면 NullPointerException가 발생하지 않음
```java
Optional<Member> optionalMember = Optional.ofNullable(aMember);
Optional<Member> optionalNotMember = Optional.ofNullable(null);
```

### get()
- Optional 객체에 저장된 값을 반환
- Optional 객체가 비었잇다면 NoSuchElementException 발생

### orElse()
- 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 인수로 전달된 값을 반환
- 비어있는 Optional 객체에 대해 넘어온 인자 반환
```java
Optional<String> opt = Optional.empty(); // Optional를 null로 초기화함.

System.out.println(opt.orElse("빈 Optional 객체"));
```

### orElseGet()
- 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 인수로 전달된 람다 표현식의 결괏값을 반환
- 함수형 인자를 통해 생성된 객체를 반환
```java
Optional<String> opt = Optional.empty(); // Optional를 null로 초기화함.

System.out.println(opt.orElseGet(String::new));
```

### orElseThrow()
- 저장된 값이 존재하면 그 값을 반환하고, 값이 존재하지 않으면 인수로 전달된 예외를 발생
- Optional 객체에 대해서, 넘어온 함수형 인자를 통해 생성된 예외를 발생

### isPresent()
- 저장된 값이 존재하면 true를 반환하고, 값이 존재하지 않으면 false를 반환
- get()을 호출하기 전에 isPresent()를 사용하여 Optinal 객체에 저장된 값이 null인지 아닌지 먼저 확인한 후 호출!!
```java
Optional<String> opt = Optional.ofNullable("자바 Optional 객체");

if(opt.isPresent()) {
    System.out.println(opt.get());
}
```
## Stream + Map + Filter + ifPresent
- stream, map, filter, ifPresent를 Optinal과 함께 사용하면 진가를 발휘합니다요!
- isPresent와는 다른거양~

## OptinalInt
### getAsInt()
- Optinal의 반환 값을 int형으로 반환
```java
IntStream stream = IntStream.of(4, 2, 1, 3);

OptionalInt result = stream.findFirst();
System.out.println(result.getAsInt());
```

## OptinalLong
### getAsLong()
- Optinal의 반환 값을 int형으로 반환
```java
IntStream stream = IntStream.of(4, 2, 1, 3);

OptionalInt result = stream.findFirst();
System.out.println(result.getAsLong());
```

## OptionalDouble
### getAsDouble()
- Optinal의 반환 값을 int형으로 반환
```java
IntStream stream = IntStream.of(4, 2, 1, 3);

OptionalInt result = stream.findFirst();
System.out.println(result.getAsDouble());
```

## 간단한 예제
### Example 1
```java
/* 주문을 한 회원이 살고 있는 도시를 반환한다 */
public String getCityOfMemberFromOrder(Order order) {
	Optional<Order> maybeOrder = Optional.ofNullable(order);
	if (maybeOrder.isPresent()) {
		Optional<Member> maybeMember = Optional.ofNullable(maybeOrder.get());
		if (maybeMember.isPresent()) {
			Optional<Address> maybeAddress = Optional.ofNullable(maybeMember.get());
			if (maybeAddress.isPresent()) {
				Address address = maybeAddress.get();
				Optinal<String> maybeCity = Optional.ofNullable(address.getCity());
				if (maybeCity.isPresent()) {
					return maybeCity.get();
				}
			}
		}
	}
	return "Seoul";
}
```

#### 위의 기존 조건문을 다음과 같이 바꿀 수 있다.
```java
int length = Optional.ofNullable(getText()).map(String::length).orElse(0);
```

<hr></hr>

### Example 2 Null
```java
Map<Integer, String> cities = new HashMap<>();

cities.put(1, "Seoul");
cities.put(2, "Busan");
cities.put(3, "Daejeon");

String city = cities.get(4); // returns null
int length = city == null ? 0 : city.length(); // null check
System.out.println(length);
```

#### 위의 기존 조건문을 다음과 같이 바꿀 수 있다.
```java
Optional<String> maybeCity = Optional.ofNullable(cities.get(4)); // Optional
int length = maybeCity.map(String::length).orElse(0); // null-safe
System.out.println(length);
```

<hr></hr>

### Example 3 Throw Exception (null 반환 x)
```java
List<String> cities = Arrays.asList("Seoul", "Busan", "Daejeon");

String city = null;
try {
	city = cities.get(3); // throws exception
} catch (ArrayIndexOutOfBoundsException e) {
	// ignore
}

int length = city == null ? 0 : city.length(); // null check
System.out.println(length);
```

#### 위의 기존 조건문을 다음과 같이 바꿀 수 있다.
```java
public static <T> Optional<T> getAsOptional(List<T> list, int index) {
	try {
		return Optional.of(list.get(index));
	} catch (ArrayIndexOutOfBoundsException e) {
		return Optional.empty();
	}
}

Optional<String> maybeCity = getAsOptional(cities, 3); // Optional
int length = maybeCity.map(String::length).orElse(0); // null-safe
System.out.println(length);
```

[출처]  
https://www.daleseo.com/java8-optional-after/