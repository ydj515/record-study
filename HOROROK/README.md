# 이런거 저런거

## 웹서버와 WAS
### 웹 서버
- 클라이언트가 서버에 페이지 요청을 하면 요청을 받아 정적 컨텐츠(html, csss)를 제공하는 서버
- 클라이언트에서 요청이 올 때 가장 앞에서 요청에 대한 처리
- 동적 컨텐츠에 대한 요청이면 WAS에게 클라이턴트의 요청을 전달
- ex) Apache, nginx

### WAS
- 동적 컨텐츠를 제공하기 위해 만들어진 애플리케이션 서버(DB 조회, 로직 처리가 필요한 컨텐츠)
- JSP, Servlet
- 컨테이너, 서블릿 컨테이너라고도 함
- 웹서버로부터 요청이 오면 컨테이너가 받아서 처리
- 컨테이너는 web.xml을 참조하여 해당 서블릿에 대한 쓰레드 생성하고 httpServletRequest와 httpServletResponse 객체를 생성하여 전달
- 컨테이너는 서블릿을 호출
- 호출된 서블릿의 작업을 담당하게 된 쓰레드(위의 web.xml을 참조하여 해당 서블릿에 대해 생성된 스레드)는 doPost()또는 doGet()을 호출한
- 호출된 doPost(), doGet() 메소드는 생성된 동적 페이지를 Response객체에 담아 컨테이너에 전달
- 컨테이너는 전달받은 Response객체를 HTTPResponse형태로 바꿔 웹서버에 전달하고 생성되었던 쓰레드를 종료하고 httpServletRequest, httpServletResponse 객체를 소멸시킴
- ex) Tomcat, Jeus, JBoss

### 비고
- WAS는 정적,동적 처리 둘다 가능하지만 정적처리를 WAS가 하게되면 부하가 많이 걸려서 좋지 않음
- 톰캣(WAS)은 아파치(웹서버)의 기능(웹서비스데몬, Httpd)를 포함
- 웹서버와 WAS를 따로 두지 않는 이유는 톰캣 5.5 이상부터는 httpd의 native모듈을 사용해서 정적파일을 처리하는 기능을 제공하는데 이것이 순수 아파치 Httpd만 사용하는 것과 비교해서 성능이 전혀 떨어지지 않기 때문
- 그럼에도 톰캣앞에 아파치를 두는 이유는 하나의 서버에서 php애플리케이션과 java애플리케이션을 함께 사용하거나, httpd 서버를 간단한 로드밸런싱을 위해서 사용해야 할 때 필요하기 때문

## Request Header
### Date
- HTTP 메시지가 만들어진 시각입니다. 자동으로 만들어짐
- ex) Date: Sun, 13 Jan 2020 11:28:13 GMT

### Connection
- 일반적으로 HTTP/1.1을 사용하며 Connection은 기본적으로 keep-alive
- ex) Connection: keep-alive

### Content-Length
- 요청과 응답 메시지의 본문 크기를 바이트 단위로 표시
- 메시지 크기에 따라 자동으로 만들어짐
- ex) Content-Length: 88052

### Content-Language
- 유저 언어

### Content-Encoding
- 응답 컨텐츠를 br, gzip, deflate 등의 알고리즘으로 압축해서 보내면, 브라우저가 알아서 해제해서 사용
- 요청이나 응답 전송 속도도 빨라지고, 데이터 소모량도 줄어들기 때문에 사용
- ex) Content-Encoding: gzip, deflate

### Host
- 서버의 도메인 네임
- Host 헤더는 반드시 하나가 존재해야 한다.
- ex) host: www.akmall.com

### User-Agent
- 현재 사용자가 어떤 클라이언트(운영체제, 앱, 브라우저 등)를 통해 요청을 보냈는지 알 수 있음
- ex) User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36

