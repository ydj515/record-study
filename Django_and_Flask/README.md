# Django vs. Flask

## Django
- https://github.com/ydj515/helloDJango
### 특징
- 파이썬 기반으로 빠른 코드 수정 및 짧은 코드길이 => 개발시간 단축
- **인증, 관리**  
 -크로스 사이트 스크립팅, 사이트 간 요청 위조 및 클릭 재킹과 와 같이 거의 대부분의 사이트에서 사용하는 기능들이 기본 모듈로 제공
- **MVT(Model, View Template)**  
 -MVC(Model, View, Controller) 패턴 기반의 MVT: View가 Logic담당, Template가 View 담당  
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
- **Python 3.6 버전부터 지원**


## 차이점

### Django ORM vs. SqlAlchemy  
![1](https://user-images.githubusercontent.com/32935365/62513107-a61a8e80-b855-11e9-94ac-af9321332842.PNG)
#### Django ORM
- **Select**  
  - **Get**  
  -**모델 타입으로 반환**  
  -get()안에 조건 제시 가능(sql where절)  
  -get()은 단일행이므로 메소드들을 연결해서 사용 불가
  ```python
   from polls.models import Question # from 앱이름.models import 모델1, 모델2 ...
   key = Question.objects.get(pk=) # Query set 타입으로 반환
   key.name
   ```
  - **All**  
  -전체 자료를 불러온다.  
  -**Query set 타입으로 반환**  
  -dictionary를 사용하는 것과 동일하게 사용 가능
   ```python
   from polls.models import Question ## from 앱이름.models import 모델1, 모델2 ...
   key = Question.objects.all() ## Query set 타입으로 반환
   key[0]['name']
   ```
   - **Filter**  
   -조건을 걸어 여러행 출력  
   -**Query set 타입으로 반환**  
   -objects.all().filter()와 동일한 기능
   ```python
   value = key = Question.objects.filter(name='yoo')
   key[0]['name']
   ```
   
   - **조건 키워즈**  
   -get과 filter에 각 조건을 걸 수 있으며 **and로 결합**  
   ![condition](https://user-images.githubusercontent.com/32935365/62521152-0ddad480-b86a-11e9-8e37-4c953f09a434.PNG)
   
   - **Orderr by**  
   -기본 정렬은 오름차순  
   -내림차순은 '-'를 붙힘
   ```python
   value = Question.objects.order_by('pk') # 오름차순 정렬
   value = Question.objects.order_by('-pk') # 내림차순 정렬
   ```
   
   - **Value**  
   -**sql select**와 같은 기능  
   -**Querey set타입으로 반환**
   ```python
   value = Questino.objects.values('pk') # query set 타입으로 pk만 출력
   ```
   
   - **Aggregate**  
   -**sql max, min, count**와 같이 다중행을 단일 행으로 출력    
   -뒤에 다른 메소드를 붙혀 사용할수 없음
   ```python
   from django.db.models import Max
   value = model.objects.aggregate(temp_name=Max('pk')) # temp_name은 사용자가 임의로 정할 수 있음
   value['temp_name']
   ```
   ```python
   from django.db.models import Max
   from django.db.models.functions import Coalesce
   value = model.objects.aggregate(temp_name=Coalesce(Max('pk'), 10000)) # temp_name은 사용자가 임의로 정할 수 있음
   value['temp_name']
   ```
   
- **Insert**  
   - **save()**  
   -**save()를 하지 않을 경우 메모리 상에 저장할 데이터의 Instance만 존재하고 테이블에 저장되지 않음을 유의!**
   ```python
   data = Question(name='yoo')
   data.save() # Question이라는 테이블에 'lee'라는 데이터 insert
   ```
   
   - **objects.create()**  
   -**save()를 할 필요 없이 바로 저장**
   ```python
   data = Question.objects.create(name='yoo')
   ```
   
   - **Rest framework 사용**  
   -**save()를 할 필요 없이 바로 저장**  
   -따로 rest framework 설치 해야함  
   -**json_format_data는 json(dict)형식의 데이터**  
   -**partial은 테이블 내의 일부만 insert할 때 사용**  
   -**save()를 하기전에 validation을 먼저 확인**
   ```python
   serializer = CommonTax1InSerializer(data=json_format_data, partial=True)
   
   if serializer.is_valid():
      serializer.save()
   ```
   
- **Update**  
   - **1개의 데이터 update**  
   ```python
   data = Question.objects.get(pk=pk)
   data.name = 'yoo'
   data.save() # save()를 해야 저장
   ```
   ```python
   # Rest framework
   pk = Question.objects.get(pk=pk)
   serializer = Question(pk, data=json_data)
   if serializer.is_valid():
      serializer.save()
   ```
   
   - **여러개의 데이터 update**  
   ```python
   Question.objects.filter(name='yoo', age='25').update(**update_dict)
   ```
   ```python
   # Rest framework
   queryset = Question.objects.all()
   serializer = BookSerializer(queryset, many=True)
   if serializer.is_valid():
      serializer.save()
   ```
   
- **Delete**  
   - **1개의 데이터 delete**  
   ```python
   pk = Question.objects.get(pk=pk)
   pk.delete()
   ```
   - **여러개의 데이터 delete**  
   ```python
   Question.objects.filter(name='yoo', age='25').delete()
   ```
   
#### SqlAlchemy
- **설치**
  - **pip install**  
  ```
  $ pip install flask_sqlalchemy
  ```
  - **import**
  ```python
  from flask_sqlahcmey import SQLAlchemy
  ```
- **app객체 설정**  
  -__init__.py에서 설정  
  ```python
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'this is secret' # secret key 추가
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # 
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 

  db = SQLAlchemy(app) # SQLAlchemy객체 생성
  ```
- **config 파일 생성**  
  -config.py에서 설정  
  ```python
  SQLALCHEMY_DATABASE_URI = 'mysql://<mysqluser>:<password>@<mysqlhostname>/<databasename>?charset=utf8'
  ```
- **DB 생성**

```python
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __table_name__ = 'user'
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')
 
  def __init__(self, username, email, password, **kwargs):
      self.username = username
      self.email = email
 
      self.set_password(password)
 
  def __repr__(self):
        return f"<User('{self.id}', '{self.username}', '{self.email}')>"
 
  def set_password(self, password):
    self.password = generate_password_hash(password) # 비밀번호 암호화
    print(self.password)
 
  def check_password(self, password):
    return check_password_hash(self.password, password) # 맞으면 True, 틀리면 False를 return
```  

- **Create**  
```python
from app import app, db, User
db.create_all()
```

- **Update**  
```python
from app import app, db, User, Post
user1 = User(id=1, username='dongjin', email='ydj515@naver.com', password='ehdwls515' )
user2 = User(id=2, username='yoodong', email='ydj515@google.com', password='elwpdl515' )
db.session.add(user1)
db.session.add(user2)
db.session.commit() # commit을 해주어야 db 반영
```

- **Delete**  
```python
```

### Form vs. flask-wtf
#### Form  
- Django에서 form을 처리하는 방식
![form](https://user-images.githubusercontent.com/32935365/62533995-f2c88e80-b882-11e9-86f4-0ea7d4eadccf.PNG)
-
#### flask-wtf
- **설치**
  - **pip install**  
  ```
  $ pip install flask-wtf
  ```
- **문법**  
  - **WTForms HTML Field**  
  ![11](https://user-images.githubusercontent.com/32935365/62620963-997d5f80-b955-11e9-9108-d1c2d0d0122e.PNG)  

  - **WTForms Validator**  
  ![22](https://user-images.githubusercontent.com/32935365/62620994-adc15c80-b955-11e9-9b7f-0023d395f3dd.PNG)
  - **예시**  
-myFlask/app.py
  ```python

  @app.route('/', methods=['GET', 'POST'])
  def index():
    name = None
    form = ProgramForm()

    if form.validate_on_submit() == True:
        name = form.name.data
        form.name.data =''

    return render_template('index.html', form=form, name=name)
  ```
  -myFlask/templates/index.html
  ```jinja
  {% block content %}
    <div class="container">
      <div class="page-header">
        <h1>Input Your Value is : {% if name %} {{ name }} {% else %} None {% endif %} !</h1>

        <form method="POST">
          {{ form.csrf_token }}
          {{ form.name.label }} {{ form.name() }}
          {{ form.submit() }}
        </form>
      </div>
      {{ wtf.quick_form(form) }}
    </div>
   {% endblock %}
  ```
  

### Template Engine vs. Jinja2
#### Template Engine
-Flask의 Jinja2와 흡사
- **예시**
```django
{% if count > 0 %}
    Data Count = {{ count }}
{% else %}
    No Data
{% endif %}
 
{% for item in dataList %}
  <li>{{ item.name }}</li>
{% endfor %}
 
{% csrf_token %}
```  

#### Jinja2
-Django의 Template Engine과 거의 흡사  
-Jinja의 표현방식이 좀 더 python 문법에 가까움
- **설치**
  - **pip install**  
  ```
  $ pip install jinja2
  ```
- **예시**  
-아래와 같이 python과 비슷하다.
```jinja2
{% for item in myItems %}
<li><a href="{{ item.href }}">{{ item.caption }}</a></li>
{% endfor %}
```
-여러 문법의 사용은 https://github.com/ydj515/FlaskWeb 여기에 있다.


### Admin Page vs. flask-admin
#### Admin Page
-
#### flask-admin
-

### Middleware vs. before_request, after_request
#### Middleware
- **Middle ware란?**  
-Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.  
-즉, 장고는 http 요청이 들어오면 미들웨어를 거쳐서 해당 URL 에 등록되어 있는 뷰로 연결해주고, http 응답 역시 미들웨어를 거쳐서 내보낸다.  
-**HTTP Request, HTTP Response에 대한 전처리를 한다.**  
![33](https://user-images.githubusercontent.com/32935365/62621669-75bb1900-b957-11e9-843f-b48f5db5454c.PNG)

- **예시**
 ```python
  import re # 정규식을 위한 
  from rest_framework.status import is_client_error, is_success


   class ResponseFormattingMiddleware:
       
       # Rest Framework 을 위한 전용 커스텀 미들웨어에 대해 response format 을 자동으로 세팅
       
       METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

       def __init__(self, get_response):
           self.get_response = get_response
           self.API_URLS = [
               re.compile(r'^(.*)/api'),
               re.compile(r'^api'),
           ]

       def __call__(self, request):
       
           response = None
           
           if not response:
               response = self.get_response(request)
           if hasattr(self, 'process_response'):
               response = self.process_response(request, response)
               
           return response

       def process_response(self, request, response):
           
           # API_URLS 와 method 가 확인이 되면 response 로 들어온 data 형식에 맞추어
           # response_format 에 넣어준 후 response 반환
           
           path = request.path_info.lstrip('/')
           valid_urls = (url.match(path) for url in self.API_URLS)

           if request.method in self.METHOD and any(valid_urls):
               response_format = {
                   'success': is_success(response.status_code),
                   'result': {},
                   'message': None
               }

               if hasattr(response, 'data') and \
                       getattr(response, 'data') is not None:
                   data = response.data
                   try:
                       response_format['message'] = data.pop('message')
                   except (KeyError, TypeError):
                       response_format.update({
                           'result': data
                       })
                   finally:
                       if is_client_error(response.status_code):
                           response_format['result'] = None
                           response_format['message'] = data
                       else:
                           response_format['result'] = data

                       response.data = response_format
                       response.content = response.render().rendered_content
               else:
                   response.data = response_format
   
           return response
 ```
#### before_request, after_request
-Middle ware와 비슷하게 request의 전처리 후처리를 해주는 역할을 한다.
- **예시**
  ```python
  @app.before_first_request
  def before_first_request(): # request 요청 처음에만
      pass

  @app.before_request
  def before_request():
      # 매 번의 request시 호출
      # app.route()의 경로가 어디든 before_request()는 호출됨
      # 1. filter 역할도 해줄 수 있다는 것임
      # 2. DB connection 열기
      print("before request!!")
      g.str = "한글" # g : application context(모든 유저가 사용 가능)

   @app.after_request
   def after_request():
      # 매번 request가 종료되는 시점
      # response가 끈나고 불림
      # 1. DB connection 닫기
      pass

  @app.teardown_request
  def teardown_request(Exception):
      # after_reqeust 후에 실행
      # 오류처리
      pass

  @app.teardown_appcontext
  def teardown_appcontext(Exception):
      # app context 끝나고 불림
      pass
  ```
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


[이미지 출처]  
https://ehclub.co.kr/3446  
https://speakerdeck.com/nerogit/django-vs-flask-ggabobsida?slide=37  
https://brownbears.tistory.com/63  
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms  
https://cozy-ho.github.io/flask/2017/10/19/flask-day04.html  
https://has3ong.tistory.com/m/443?category=831354  
https://gyukebox.github.io/blog/django-%EC%BB%A4%EC%8A%A4%ED%85%80-%EB%AF%B8%EB%93%A4%EC%9B%A8%EC%96%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0---rest-framework-%EB%A5%BC-%EC%9C%84%ED%95%9C-http-response-formatting/  
