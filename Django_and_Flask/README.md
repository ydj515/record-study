# Django vs. Flask

## Django
- https://github.com/ydj515/helloDJango
### 특징
- 파이썬 기반으로 빠른 코드 수정 및 짧은 코드길이 => 개발시간 단축
- **인증, 관리**  
 크로스 사이트 스크립팅, 사이트 간 요청 위조 및 클릭 재킹과 와 같이 거의 대부분의 사이트에서 사용하는 기능들이 기본 모듈로 제공
- **MVT(Model, View Template)**  
 MVC(Model, View, Controller) 패턴 기반의 MVT: View가 Logic담당, Template가 View 담당  
![1](https://user-images.githubusercontent.com/32935365/62485306-53aa8500-b7f7-11e9-9f50-6a1f41863bce.PNG)
- **ORM(Object-Relational Mapping)** 지원
- Easy URL Parsing
- View를 위한 **template 엔진 제공**
- Easy to DBA
- Huge community는 open source로써의 강점
- 실제 사용 예 : **Instagram**


## Flask
- https://github.com/ydj515/FlaskWeb
### 특징
- **Micro Framework**  
 매우 가볍고 심플한 Framework를 지향
- **높은 자유도**  
 처음부터 주어진 기능이 없기에 내가 원하는 설계 방향대로 framework를 구축해 나갈 수 있다는 장점
- 템플릿 엔진 **Jinja2** 사용

 
- 실제 사용 예 : **Linked-in**


## 차이점

### Django ORM vs. SqlAlchemy
#### Django ORM
-
#### SqlAlchemy
-

### Form vs. flask-wtf
#### Form
-
#### flask-wtf
-

### Template Engine vs. Jinja2
#### Template Engine
-
#### Jinja2
-

### Admin Page vs. flask-admin
#### Admin Page
-
#### flask-admin
-

### Middleware vs. before_request, after_request
#### Middleware
-
#### before_request, after_request
-

### manage.py vs manage.py vs. flask-scripts
#### manage.py
-
#### manage.py vs. flask-scripts
-

### manage.py test vs. unittest or flask-test
#### manage.py test
-
#### before_request, unittest or flask-test
-

### def view(request) vs. flask.request
#### def view(request)
-
#### flask.request
-

### request.user vs. flask.g.user
#### request.user
-
#### flask.g.user
-

### django.contrib.messages vs. flask.flash
#### django.contrib.messages
-
#### flask.flash
-


[출처]  
https://ehclub.co.kr/3446  
https://speakerdeck.com/nerogit/django-vs-flask-ggabobsida?slide=37
