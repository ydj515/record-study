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


[출처]  
https://jeong-pro.tistory.com/84  
https://goddaehee.tistory.com/169  