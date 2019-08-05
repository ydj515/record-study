# 안드로이드 앱에서 Youtube 연동

- **해당 홈페이지는 youtube에 관련된 api가 정리된 document**  
https://developers.google.com/youtube/android/player/?hl=ko


## Youtube API 연동 환경 설정
### 1. Youtube API 다운
- 위의 <a href="https://developers.google.com/youtube/android/player/?hl=ko">URL</a>에 들어간 다음 overview에 download로 들어가기
- Youtube API 다운 
- YouTubeAndroidPlayerApi-1.2.2.zip 다운로드

### 2. API key 생성
- https://console.developers.google.com/apis/credentials?hl=ko 사이트에 들어가서 프로젝트 생성 후 사용자 인증정보 만들기
- 아래와 같이 api키를 만들면 성공
![2](https://user-images.githubusercontent.com/32935365/62461747-8c7b3780-b7c0-11e9-82f6-4eb0ac3f3570.PNG)

### 3. Dependency 추가
- 압축 해제 후 File - Project Structure - Dependencies에서 +를 누르고 Jar Dependecy에 압축을 푼 폴더에 libs 밑의 YouTubeAndroidPlayerApi.jar의 경로를 추가후 apply.
![1](https://user-images.githubusercontent.com/32935365/62464897-b2a4d580-b7c8-11e9-8f9e-32cd4fe63be0.PNG)  
위와 같이 나오면 ok를 누른다.

### 4. Android Studio에서 api key값 관리
- 안드로이드 스튜디오에서 res - values - **string.xml**에 이 키값을 넣고 관리하는 것이 편하므로  
string.xml에 넣어서 사용 **(youtube_key라는 변수에 api 키값 넣음)**
![3](https://user-images.githubusercontent.com/32935365/62461908-0d3a3380-b7c1-11e9-9ab5-5a9342527e03.PNG)

### 5. Permission 추가
- **AndroidManifest.xml** 에 아래와 같이 **internet permission추가**  
```
<uses-permission android:name="android.permission.INTERNET" />
```
![4](https://user-images.githubusercontent.com/32935365/62462194-bbde7400-b7c1-11e9-9f36-17878d21d8b0.PNG)

