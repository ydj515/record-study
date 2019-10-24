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
curl http://본인IP:8080/
```

- 아래와 같이 뜨면 성공한거!  
![22](https://user-images.githubusercontent.com/32935365/67461693-e92c1700-f678-11e9-8501-6c166adc8018.PNG)




## Elasticsearch
https://victorydntmd.tistory.com/308

## python 연동
http://jason-heo.github.io/elasticsearch/2016/07/16/elasticsearch-with-python.html

[출처]  
http://mixedcode.com/Article/Index?aidx=1113