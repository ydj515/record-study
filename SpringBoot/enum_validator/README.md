# SpringBoot - enum validator

-EnumValid
```java
@Target({ElementType.METHOD, ElementType.FIELD, ElementType.TYPE, ElementType.CONSTRUCTOR, ElementType.PARAMETER, ElementType.TYPE_USE})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = EnumValidator.class)
@Documented
public @interface EnumValid {
    String message() default "Invalid request parameter";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
    Class<? extends Enum<?>> enumClass();
    boolean ignoreCase() default false;
}
```
- EnumValidList
```java
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = EnumListValidator.class)
public @interface EnumListValid {
    String message() default "Invalid request parameter list type";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
    Class<? extends Enum<?>> enumClass();
    boolean ignoreCase() default false;
}
```
- EnumValidator
```java
public class EnumValidator implements ConstraintValidator<EnumValid, String> {
    private List<String> acceptedValues;
    @Override
    public void initialize(EnumValid constraintAnnotation) {
        acceptedValues = Stream.of(constraintAnnotation.enumClass().getEnumConstants())
                .map(e -> {
                    if (e instanceof DisplayNameAware) {
                        return ((DisplayNameAware) e).getDisplayName();
                    } else {
                        return e.toString();
                    }
                })
                .collect(Collectors.toList());
    }
    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        if (value == null || StringUtil.isBlank(value)) {
            return false;
        }
        return acceptedValues.stream().anyMatch(val -> val.equals(value));
    }
}
```
- EnumListValidator
```java
public class EnumListValidator implements ConstraintValidator<EnumListValid, List<String>> {
    private List<String> acceptedValues;
    @Override
    public void initialize(EnumListValid constraintAnnotation) {
        acceptedValues = Stream.of(constraintAnnotation.enumClass().getEnumConstants())
                .map(e -> {
                    if (e instanceof DisplayNameAware) {
                        return ((DisplayNameAware) e).getDisplayName();
                    } else {
                        return e.toString();
                    }
                })
                .collect(Collectors.toList());
    }
    @Override
    public boolean isValid(List<String> value, ConstraintValidatorContext context) {
        if (value == null || value.stream().anyMatch(val -> val.trim().isEmpty())) {
            return false;
        }
        return new HashSet<>(acceptedValues).containsAll(value);
    }
}
```
- DataTypeEnum
```java
public enum DataTypeEnum implements DisplayNameAware {
    FILE("FILE"),
    API("API"),
    STD("STD"),
    LINK("LINK");
    private final String displayName;
    DataTypeEnum(String displayName) {
        this.displayName = displayName;
    }
    @Override
    public String getDisplayName() {
        return displayName;
    }
}
```
- SearchParams
```java
@Data
public class SearchParams {
	
	@EnumValid(enumClass = LocaleEnum.class, message = "locale should be kor or eng")
    private String locale = "kor";
    @ApiModelProperty(value = "검색어", notes = "검색어")
    @Pattern(regexp = "^[a-zA-Z0-9가-힣*]+([ ][a-zA-Z0-9가-힣*]+)*$", message = "keyword" + DEFAULT_REGEX_MESSAGE)
    private String keyword = "*";
    @ApiModelProperty(value = "데이터 타입", notes = "FILE, API, STD, LINK")
    @EnumListValid(enumClass = DataTypeEnum.class, message = DATA_TYPE_MEESAGE)
    private List<String> dataType = Arrays.asList("FILE", "API", "STD"); // data type
}	
```
- Controller
```java
@Slf4j
@Controller
@AllArgsConstructor
@RequestMapping("/")
public class SearchController {
    private final SearchService searchService;
    @ApiOperation(value = "service", notes = "search service")
    @ApiResponses({
            @ApiResponse(code = 200, message = "Success"),
            @ApiResponse(code = 400, message = "Invalid access"),
            @ApiResponse(code = 405, message = "Not Supported Request Method"),
            @ApiResponse(code = 500, message = "Internal Server Error")
    })
    @ResponseBody
    @PostMapping("/search-data")
    public ResponseEntity<?> search(@RequestBody @Validated SearchParams searchParams) throws IOException {
        AggregationResult result = searchService.searchData(searchParams);
        ApiResponseData response = new ApiResponseData<>(HttpStatus.OK.value(), AggregationResultMapper.INSTANCE.aggregationToAggregationDTO(result));
        return ResponseEntity.ok().body(response);
    }
}
```