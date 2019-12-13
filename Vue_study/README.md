# Vue Study

## WHat is Vue
- **MVVM의 ViewModel layer**에 해당하는 library
- 데이터 바인딩과 화면 단위 컴포넌트를 제공. 관련 API를 지원
- **양방향 데이터 바인딩 제공**(Angular 처럼)
- **컴포넌트 간 통신**은 React의 **단방향 데이터 흐름**(부모 -> 자식)
- Angular, React와 비교했을 때 **가볍고 빠름****
- 문법이 단순하고 간결
- React와 마찬가지로 **Virtual DOM**을 사용
- 화면의 DOM의 변경이 일어날 때마다 화면을 다시 그리지 X
- JS 객체로 DOM의 모양을 잡아놓고 화면의 횟수를 최소화 하여 Browser의 부하를 줄임

![vue picture](https://user-images.githubusercontent.com/32935365/70506871-9c3fc980-1b6e-11ea-8545-abf47b405b2c.PNG)  
![mvvm](https://user-images.githubusercontent.com/32935365/70506886-a4980480-1b6e-11ea-8f6a-55d957dd7459.PNG)  


## Vue Install
### Install
```
npm install -g vue-cli
mkdir {폴더이름}
cd {폴더이름}
npm install
```

### srart Vue
```
vue init pwa {폴더이름}
```  
- 아래와 같이 따라하면대용 ㅎ_ㅎ  
![vue start](https://user-images.githubusercontent.com/32935365/70500470-fdf83780-1b5e-11ea-99da-0211c0559c19.PNG)

- 아래의 명령어 입력하고 아래와 같이 나온다면 성공
```
cd to-do-frontend
npm install
npm run dev
```  
![vue seccess](https://user-images.githubusercontent.com/32935365/70500684-7bbc4300-1b5f-11ea-871e-528ce24bde0c.PNG)

### 폴더 구조
- src
    - **assets** : css, png와 같은 UI 관련 resources
    - **components** : 재사용할수 있는 단위. html templates, vue.js function
    - **router** : 라우팅 정보

- static
    - **img** : image파일들

- package.json
    - 설정 파일

### Bootstrap 추가
```
npm install bootstrap-vue bootstrap --save
npm install
```

## Grammar
### Vue Instance
- Vue 생성자 함수를 이용하여 인스턴스 생성
- Vue 객체 생성 시에 data, templage, el, methods, life cycle hook등을 옵셕 속성으로 포함 가능
```js
new Vue({
    el: '#app',
    router,
    template: '<App/>',
    components: { App },
    data: {
        msg: 'Hello world'
    }
})
```
- **el**  
내부적으로 연결된 템플릿값을 넣어준다  
```js
{
    el: '#app'
}
```

- **data**  
템플릿에 바인딩할 데이터들의 집합  
```js
{
    data: {
        msg: 'Hello world'
    }
}
```

- **methods**  
주로 돔에 연결할 event handler  
```html
<div id="app">
    <button v-on:click="onClick">클릭미!</button>
</div>

<script>
var vm = new Vue({
    el: '#app',
    methods: {
        onClick: function(){ alert('Hello world'); }
    }
});
</script>
```

- **computed**  
methods와 비슷한 역할을 하지만 **캐쉬를 가지고 있어**
함수 본문에서 사용하는 **상태값에 변화가 없으면** 함수를 수행하지 않고
저장한 **캐쉬값을 바로 반환**하기 때문에 **비교적 빠름**
```html
<div id="app">{{ greeting }}</div>

<script>
var vm = new Vue({
    el: '#app',
    data: { name: 'Chris' },
    computed: {
        greeting: function(){ return 'Hello ' + this.name; }
    }
});
</script>
```

### child component
- Vue.component로 생성할 수 있음
```html
<div id="child">Hello {{ name }}</div>

<div id="app"><Child></Child></div>

<script>
Vue.component('Child', {
    el: '#child',
    data: function() {
        return {
            name: 'Chris'
        }
    }
});

var vm = new Vue({
    el: '#app'
});
</script>
```

### Data 전달방법
- 기본적으로 부모 -> 자식 으로만 데이터 전달 가능
- 자식 -> 부모 : event emit
- 부모 -> 자식 : props
- props를 이용해 데이터 전달
![data](https://user-images.githubusercontent.com/32935365/70513096-4bcb6a80-1b74-11ea-91fb-f2397b983ddc.PNG)  

- props
```html
<!-- 상위 컴포넌트 -->
<div id="app">
    <!-- 하위 컴포넌트에 상위 컴포넌트가 갖고 있는 message를 전달함 -->
    <child-component v-bind:propsdata="message"></child-component>
</div>
<script>
    // 하위 컴포넌트
    Vue.component('child-component', {
        // 상위 컴포넌트의 data 속성인 message를 propsdata라는 속성으로 넘겨받음
        props: ['propsdata'],
        template: '<p>{{ propsdata }}</p>'
    });

    // 상위 컴포넌트
    var app = new Vue({
        el: '#app',
        data: {
            message: 'Hello Vue! from Parent Component',
        }
    });
</script>
```

- EventBus  
상하 관계가 아닌 같은 level의 컴포넌트 통신
```js
// 화면 개발을 위한 인스턴스와 다른 별도의 인스턴스를 생성하여 활용
var eventBus = new Vue();

new Vue({
    // ...
})

eventBus.$emit('refresh', 10); // 이벤트를 발생시킬 컴포넌트에서 $emit 호출

// 이벤트 버스 이벤트는 일반적으로 라이프 사이클 함수에서 수신
new Vue({
    created: function() {
        eventBus.$on('refresh', function(data) {
            console.log(data); // 10
        });
    }
})

new Vue({
    methods: {
        callAnyMethod() {
            // ...
        }
    },
    created() {
        var vm = this;
        eventBus.$on('refresh', function(data) { // 이벤트를 받을 컴포넌트에서 $on
            console.log(this); // 여기서의 this는 이벤트 버스용 인스턴스를 가리킴
            vm.callAnyMethod() // vm은 현재 인스턴스를 가리킴
        });
    }
})
```
- 만약 eventBus의 콜백 함수 안에서 해당 컴포넌트의 메소드를 참고하려면 **vm**을 사용
```js
new Vue({
    methods: {
        callAnyMethod() {
            // ...
        }
    },
    created() {
        var vm = this;
        eventBus.$on('refresh', function(data) {
            console.log(this); // 여기서의 this는 이벤트 버스용 인스턴스를 가리킴
            vm.callAnyMethod() // vm은 현재 인스턴스를 가리킴
        });
    }
})
```

- Example  
![123](https://user-images.githubusercontent.com/32935365/70597304-5f85d800-1c2b-11ea-84a2-85dd24a1f830.PNG)  

```html
<div id="root">
    <input type="text" v-model="input" @keydown.enter="addTodo" />
    <button @click="addTodo">Add TODO</button>
    <ul>
        <li v-for="todo in todos" v-text="todo.text" :style="{ textDecoration: todo.isDone ? 'line-through' : 'none' }" @click="toggleTodo(todo)"></li>
    </ul>
    <p>Total: {{ todosCount }}</p>
    <p>Active: {{ todosCount - doneTodosCount }}</p>
    <p>Done: {{ doneTodosCount }}</p>
</div>
```

```js
new Vue({
    el: '#root',
    data: {
        input: '',
        todos: []
    },
    computed: {
        todosCount() {
            return this.todos.length.toString();
        },
        doneTodosCount() {
            return this.todos.filter(e => e.isDone).length;
        }
    },
    methods: {
        addTodo() {
            this.todos.push({
                text: this.input,
                isDone: false
            });
            this.input = '';
        },
        toggleTodo(todo) {
            todo.isDone = !todo.isDone;
        }
    }
});
```


### Router
- npm, cdn 방식 모두 지원
- npm 방식
```js
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
```
- npm 방식
```
npm install vue-router --save
```

- **루트URL/#/라우터이름**의 기본 구조
- #을 제거 하고 싶으면 아래와 같이 mode 속성 추가!
```js
new VueRouter({
    mode: 'history'
})
```

### 라우팅 방식
![router](https://user-images.githubusercontent.com/32935365/70519582-8686d000-1b7f-11ea-8d83-ea61bfa5eb59.PNG)  

- Nested Routers  
특정 URL에 지정된 1개의 컴포넌트가 여러 개의 하위 컴포넌트를 갖는 것  
트리 구조식으로 상위 컴포넌트가 하위 컴포넌트를 포함하는 parent - child 구조
```html
<!-- localhost:5000 -->
<div id="app">
    <router-view></router-view>
</div>

<!-- localhost:5000/home -->
<div>
    <p>Main Component rendered</p>
    <app-header></app-header>
</div>
```
```js
// 'localhost:5000/home'에 접근하면 Main과 Header 컴포넌트 둘다 표시된다.
{
    path : '/home',
    component: Main,
    children: [
        {
            path: '/',
            component: AppHeader
        },
        {
            path: '/list',
            component: List
        },
    ]
}
```

- **Named Views**  
특정 URL에 여러 개의 컴포넌트를 영역 별로 지정하여 렌더링 하는 것
```html
<div id="app">
    <router-view name="appHeader"></router-view>
    <router-view></router-view>
    <router-view name="appFooter"></router-view>
</div>
```
```js
{
    path : '/home',
    // Named Router
    components: {
        appHeader: AppHeader,
        default: Body,
        appFooter: AppFooter
    }
}
```



### Axios
- HTTP 통신 library
- CDN, npm 설치 방식 지원
- Pormis 기반이라 코드를 간결하게 작성 용이

- install
```
npm install axios
```

```html
<script>
import axios from 'axios'

export default {
    name: 'hello',
    data: () => {
        return {
            toDoItems: [] // toDoItems를 빈 리스트로 초기화한다.
        }
    },
    created () { // 초기화 함수를 정의 한다.
        axios.get('http://127.0.0.1:5000/todo/') // http://localhost:5000/todo/에 get call을 한다.
            .then(response => {
                this.toDoItems = response.data.map(r => r.data) // 반환되는 값을 toDoItems에 저장한다.
            })
            .catch(e => {
                console.log('error : ', e) // 에러가 나는 경우 콘솔에 에러를 출력한다
            })
    }
}
</script>
```

### Template

- data binding
```html
<div>{{ str }}</div>
<div>{{ number + 1 }}</div>
<div>{{ message.split('').reverse().join('') }}</div>
```

- directives
```html
<!-- seen의 진위 값에 따라 p 태그가 화면에 표시 또는 미표시 -->
<p v-if="seen">Now you see me</p>
<!-- 화면에 a 태그를 표시하는 시점에 뷰 인스턴스의 url 값을 href에 대입 -->
<a v-bind:href="url"></a>
<!-- 버튼에 클릭 이벤트가 발생했을 때 doSomething이라는 메서드를 실행 -->
<button v-on:click="doSomething"></button>
```

- filters  
화면에 표시되는 텍스트의 형식을 편하게 바꿀수 있음  
"|"를 사용하여 여러개의 필터를 적용할 수 있음
```html
<!-- message 값에 capitalize 필터를 적용하여 첫 글자를 대문자로 변경 -->
{{ message | capitalize }}
```
```js
new Vue({
    filters: {
        capitalize: function(value) {
            if (!value) return '';
            value = value.toString();
            return value.charAt(0).toUpperCase() + value.slice(1);
        }
    }
})
```

## Error
### V-for 태그 오류
```
error: Elements in iteration expect to have 'v-bind:key' directives (vue/require-v-for-key) at

[vue/require-v-for-key] 
Elements in iteration expect to have 'v-bind:key' directives
```
- 조치 방법  
v-bind:key="toDoItem"처럼 **v-bind:key 속성 추가**  
![111](https://user-images.githubusercontent.com/32935365/70500900-fb4a1200-1b5f-11ea-86a9-32edce076f94.PNG)

[출처]  
https://joshua1988.github.io/web-development/vuejs/vuejs-tutorial-for-beginner/