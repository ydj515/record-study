# generic vs wildcard

## generic
- 제네릭은 클래스, 인터페이스, 메소드를 정의할 때 매개변수로 받은 Type으로 정의
- 타입을 모르지만, 타입을 정해지면 그 타입의 특성에 맞게 사용
```java
// 1. 제네릭 클래스
public Coffee<T>{
	// 객체를 생성할 때, new Class<String>으로 하면 클래스 내부 T로 정의된 타입은 String이 된다.
}

// 2. 제네릭 인터페이스
public interface List<E> extends Collection<E> {
	// ... 리스트 인터페이스의 추상메소드들
}

// 3. 제네릭 메소드
public static <T> T order(T t){
/*
이 메소드에서 사용될 타입은 메소드의 수식자와 반환형 사이에 위치한다.
(메소드에서 사용할 T타입이 있음을 <T>로 알리는 것이다)
이 메소드에서 T 타입은 입력받은 T타입으로 정의된다.
*/    
	return t;
}
```

- convention
```
E - Element (used extensively by the Java Collections Framework)
K - Key
N - Number
T - Type
V - Value
S,U,V etc. - 2nd, 3rd, 4th types
```

### how to use
```java
// 1
class Box<Object>{
}
//2
class BoxAny<T>{
}



public class GenericTest {

    @Test
    void genericTest(){
        final Box<String> stringBox = new Box<>(); // 정상동작
        // 1. String은 Object 타입이므로 생성할 수 있음
        final BoxAny<String> stringBoxAny = new BoxAny<>(); // 정상동작

        printBoxObject(stringBox); // 컴파일 오류
        //1. Box<String>과 Box<Object>는 타입이 다르고 상속관계도 아니므로 오류
        printBoxAny(stringBox); // 정상동작
    }

    public static void printBoxObject(Box<Object> box) { System.out.println(box); }
    public static <T> void printBoxAny(BoxAny<T> box) { System.out.println(box); }

}
```


## wildcard
- 무슨 타입인지 모르고, 무슨 타입인지 신경쓰지 않는다. 타입을 확정하지 않고 가능성을 열어둔다.



## generic vs wildcard

```java
List<?> list; 
/*
1. 원소를 꺼내 와서는 Object에 정의되어 있는 기능만 사용하겠다. equals(), toString(), hashCode()… 
2. List에 타입이 뭐가 오든 상관 없다. 나는 List 인터페이스에 정의되어 있는 기능만 사용하겠다. 
size(), clear().. 단, 타입 파라미터와 결부된 기능은 사용하지 않겠다! add(), addAll() 
*/

List<T> list; 
/*
1. 원소를 꺼내 와서는 Object에 정의되어 있는 기능만 사용하겠다. equals(), toString(), hashCode()… 
2. List에 타입이 뭐가 오든 상관 없다. 
나는 List 인터페이스에 정의되어 있는 기능만 사용을 하고, 타입 파라미터와 결부된 기능도 사용하겠다.
```

- 한정적 와일드카드에서 extends를 사용하면 아래의 예시는 get 하였을 때는 상위 인터페이스인 Drink 객체가 된다. 하지만 add 하기에는 파라미터에서 타입이 확신할 수 없으므로 불가하다.
```java
interface Drink{
}

class Coffee implements Drink{
}

class Milk implements Drink{
}

public class GenericTest {
    private void test1(final List<? extends Drink> drinks ){
        final Drink drink = drinks.get(0);
        // <? extends Drink>에 들어가는 타입은 Drink가 될수도, Drink를 구현한 Coffee가 될수도 Milk가 될수도 있다.
        // 하지만 결국 Drink 타입을 구현하므로 drinks에서 꺼내오는 것은 Drink 타입이 된다.
        Drink drink1 = new Coffee();
        drinks.add(drink1); // 컴파일오류
        // <? extends Drink>가 Drink 타입임을 확신할 수 없다. drinks에 넣을수 없다.
    }

    private <T extends Drink> void test2(final List<T> drinks){
        final T t = drinks.get(0);
        // <T extends Drink>에 들어가는 타입은 Drink가 될수도, Drink를 구현한 Coffee가 될수도 Milk가 될수도 있다.
        // 하지만 결국 Drink 타입을 구현하므로 Drink 타입이 될 수 있다.
        drinks.add(drinks.get(0));    //정상 작동
        // T라는 제네릭타입은 입력받는 순간 정해지고 그 타입으로 고정되므로 문제없이 추가된다.
    }
}
```

- 상한 제한과 하한제한에서 와일드카드 차이
- extends 꺼내는것만 가능, super는 넣는것만 가능
```java
    private void test1(final List<? extends Drink> drinks) {
        final Drink drink = drinks.get(0);
        // <? extends Drink> 여기에 들어가는 타입은 Drink가 될수도, Drink를 구현한 Coffee가 될수도 Milk가 될수도 있다.
        // 하지만 결국 Drink 타입을 구현하므로 drinks에서 꺼내오는 것은 Drink 타입이 된다.
        Drink drink1 = new Coffee();
        drinks.add(drink1); // 컴파일오류
        // 와일드카드는 무슨 타입인지 신경쓰지 않는다.
        // 따라서 <? extends Drink>가 Drink 타입임을 확신할 수 없다. 
        // List<Coffee>일수도 List<Drink> 일수도 있다. 따라서 drinks에 넣을수 없다.

    }

    private void test3(final List<? super Drink> drinks) {
        final Object object = drinks.get(0);
        // Drink의 부모만 오기 때문에 모든 것을 포괄하는 Object 타입이 된다. (사실상 타입을 알 수 없는 것과 같다)
        Drink drink1 = new Coffee();
        drinks.add(drink1); // 정상 작동
        // Object 타입으로 변경될 것이고 특정 타입이 아닌 Object 타입이 되므로 drinks에 넣을수 있다.
        // 하지만 들어가는 것은 Drink의 하위 타입이어야 한다. 왜냐면 Drink 상위타입 어떤 것이 될 수 있는 가능성이 있기 때문이다.
    }
}
매개변수화 타입T가 생산자라면 <? extends T>를 사용한다. List<? extends Drink> drinks는 get등오로 생산만 가능하기 때문이다. 하지만, 소비자라면 <? super T>로 사용한다. 사실상 get은 무의미하며, add, remove 등을 사용가능(소비)하기 때문이다.  
```

[출처]<br/>
https://vvshinevv.tistory.com/54