# SpringBoot - WebMvcConfig & ArgumentResolver

- ClientIP
```java
@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
public @interface ClientIP {
}
```

- LoginUser
```java
@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
public @interface LoginUser {
}
```

- ClientIPArgumentResolver
```java
@Component
public class ClientIPArgumentResolver implements HandlerMethodArgumentResolver {

    private static final String[] IP_HEADER_CANDIDATES = {
            "X-Forwarded-For", "Proxy-Client-IP", "WL-Proxy-Client-IP",
            "HTTP_X_FORWARDED_FOR", "HTTP_X_FORWARDED", "HTTP_X_CLUSTER_CLIENT_IP",
            "HTTP_CLIENT_IP", "HTTP_FORWARDED_FOR", "HTTP_FORWARDED", "HTTP_VIA",
            "REMOTE_ADDR"
    };

    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        return parameter.hasParameterAnnotation(ClientIP.class);
    }

    @Override
    public Object resolveArgument(MethodParameter param, ModelAndViewContainer mavc, NativeWebRequest req,
                                  WebDataBinderFactory wbf) throws Exception {

        HttpServletRequest request = (HttpServletRequest) req.getNativeRequest();

        for (String header : IP_HEADER_CANDIDATES) {
            String ip = request.getHeader(header);

            if (ip != null && ip.length() != 0 && !"unknown".equalsIgnoreCase(ip)) {
                return ip;
            }
        }

        return request.getRemoteAddr();
    }
}
```

- LoginUserArgumentResolver
```java
@Component
@RequiredArgsConstructor
public class LoginUserArgumentResolver implements HandlerMethodArgumentResolver {

    private final MemberService memberService;

    @Value("${app.site.url}")
    private String siteUrl;

    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        return parameter.hasParameterAnnotation(LoginUser.class);
    }

    @Override
    public Object resolveArgument(MethodParameter methodParameter,
                                  ModelAndViewContainer modelAndViewContainer,
                                  NativeWebRequest nativeWebRequest,
                                  WebDataBinderFactory webDataBinderFactory) {

        HttpServletRequest request = (HttpServletRequest) nativeWebRequest.getNativeRequest();

        String loginId = request.getRemoteUser();

        Member member = null;

        if (loginId != null) {
            member = memberService.findByUserId(loginId);
        }

        Object result = null;

        if (!Objects.isNull(member)) {
            result = member;
            modelAndViewContainer.addAttribute("loginUser", member);
        } else if (memberService.TEST_USER_ID.equals(loginId)) {
            result = memberService.findByMbrPno(loginId);
            modelAndViewContainer.addAttribute("loginUser", result);
        }

        modelAndViewContainer.addAttribute("siteUrl", siteUrl);

        return result;
    }
}
```

- WebMvcConfig
```java
@Slf4j
@Configuration
@RequiredArgsConstructor
public class WebMvcConfig implements WebMvcConfigurer {

    private final ClientIPArgumentResolver clientIpResolver;
	private final LoginUserArgumentResolver loginUserArgumentResolver;

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers) {
        argumentResolvers.add(clientIpResolver);
        argumentResolvers.add(requestUrlArgumentResolver);
    }

    @Bean
    public LocaleResolver localeResolver() {
        SessionLocaleResolver slr = new SessionLocaleResolver();
        slr.setDefaultLocale(Locale.KOREA);
        return slr;
    }

}
```

- controller
```java
@GetMapping("")
    public String serviceIndex(@ClientIP String clientIP,
                               @LoginUser Member loginUser, // @LoginUser Object loginUser
                               Model model) throws Exception {
    	...
}
```