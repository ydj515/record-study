# Kotlin Study

## What is Kotlin?
- 자바 가상머신에 돌아가는 **JVM 언어의 하나**
- 2017년 구글 I/O에서 코틀린은 **공식언어로 지정**

## Why Kotlin?
- **More simpler** than JAVA  
  -코드의 간결성은 가독성을 높힌다.
  ```java
  class Person {
    private String name;
    private int age;
    private String Email;
    private int grade;
    
    public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setEmail(String Email) {
        this.Email = Email;
    }
    public void setGrade(int grade) {
        this.grade = grade;
    }
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public String getEmail(){
        return Email;
    }
    public int getGrade(){
        return grade;
    }
  }
  ```
  위의 java 코드를 코틀린으로 변환하면 훨씬 간결해진다.
  ```kotlin
  class Person {
    var name: String=""
    var age: Int=0
    var Email: String=""
    var grade: Int=0
  }
  ```
- **Effectively handle Nullpointerexception**
-String에 NULL을 집어 넣을 수 없으므로 Nullpointerexception을 Java보다 디버깅이 용이
- 상속 받지 않고도 클래스 확장이 가능
  ```kotlin
  fun Context.showToast(text: CharSequence, duration: Int = Toast.LENGTH_SHORT) { // Toast메시지 확장
     Toast.makeText(this, text, duration).show()
  }
  
  fun Context.startCallActivity(myName: String) { // startActivity 확장
     val intent = Intent(Intent.ACTION_DIAL)
     val uri = "tel:$myName"
     intent.data = Uri.parse(uri)
     startActivity(intent)
  }
  
  showToast("호로록")
  startCallActivity("유동진이야")
  ```
- 객체지향 언어지만 함수형 언어의 장점인 **람다식 표현을 차용**  
  사용되지 않는 view마저도 없애버릴 수 있음 => 코드가 간결해짐
  - **Java**
   ```java
   button.setOnClickListener(new View.OnClickListener() {
       @Override public void onClick(View view) {
       // TODO
       }
   });

   ```
  - **java의 람다식 표현**
   ```java
   button.setOnClickListener(view -> {
       // TODO
   });
   ```
  - **Kotlin**
   ```kotlin
   button.setOnClickListener {
       // TODO
   }
   ```
- **사용방식**  
![111](https://user-images.githubusercontent.com/32935365/62598179-7a65da00-b923-11e9-8069-a723c185ba32.png)
## Android에서 Kotlin 사용

### Mainactivity

- **Java**  
![java](https://user-images.githubusercontent.com/32935365/62598107-35da3e80-b923-11e9-8f4c-b28bd8044933.PNG)
- **Kotlin**  
![kotlin](https://user-images.githubusercontent.com/32935365/62598116-3d014c80-b923-11e9-879a-8d503076b64b.PNG)

[이미지 출처]  
https://medium.com/androiddevelopers/kotlin-standard-functions-cheat-sheet-27f032dd4326
