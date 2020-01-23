# Lamda expression

## What is Lamda expression
- 식별자 없이 실행 가능한 함수
- 메소드를 하나의 식으로 표현
- **익명 클래스와 비슷**하다고 보면됨
- **가독성 증가** 및 **함수형 프로그래밍** 가능

## 간단 사용법
```
(매개변수, ...) -> { 실행문 ...}
```

### 예제1
```java
// 익명 클래스
new Object() {
    int minNum(int x, int y) {
        return x < y ? x : y;
    }
};

// 람다
(x,y) -> x < y ? x : y;
```
### 예제2
```java
// 익명 클래스
new Thread(new Runnable() {
    public void run() {
        System.out.println("익명 클래스 사용");
    }
}).start();

// 람다
new Thread(() -> {
    System.out.println("람다 표현식 사용");
}).start();
```

## 함수형 인터페이스 선언
- **@FunctionalInterface**을 사용

```java
public class Main {

	public static void main(String[] args) {

		MyNum max = (x, y) -> (x >= y) ? x : y;
		
        System.out.println(max.getMax(10, 30));
	}

}

@FunctionalInterface // 함수형 인터페이스 체크 어노테이션
interface MyNum {
	int getMax(int num1, int num2);
}
```