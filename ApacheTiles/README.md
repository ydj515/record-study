# ApacheTiles

- https://github.com/ydj515/WebFrameWork2_Report1
- https://github.com/ydj515/WebFrameWork2_Report2

## What is Apache Tiles
- Template, Attribute, Definition
- Free open-sourced templating framework for moder Java Applications
- runtime시에 page fragments(header, footer, navigation menu...)를 조립할 수 있다.

## Tiles의 장점
- 사용자 입장에서 page들이 **template화 되어 있어서 일관성있게 느낌**
- page들의 **중복성 제거 -> 유지보수 용이**

## Tiles 설정

### pom.xml
```xml
<!-- https://mvnrepository.com/artifact/org.apache.tiles/tiles-extras -->
<dependency>
  <groupId>org.apache.tiles</groupId>
  <artifactId>tiles-extras</artifactId>
  <version>3.0.8</version>
</dependency>
```

### servlet-context.xml
- View Resolver는 더의상 필요없다.
- View Resolver대신에 TilesViewResolver를 사용
```xml
<!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
<!-- <beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver"> 
       <beans:property name="prefix" value="/WEB-INF/views/" />
       <beans:property name="suffix" value=".jsp" />
     </beans:bean> -->

<!-- definition 이름과 view 이름을 mapping -->
<beans:bean id="tilesViewResolver"
  class="org.springframework.web.servlet.view.tiles3.TilesViewResolver">
</beans:bean>

<beans:bean id="tilesConfigurer"
  class="org.springframework.web.servlet.view.tiles3.TilesConfigurer">
  <beans:property name="definitions">
    <beans:list>
      <beans:value>/WEB-INF/tiles-def/tiles.xml</beans:value> <!-- root 경로는 webapp -->
    </beans:list>
  </beans:property>
</beans:bean>
```

### tiles.xml
- src/main/webapp/WEB-INF/tiles-def/tiles.xml에서 설정
- 아래의 코드처럼 definition으로 정의하고 **extends**로 상속받아서 사용 가능하다.  
- **put-attribute name**의 값은 각 jsp 파일에서 **insertAttribute의 name 속성**이 됨

```xml
<definition name="base" template="/WEB-INF/templates/layout.jsp">
  <put-attribute name="title" value="eStore homepage" />
  <put-attribute name="menu" value="/WEB-INF/templates/menu.jsp" />
  <put-attribute name="footer" value="/WEB-INF/templates/footer.jsp" />
</definition>

<!-- definition name의 값과 controller의 return 값이랑 일치해야됨 -->
<!-- menu와 footer의 값은 계속 상속 받는거라 따로 안쓴거임 -->
<definition name="home" extends="base">
  <put-attribute name="title" value="My eStore homepage" />
  <put-attribute name="body" value="/WEB-INF/views/home.jsp" />
</definition>

<definition name="products" extends="base">
  <put-attribute name="title" value="Products page" />
  <put-attribute name="body" value="/WEB-INF/views/products.jsp" />
</definition>
<definition name="login" extends="base">
  <put-attribute name="title" value="Login page" />
  <put-attribute name="body" value="/WEB-INF/views/login.jsp" />
</definition>
```