### Accept
- 클라이언트가 허용할 수 있는 파일 형식(MIME TYPE)
- 콤마로 여러 타입을 동시에 적어줄 수도 있고, *(와일드카드)로 텍스트면 ok라고 요청할 수 있음
- ex1) Accept: text/html (HTML 형식인 응답을 처리하겠다)
- ex2) Accept: image/png, image/gif
- ex3) Accept: text/*

### Cookie
- 웹서버가 클라이언트에 쿠키를 저장해 놓았다면 해당 쿠키의 정보를 key-value 쌍으로 웹서버에 전송

### Origin
- POST같은 요청을 보낼 때, 요청이 어느 주소에서 시작되었는지를 나타내는데 이때 보낸 주소와 받는 주소가 다르면 CORS 문제가 발생하기도 함

### If-Modified-Since
- 페이지가 수정되었으면 최신 버전 페이지 요청을 위한 필드
- 만일 요청한 파일이 이 필드에 지정된 시간 이후로 변경되지 않았다면, 서버로부터 데이터를 전송받지 않음

### Authorization
- 인증 토큰을 서버로 보낼 때 사용하는 헤더.
- API 요청같은 것을 할 때 토큰이 없으면 거절당하기 때문에 이 때, Authorization을 사용
- JWT(Json Web Token) 을 사용한 인증에서 주로 사용
- ex) Authorization: Bearer xxx.xxx.xxx

### Request 예시
```
accept: text/html, */*; q=0.01
accept-encoding: gzip, deflate, br
accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
content-type: application/x-www-form-urlencoded; charset=UTF-8
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
x-requested-with: XMLHttpRequest
Host: www.akmall.com
Content-Length: 91
```

## 동기 비동기
### 동기
- 요청과 그 결과가 동시에 일어남
- 함수의 결과를 호출한 쪽에서 처리

### 비동기
- 함수를 호출한 쪽에서 콜백함수를 통해 결과 처리

### 스레드 기반 동기 vs 이벤트 기반 비동기
- 스레드 기반 동기 방식은 여러개의 스레드를 만들어 동시에 일을 처리하지만 일이 많아질 수록 스레드를 더 많이 나눠야하므로 메모리 사용량이 증가함
- 이벤트 기반 동기 방식은 스레드는 단 하나지만 각 함수를 호출하고 이벤트가 발생하는 순간 콜백을 받아서 메모리 사용량에 변화가 거의 없다.
- 대표적인 이벤트 기반 비동기 방식인 node는 이런 장점을 가지고 있지만, 단점으로는 프로그램이 진행에 문제가 발생하면 프로그램 전체가 영향을 받음.

## 블록킹 논블록킹
### 블록킹
- 수행결과가 끝날 때까지 제어 소유

### 논블록킹
- 자신이 호출되었을 때 제어권을 자신을 호출한 쪽으로 넘김

## SQL INSERT TIME
### now() vs. sysdate()
- **now()** 는 쿼리문이 실행되는 시간의 값을 저장하고, **sysdate()**는 해당 함수가 호출되는 순간의 시간을 저장한다. 
- 단, 여기서 데이터 타입을 timestamp로 해주어야 한다. datetime은 에러를 발생시킴
- ex
```SQL
select NOW(), SLEEP(2), NOW(); -- 2020-08-02 18:14:15 / 0 / 2020-08-02 18:14:15
select SYSDATE(), SLEEP(2), SYSDATE(); -- 2020-08-02 18:14:15 / 0 / 2020-08-02 18:14:17
```

## OAuth
- 인증을 위한 오픈 스탠더드 프로토콜
- 사용자가 Facebook, kakao, naver등과 같은 인터넷 서비스의 기능을 다른 어플리케이션에서도 사용할 수 있게한다.
- 위의 사이트들에 대해 사용자 아이디와 암호를 대신 인증해달라고 요청하고 사용자 인증을 받는 형식
- 간단히 말해 소셜 로그인등 과 같은 것
- 각 제공 사이트 마다 요구하는 객체(Response 형식)이 다름
![123](https://user-images.githubusercontent.com/32935365/89119988-55cc2000-d4ed-11ea-8f85-51bac98d2bcc.PNG)

### 인증 종류
#### Authorization Code Grant
- 서버 사이드 코드로 인증하는 방식
- 권한서버가 클라이언트와 리소스 서버 간의 중재 역할
- access token을 바로 클라이언트로 전달하지 않아 잠재적 유출 방지
- 로그인시에 페이지 **URL**에 **response_type=code** 라고 넘김

#### Implicit Grant
- token과 scope에 대한 스펙 등은 다르지만 OAuth 1.0a과 가장 비슷한 인증방식
- Public Client인 브라우저 기반의 어플리케이션(Javascript application)이나 모바일 어플리케이션에서 이 방식을 사용하면 됨
- OAuth 2.0에서 가장 많이 사용되는 방식
- 권한코드 없이 바로 발급되서 보안에 취약
- 주로 Read only인 서비스에 사용
- 로그인시에 페이지 **URL**에 **response_type=token** 라고 넘김

#### Password Credentials Grant
- 클라이언트에 ID/PW를 저장해 놓고 ID/PW로 직접 access token을 받아오는 방식
- 클라이언트를 믿을 수 없을 때에는 사용하기에 위험
- 로그인시에 API에 **POST**로 **grant_type=password** 라고 넘김

#### Client Credentials Grant
- 어플리케이션이 Confidential Client일 때 id와 secret을 가지고 인증하는 방식
- 로그인시에 API에 **POST**로 **grant_type=client_credentials** 라고 넘김

### Token
### Access Token
- 위의 4가지 권한 요청 방식 모두, 요청 절차를 정상적으로 마치면 클라이언트에게 Access Token이 발급됨
- access token은 보호된 리소스에 접근할 때 권한 확인용으로 사용
- 문자열 형태이며 클라이언트에 발급된 권한을 대신함
- 계정 아이디와 비밀번호 등 계정 인증에 필요한 형태들을 이 access token 하나로 표현함으로써, 리소스 서버는 여러 가지 인증 방식에 각각 대응 하지 않아도 권한을 확인 할 수 있게 됨

### Refresh Token
- 한번 발급받은 access token 은 사용할 수 있는 시간이 제한되어 있음
- 사용하고 있던 access token 이 유효기간로 만료되면, 새로운 액세스 토큰을 얻어야 하는데 그때 이 refresh token을 사용
- 권한 서버가 access token 을 발급해주는 시점에 refresh token 도 함께 발급하여 클라이언트에게 알려주기 때문에, 전용 발급 절차 없이 refresh token을 미리 가지고 있을 수 있음
- 문자열 형태. 단 권한 서버에서만 활용되며 리소스 서버에는 전송되지 않음

### 토큰의 갱신 과정
1. 클라이언트가 권한 증서를 가지고 권한서버에 access token 을 요청
2. 권한 서버는 access token과 refresh token 을 함께 클라이언트에 알려줌
3. 클라이언트는 access token을 사용하여 리소스 서버에 각종 필요한 리소스들을 요청하는 과정을 반복
4. 3의 과정을 반복하다가 일정한 시간이 흐른 후 access token이 만료되면, 리소스 서버는 이후 요청들에 대해 정상 결과 대신 오류를 응답
5. 오류 등으로 액세스 토큰이 만료됨을 통보 받은 클라이언트는, 전에 받아 두었던 refresh token을 권한 서버에 보내어 새로운 access token을 요청
6. 갱신 요청을 받은 권한 서버는 refresh token 의 유효성을 검증한 후, 문제가 없다면 새로운 액세스 토큰을 발급해줌
7. 6번에서 옵션에 따라 refresh token 도 새롭게 발급 될 수 있음

[출처]  
https://jeong-pro.tistory.com/84  
https://goddaehee.tistory.com/169  

https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#before-you-begin  
https://developers.naver.com/docs/common/openapiguide/apilist.md  
https://developers.payco.com/guide/development/start  
https://showerbugs.github.io/2017-11-16/OAuth-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C  