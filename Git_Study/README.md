# Git Study

## Git Install
### Git download
- https://git-scm.com/downloads

### Git start
- Linux / macOS : Terminal 실행
- Windows : Git -> Git Bash 실행

### Git Version Confirm
```
git --version
```
![1 git version](https://user-images.githubusercontent.com/32935365/68192616-ed4f2180-fff4-11e9-887f-7704256faa23.PNG)


## Git start
### 사용자 정보 설정
- 저장소에 코드를 반영할 때 등록될 **사용자 정보 설정**
- 프로젝트마다 다른 사용자 정보를 지정하고 싶다면 **--global**을 빼고 설정
```
git config --global user.name "ydj515"
git config --global user.email ydj515@hanmail.net
```


### 설정 정보 확인
```
git config --list
```
![2 설정 정보 확인](https://user-images.githubusercontent.com/32935365/68192631-f7712000-fff4-11e9-98aa-407fe1c6f85a.PNG)

## Git 저장소 생성
### 기존 디렉토리 사용
- git을 사용할 프로젝트 폴더로 이동 후 명령어 실행
```
git init
```
![git init](https://user-images.githubusercontent.com/32935365/68192722-1cfe2980-fff5-11e9-9716-74e8318c85ad.PNG)

- 아래와 같이 master branch로 바뀌면서 저장소 생성
![git init2](https://user-images.githubusercontent.com/32935365/68192747-24253780-fff5-11e9-834e-718f38761728.PNG)


### clone후 사용
- github.com에 있는 프로젝트를 **clone**
``` 
git clone https://github.com/ydj515/record-study.git
```
![git clone](https://user-images.githubusercontent.com/32935365/68192818-49b24100-fff5-11e9-863e-7fb601f43772.PNG)  
![git clone2](https://user-images.githubusercontent.com/32935365/68192833-50d94f00-fff5-11e9-9716-c041894ca9f8.PNG)


## Commit
### working directory -> stage area
- comment.js 파일을 **add** 한다
``` 
git add comment.js
```
- 현재 working directory에 있는 **모든 파일을 add** 한다
```
git add .
```

### stage area -> working directory
- stage area 에 올린 파일들을 **취소**
```
git reset comment.js
```

### 수정된 파일 되돌리기
- 수정된 **내용은 모두 삭제!**
```
git checkout -- commment.js
```

### repository 확인
- 어떤 파일이 **변경**되었는지, **stage area**에 있는지 확인
```
git status
```
![git status](https://user-images.githubusercontent.com/32935365/68192883-65b5e280-fff5-11e9-8599-6c83d67ae210.PNG)


### 변경 내용 확인
- 어떤 파일의 내용이 변경되었는지 확인
```
git diff
```
![git diff](https://user-images.githubusercontent.com/32935365/68192910-71090e00-fff5-11e9-902b-1a206438e68a.PNG)

### commit (stage area -> repository)
- stage area에 있는 파일을 저장소에 반영
- 따옴표 안에 커밋 메시지 적기
```
git commit -m "initial commit"
```
![git commit](https://user-images.githubusercontent.com/32935365/68192937-8120ed80-fff5-11e9-8d93-a4de515bfad8.PNG)

### commit 내용 변경
```
git commit --amend
```

### 저장소 반영 삭제
- commit 내용 전부 삭제
```
git reset --hard HEAD^
```
![git reset](https://user-images.githubusercontent.com/32935365/68192967-8b42ec00-fff5-11e9-984c-0c4050906462.PNG)

### git log
- log 확인
```
git log
```
![git log](https://user-images.githubusercontent.com/32935365/68192983-93029080-fff5-11e9-8d3e-265cc63b6bd3.PNG)

## Branch create, switch
### branch 생성
```
git branch like_feature
```

### branch 확인
```
git branch
```
![git branch](https://user-images.githubusercontent.com/32935365/68193020-a9105100-fff5-11e9-8541-0e6609c9c468.PNG)

### branch switch
```
git checkout like_feature
```
![git checkout](https://user-images.githubusercontent.com/32935365/68193066-baf1f400-fff5-11e9-8ca8-923ef3cfc786.PNG)

## Merge
- master branch에서 지속적으로 가져와서 충돌나는 부분을 계속 없애주는 것이 중요!!

### like_feature에서 작업 후 master branch로 Merge
```
git checkout master
git merge like_feature
```

### confilct 해결
- git status명령으로 어느 파일에서 충돌이 발생했는지 확인
```
git status
```
![merge git status](https://user-images.githubusercontent.com/32935365/68193126-df4dd080-fff5-11e9-8ffe-da1cb05eb365.PNG)

- conflict난 파일 열어서 내용 확인
![conflict 내용 확인](https://user-images.githubusercontent.com/32935365/68193142-e5dc4800-fff5-11e9-81ad-af919b01f54a.PNG)

- 수정 후 '<<<<<<<', '=======', '>>>>>>>'가 포함된 행 삭제

- 수정 후, add, commit, merge
```
git add comment.js
git commit -m "solve conflict"
git checkout master
git merge like_feature
```
![merge conflict](https://user-images.githubusercontent.com/32935365/68193194-fd1b3580-fff5-11e9-9b9a-afd4b5104dc6.PNG)


## branch 삭제
- merge된 branch는 삭제해도 무방
### merge된 branch 확인
```
git branch --merged
```
![git branch --merged](https://user-images.githubusercontent.com/32935365/68193253-0efcd880-fff6-11e9-9766-4f548e3dce13.PNG)

### branch 삭제
```
git branch -d like_feature
```
![branch delete](https://user-images.githubusercontent.com/32935365/68193262-158b5000-fff6-11e9-8ffe-0a9151aadfb1.PNG)

## 원격 repository
### 원격 repository 확인
```
git remote
```
![git remote](https://user-images.githubusercontent.com/32935365/68195202-cb0bd280-fff9-11e9-99ad-31291c681e6b.PNG)

### 원격 repository 연결
```
git remote add origin https://github.com/ydj515/record-study.git
```

### 원격 repository 보기
```
git remote show origin
```
![git remote show origin](https://user-images.githubusercontent.com/32935365/68195219-d2cb7700-fff9-11e9-88a0-51d3fb3c2a55.PNG)

### 원격 repository 이름 변경(origin -> git_test)
```
git remote rename origin git_test
```
![git remote show origin](https://user-images.githubusercontent.com/32935365/68195257-e2e35680-fff9-11e9-9c5a-7a44347b8f1f.PNG)

### 원격 repository 삭제
```
git remote rm git_test
```

## Pull & Push
### Pull
```
git pull
```

### repository 갱신
- 원격 repository에서 데이터는 가져오지만 merge는 x
- 진행중인던 작업을 마무리 후 merge 해주어야함!
```
git fetch
```
![git fetch](https://user-images.githubusercontent.com/32935365/68195269-e7a80a80-fff9-11e9-8115-25e6334a62ee.PNG)

### git log로 확인 후 merge
- git log
```
git log origin/master
```
![git log originmaster](https://user-images.githubusercontent.com/32935365/68195282-ef67af00-fff9-11e9-864c-c707d74f6d2c.PNG)

- git merge
```
git merge origin/master
```
![git merge originmaster](https://user-images.githubusercontent.com/32935365/68195419-2938b580-fffa-11e9-9e0a-2adc4ecb0408.PNG)

### Push
- local repository -> remote repository에 반영
```
git push origin master
```

## Reset
```
git reset --hard {commit 번호}

## 실습 1
![git conflict practice](https://user-images.githubusercontent.com/32935365/68195534-600ecb80-fffa-11e9-8af9-466014bce3f0.PNG)

<hr>

## 실습 2
### git remote
![1 git remote](https://user-images.githubusercontent.com/32935365/68217334-c5c47d00-0025-11ea-93a6-a18f2b3b87e6.PNG)

### fetch 후 head 변경
![2 fetch 후 head 변경](https://user-images.githubusercontent.com/32935365/68217355-ce1cb800-0025-11ea-8edb-5ed679d3ae9b.PNG)

### merge
![3 merge](https://user-images.githubusercontent.com/32935365/68217370-d4ab2f80-0025-11ea-97c3-de05279d0fc4.PNG)

### commt & push
![4 commit   push 기릿](https://user-images.githubusercontent.com/32935365/68217399-e2f94b80-0025-11ea-907c-ff9810725593.PNG)
