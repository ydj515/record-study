# Garbage Collector

## JVM
- JAVA Virtual Machine
- 자바 애플리케이션을 클래스 로더를 통해 읽어 들여 자바 API와 함께 실행하는 것
- JAVA와 OS사이에서 중개자 역할을 수행하여 운영체제에 독립적인 플랫폼을 갖게 해줌
- 프로그램의 메모리 관리를 알아서 해줌
- C프로그램 같은 경우 에는 직접 메모리할당을 해주고 해지해줘야하지만 JAVA에서는 JVM이 자동으로 Memory 관리를 해줌

### Java Visual VM
- **C:\Program Files\Java\jdk1.8.0_181\bin** 경로에 jvisualvm.exe를 실행
- tools > plugins 탭에서 visual gc install  
![visual gc](https://user-images.githubusercontent.com/32935365/85432410-e85bd400-b5bd-11ea-9be0-4e3b3b2fbd21.PNG)
- 아래와 같이 확인 가능  
![visual gc2](https://user-images.githubusercontent.com/32935365/85432524-0c1f1a00-b5be-11ea-89e6-46ea30f00715.PNG)  
- JVM 옵션  
![option](https://user-images.githubusercontent.com/32935365/85567670-07b13a80-b66c-11ea-8fe6-595f50a37381.PNG)  

### linux 모니터링 명령
```
$ jstat -gcutil [pid] [몇초마다 반복해서 찍을 지]
$ jstat -gcutil 1747 1s
```  
![jsat](https://user-images.githubusercontent.com/32935365/85569752-c6ba2580-b66d-11ea-8240-d21e58a1e072.png)
- E : eden space
- O : Old space
- YGC : Number of young generation GC Events
- YGCT : Young generation garbage collection time
- **FGC** : Full Garbage Collector Time
- **FGCT** : Full Garbage Collection Time
- GCT : Garbage Collection Time

## Garbage Collector  
![jvm](https://user-images.githubusercontent.com/32935365/85567322-bacd6400-b66b-11ea-8bb4-742007159047.PNG)  

### 종류
- Minor GC: Young 영역에서 발생하는 GC

- Major GC: Old 영역이나 Perm 영역에서 발생하는 GC

### 메모리 지정
- Full GC가 일어 나면 하나의 서버에 여러개의 서버가 떠있다면 gc하는동안 다른 서버에 영향이 간다.
- 빈번히 일어나지 않게 조정하는 것이 중요ㄴ
- **메모리 할당량을 늘리면 GC 발생 횟수는 감소하지만, GC 수행 시간은 길어진다.**
- **메모리 할당량을 줄이면 GC 발생 횟수는 증가하지만, GC 수행 시간은 짧아진다.**



[출처]  
https://12bme.tistory.com/57  
https://d2.naver.com/helloworld/37111  