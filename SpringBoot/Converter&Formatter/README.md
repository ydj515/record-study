# SpringBoot - Converter & Formatter

- Event.java
```java
@Data
public class Event {
 
    Integer id;
    String title;
 
    @Override
    public String toString() {
        return "Event{" +
                "id=" + id +
                ", title='" + title + '\'' +
                '}';
    }
}
```

- EventController.java
```java
@RestController
public class EventController {
 
    @GetMapping("/event/{event}")
    public String getEvent(@PathVariable Event event) { // 사용자가 입력한 숫자(이벤트id)를 Event 타입으로 변환해야한다.
        System.out.println(event);
        return event.getId().toString();
    }
}
```

### PropetyEditor 사용
Spring이 제공하는 DataBinder 인터페이스를 통해 사용됨
Spring 3 이전까지 DataBinder가 변환 작업에 사용한 인터페이스
값(상태 정보)을 저장하고 있어 thread-safe하지 않음(다른 thread끼리 공유됨)
일반적인 싱글톤 scope 빈으로 등록해서 사용 불가
Object - String간의 변환만 할 수 있어 사용 범위가 제한적

- PropertyEditor.java
```java
public class EventEditor extends PropertyEditorSupport {

    @Override
    public void setAsText(String text) throws IllegalArgumentException {
        // 사용자가 입력한 문자열을 int로 변환하여 Event 객체를 생성한 뒤 setValue() 호출
        setValue(new Event(Integer.parseInt(text)));
    }
 
    @Override
    public String getAsText() {
        Event event = (Event) getValue();
        return event.getId().toString();
    }
}
```

- EventController.java
```java
@RestController
public class EventController {
 
    // 컨트롤러에서 사용할 바인더 등록
    @InitBinder
    public void init(WebDataBinder webDataBinder) {
        // WebDataBinder에 Event 클래스 타입을 처리할 EventEditor 바인더 등록
        webDataBinder.registerCustomEditor(Event.class, new EventEditor());
    }
 
    @GetMapping("/event/{event}")
    public String getEvent(@PathVariable Event event) {
        System.out.println(event);
        return event.getId().toString();
    }
}
```


### Converter 사용
Spring3 부터 추가
참조 타입끼리 변환 가능한 일반적인(general) 기능의 변환기
Spring이 제공하는 ConversionService 인터페이스를 통해 사용
값(상태 정보)을 저장하지 않으므로 thread-safe함
빈으로 등록해서 사용 가능
Converter<Source, Target>

#### 1. Web config에 등록하여 사용
- WebConfig.java
```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
 
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addConverter(new EventConverter.StringToEventConverter());
    }
}

```

#### 2. Converter를 빈으로 등록하여 사용
- EventConverter.java
```java
public class EventConverter {
 
    @Component
    public static class StringToEventConverter implements Converter<String, Event> {
 
        @Override
        public Event convert(String s) {
            return new Event(Integer.parseInt(s));
        }
    }
 
    @Component
    public static class EventToStringConverter implements Converter<Event, String> {
 
        @Override
        public String convert(Event event) {
            return event.getId().toString();
        }
    }
}
```


### Formatter
Spring3 부터 추가
PropertyEditor의 대체제
Object - String 간 변환을 담당하는 web 특화 인터페이스
Spring이 제공하는 ConversionService 인터페이스를 통해 사용됨
값(상태 정보)을 저장하지 않으므로 thread-safe
빈으로 등록해서 사용
문자열을 Locale에 따라 다국화 처리 하는 기능 제공 (Optional)

- EventFormatter.java
```java
@Component
public class EventFormatter implements Formatter<Event> {
 
    @Override
    public Event parse(String text, Locale locale) throws ParseException { // PropertyEditor.setAsText()
        return new Event(Integer.parseInt(text));
    }
 
    @Override
    public String print(Event object, Locale locale) { // PropertyEditor.getAsText()
        return object.getId().toString();
    }
}
```

#### 1. Web config에 등록하여 사용

- WebConfig.java
```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
 
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addFormatter(new EventFormatter());
    }
}
```

#### 2. Formater 빈으로 등록하여 사용
- EventFormatter.java
```java
@Component
public class EventFormatter implements Formatter<Event> {
 
    @Override
    public Event parse(String text, Locale locale) throws ParseException {
        System.out.println("EventFormatter");
        return new Event(Integer.parseInt(text));
    }
 
    @Override
    public String print(Event object, Locale locale) {
        return object.getId().toString();
    }
}
```

<img width="503" alt="스크린샷 2023-10-22 오전 3 17 26" src="https://github.com/ydj515/record-study/assets/32935365/67786dc7-f022-4e6d-a896-32bf30e76b91">

DefaultFormattingConversionService는 위 그림과 같이 ConversionService와 FormatterRegistry, ConverterRegistry를 구현하여 해당 인터페이스들의 기능을 포함

또한 여러 기본 Converter와 Formatter가 등록되어있음. 아래 코드로 확인
- Apprunner.java
```java
@Component
public class Apprunner implements ApplicationRunner{

    @Autowired
    ConversionService와 conversionService;

    @Override
    public void run(ApplicationArguments args) {
        System.out.println(conversionService);
    }
}
```

기본적으로 Converter를 레지스트리에 등록할때는 ConverterRegistry에, Formatter는 FormatterRegistry에 등록해서 사용하지만 FormatterRegistry는 ConverterRegistry를 상속받기 때문에 예제 코드에서와 같이 FormatterRegistry에 Converter를 등록할 수 있다.

Spring Boot - WebConversionService
Spring Boot를 사용하는 웹 어플리케이션의 경우에는 DefaultFormattingConversionService를 상속하여 만든 WebConversionService를 빈으로 등록해줌