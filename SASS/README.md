# SASS

- Sass(Syntactically Awesome StyleSheets)
- CSS pre-processor로서 CSS의 한계와 단점을 보완하여 보다 가독성이 높고 코드의 재사용에 유리한 CSS를 생성하기 위한 CSS의 확장(extension)
- CSS의 간결한 문법은 배우기 쉬우며 명확
- 프로젝트의 규모가 커지고 수정이 빈번히 발생함에 따라 쉽게 지저분해지고 유지보수도 어려워지는 단점이 존재

## Install
### node-Sass
1. node 설치 : https://nodejs.org/en/download/
2. 
```bash
$ node -v
$ npm install -g node-Sassnode-sass -V
```

### Ruby Sass
- mac은 이미 ruby가 설치되어있기 때문에 생략한다.
- 설치 도중 path추가도 체크해야한다!!!
1. rubby 설치 : https://rubyinstaller.org/downloads/
2. 
```bash
$ gem install sass
$ sass -v
```

### 사용법
```bash
$ sass --watch src/main/webapp/scss/app.scss:src/main/webapp/css/app.css
```