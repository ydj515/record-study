# AWS
![11](https://user-images.githubusercontent.com/32935365/65868658-a77aba00-e3b3-11e9-985d-55c2599ec982.PNG)  

## 용어정리
https://github.com/ydj515/record-study/tree/master/AWS/Term

## AWS 시작하기_centos 7
### 1. http://aws.amazone.com 사이트 접속
### 2. 회원가입
### 3. 세팅  
- 우측 상단에 지역을 서울로 바꾼다.  
![1우측 상단](https://user-images.githubusercontent.com/32935365/66216797-184a0b00-e701-11e9-8b91-29d1898abc7c.PNG)  
- ECT 인스턴스 실행  
![2 ec2를 사용하여 가상머신 시작](https://user-images.githubusercontent.com/32935365/66216815-1f711900-e701-11e9-937c-1636743fabe0.PNG)  
![3 select centos](https://user-images.githubusercontent.com/32935365/66216831-2730bd80-e701-11e9-914c-639a74606a26.PNG)  
![4](https://user-images.githubusercontent.com/32935365/66216847-2ef06200-e701-11e9-8237-f3bfed2e3859.PNG)  
![5](https://user-images.githubusercontent.com/32935365/66216864-357ed980-e701-11e9-983d-139d24a31189.PNG)  

## JAVA 설치_ 1.8
### 1. java 설치
```
sudo yum install -y java-1.8.0-openjdk-devel.x86_64
java -version
sudo /usr/sbin/alternatives --config java
```


### 2. Path 등록
```
sudo su
echo $JAVA_HOME
javac -version
which javac
readlink -f /bin/javac
vi /etc/profile
```
![1](https://user-images.githubusercontent.com/32935365/67461161-aae22800-f677-11e9-9757-7503eb7a3f3c.PNG)

- 아래와 같이 /etc/profile 맨 밑에 추가한다.
![2](https://user-images.githubusercontent.com/32935365/67461569-9a7e7d00-f678-11e9-9972-86cea4570f23.PNG)

- 환경설정 적용
```
source /etc/profile
exit
```


## tomcat 설치_tomcat 7
### 1. tomcat 설치
```
sudo su
sudo yum list tomcat*
sudo yum install tomcat*
sudo yum list | grep tomcat
```
![tomcat1](https://user-images.githubusercontent.com/32935365/67461654-c6016780-f678-11e9-9205-9fd7fd89113e.PNG)

### 2. tomcat 설정
```
systemctl emable tomcat
systemctl start tomcat
curl http://{AWS_public_IP}:8080/
```

- 아래와 같이 뜨면 성공한거!  
![22](https://user-images.githubusercontent.com/32935365/67461693-e92c1700-f678-11e9-8501-6c166adc8018.PNG)


## FileZilla 연동
### 1. FileZilla 사이트 접속
- <a href="https://www.acmicpc.net/category/detail/1897">사이트 접속</a>
- 사이트에 접속해서 client로 다운

### 2. 환경설정
- [편집]-[설정]-[연결-SFTP]-[파일추가]-[PPK파일 추가]  
![1](https://user-images.githubusercontent.com/32935365/67474335-3d41f600-f68f-11e9-8ab4-d01bd28d3090.PNG)

- [파일]-[사이트관리자]-[새사이트]-[확인]  
![2](https://user-images.githubusercontent.com/32935365/67474372-4df26c00-f68f-11e9-8e3d-703265e6e631.PNG)

### 3. 연결
- 연결 버튼을 누르면 연결이 된 모습을 볼 수 있음  
![3](https://user-images.githubusercontent.com/32935365/67474406-5d71b500-f68f-11e9-9181-98857ce46e62.PNG)


## war파일 넣기
### 1. war파일 이동
```
sudo mv Test.war /user/share/tomcat/webapps/
```

### 2. project hosting
```
sudo systemctl restart tomcat
```

### 3. 접속
```
http://{AWS_public_IP}/{프로젝트명}/
```


## Python 3.6 설치
### 1. Repository를 yum에 추가
```
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
```

### 2.라이브러리 설치
```
yum search python3
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
```

### 3. 버전 확인
```
python -V
python3.6 -V
```

### 4. Alias 수정
```
which python3.6
ls -l /bin/python*
```  
![111](https://user-images.githubusercontent.com/32935365/67475930-07524100-f692-11e9-85f6-569e8e5e596b.PNG)

- 밑의 4줄을 실행하여 alias를 수정
```
sudo unlink /bin/python
sudo ln -s /bin/python3.6 /bin/python3
sudo ln -s /bin/python3.6 /bin/python
sudo ln -s /bin/pip3.6 /bin/pip
```  
![222](https://user-images.githubusercontent.com/32935365/67476195-7cbe1180-f692-11e9-97b0-db785d159070.PNG)


- python3 적용 확인 => python 3.6.x로 나오면 정상으로 설치 및 alias 수정
```
python -V
```  
![333](https://user-images.githubusercontent.com/32935365/67476280-ae36dd00-f692-11e9-9dbe-d12aa83c4279.PNG)


## Elasticsearch 6.6.2
- **java를 선행**으로 설치해주어야한다!!

### 1. yum으로 설치
- repo 파일을 생성해야 yum으로 설치 가능
```
sudo su
vi /etc/yum.repos.d/elasticsearch.repo
```

- 파일 내용
```
[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

- install
```
yum install -y elasticsearch
```

### 2. 서비스 등록
```
systemctl enable elasticsearch
systemctl start elasticsearch
curl -X GET 'localhost:9200'
```
![111](https://user-images.githubusercontent.com/32935365/68369764-6e85f000-017e-11ea-8598-251331b96020.PNG)  


### 3. Directory Description
- **/usr/share/elasticsearch** : 홈디렉토리
    - **bin** : 실행 파일 디렉토리
    - **plugins** : 플러그인
- **/etc/elasticsearch** : 설정 파일 디렉토리
    - **elasticsearch.yml** : 주 설정 파일
    - **jvm.options** : java 설정 파일
    - **log4j2.properties** : 로그 설정 파일
- **/var/lib/elasticsearch** : 데이터 저장 디렉토리
- **/var/log/elasticsearch** : 로그 저장 디렉토리


### 4. python ES API install
- python import 확인
```
python
>>> import elasticsearch
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named elasticsearch
>>> exit()
```

- pip install
```
pip install elasticsearch
```

- 만약 권한이 없다거나 permission deny가 나오면 다음과 같이 --user 옵션을 넣어준다.
```
pip install --user elasticsearch
```

### 5. python3 실행 오류
![1 yum 오류](https://user-images.githubusercontent.com/32935365/68369695-49917d00-017e-11ea-93b9-281723961dbe.PNG)  

- python237에서 python3.6으로 수정하면서 오류가 발생하면 아래와 같이 조치한다.
    - **1. /usr/bin/yum 파일 수정**
    ```
    vi /usr/bin/yum 
    ```
    - 맨 윗라인에 #!/usr/bin/python을 #!/usr/bin/python2.7로 수정

    - **2. /usr/libexec/urlgrabber-ext-down 파일 수정**
    ```
    vi /usr/libexec/urlgrabber-ext-down
    ```
    - 맨 윗라인에 #!/usr/bin/python을 #!/usr/bin/python2.7로 수정
 
### 간단도르
- index -> db 이름
- doc_type -> type이름
- body -> 내용
```python3
es_client.index(index='test_index', doc_type=folder, body=r)

```

## Elasticsearch와 python 연동
https://blog.nerdfactory.ai/2019/04/29/django-elasticsearch-restframework.html  
https://victorydntmd.tistory.com/308  
https://github.com/elastic/elasticsearch-py  
http://jason-heo.github.io/elasticsearch/2016/07/16/elasticsearch-with-python.html  
https://blog.nerdfactory.ai/2019/04/29/django-elasticsearch-restframework.html  
https://victorydntmd.tistory.com/310  
https://github.com/wikibook/elasticsearch  



[출처]  
http://mixedcode.com/Article/Index?aidx=1113