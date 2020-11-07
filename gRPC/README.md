# gRPC

## gRPC란?
- google에서 개발한 RPC(Remote Procedure Call) 시스템
- HTTP 2.0, TCP/IP protocol 사용
- IDL중에서 속도가 빠르고, 파일 크기가 작음
- SSL/TLS를 사용하여 서버를 인증하고, **client 와 server 간에 교환되는 모든 데이터를 암호화**함
- gRPC에서 클라이언트 응용 프로그램을 서버에서 함수를 바로 호출 할 수 있어 분산 **MSA(Micro Service Architecture)**를 쉽게 구현 할 수 있음
- 서버 측에서는 서버 인터페이스를 구현하고 gRPC 서버를 실행하여 클라이언트 호출을 처리
- **gRPC를 사용하면 service를 .proto 파일로 한 번 정의하고, gRPC 지원 언어로 클라이언트와 서버를 만들 수 있으며, 이는 다양한 환경에서 실행될 수 있음. 다른 언어와 다른 환경 간의 통신을 gRPC를 통해 처리. 효율적인 직렬화, 간단한 IDL인 protocol buffer를 사용해 성능적 이점을 얻을 수 있음**
![gRPC](https://user-images.githubusercontent.com/32935365/98444497-68419f80-2155-11eb-8475-5acfc9a9a78b.PNG)


## IDL
- 프로토콜 : 서버와 클라이언트가 정보를 주고 받는 규칙
- IDL : 정보를 저장하는 규칙
- XML, json, proto(Protocol buffers)

### XML
- HTML처럼 데이터를 보여주는 것이 목적이 아닌, 데이터를 저장하고 전달할 목적으로 만들어짐
- HTTP + XML 조합
- 예시
```xml
<items>
    <item>
        <fstvlNm>블루거제페스티벌</fstvlNm>
        <opar>장승포 일원</opar>
        <fstvlStartDate>2019-07-31</fstvlStartDate>
        <fstvlEndDate>2019-08-02</fstvlEndDate>
        <fstvlCo>우수 예술인 발굴과 지역 문화예술의 저변 확대를 위해 개최</fstvlCo>
        <mnnst>거제문화예술회관</mnnst>
        <auspcInstt>거제문화예술회관</auspcInstt>
        <phoneNumber>055-680-1000</phoneNumber>
        <rdnmadr>경상남도 거제시 장승로 145</rdnmadr>
        <latitude>34.8671782556</latitude>
        <longitude>128.7233591943</longitude>
        <referenceDate>2020-02-13</referenceDate>
        <insttCode>5370000</insttCode>
    </item>
    <item>
        ...
    </item>
</items>
```

### json
- XML이 가진 읽기 불편하고 복잡하고 느린 속도 문제를 해결
- key-value 구조
- HTTP + RESTful API + JSON 조합
- 예시
```json
"body" :{
    "items":[
        {
            "fstvlNm":"블루거제페스티벌",
            "opar":"장승포 일원",
            "fstvlStartDate":"2019-07-31",
            "fstvlEndDate":"2019-08-02",
            "fstvlCo":"우수 예술인 발굴과 지역 문화예술의 저변 확대를 위해 개최",
            "mnnst":"거제문화예술회관",
            "auspcInstt":"거제문화예술회관",
            "phoneNumber":"055-680-1000",
            "rdnmadr":"경상남도 거제시 장승로 145",
            "latitude":"34.8671782556",
            "longitude":"128.7233591943",
            "referenceDate":"2020-02-13",
            "insttCode":"5370000"
        },
        {
            ...
        }
    ]
}
```

### (proto) Protocol buffers
- 데이터를 직렬화(serialization)하기 위한 프로토콜
- XML 스키마처럼 .proto 파일에 protocol buffer 메세지 타입을 정의
- 파일크기가 작고 속도도 빠름
- byte stream 형식이라 json 처럼 따로 parsing 해줄 필요가 없음
- 예시
``` proto
// syntax가 없으면 자동으로 proto2로 인식됨
syntax = "proto3";

package greetor;

option java_package = "com.ydj515.greetor";
option java_outer_class_name = "GreetorProtos";
option java_multiple_files = true;

// Declaration for rpc service
servbice Greetor {
    rpc greetPerson(GreetorRequest) returns (GreetorResponse);
}

// message4 is a small logical record of information
message GreetorRequest {
    string name = 1;
}

message GreetorResponse {
    string greetins = 1;
}
```

[참고]  
https://grpc.io/  