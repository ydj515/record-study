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


[이미지 출처]  
https://ehclub.co.kr/3446  
https://speakerdeck.com/nerogit/django-vs-flask-ggabobsida?slide=37  
https://brownbears.tistory.com/63  
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms  
https://cozy-ho.github.io/flask/2017/10/19/flask-day04.html  
