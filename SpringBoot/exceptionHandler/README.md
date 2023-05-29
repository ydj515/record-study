# SpringBoot - exception handler

- ExceptionHandlerAdvice
```java
@Slf4j
@ControllerAdvice
public class ExceptionHandlerAdvice extends ResponseEntityExceptionHandler {

    /**
     * 400
     */
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ExceptionHandler({RuntimeException.class})
    public ResponseEntity<?> badRequestException(final RuntimeException exception) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.BAD_REQUEST)
                .message("The request parameter format is out of order")
                .build();
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }

    /**
     * 400
     */

    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @Override
    protected ResponseEntity<Object> handleHttpMessageNotReadable(HttpMessageNotReadableException exception, HttpHeaders headers, HttpStatus status, WebRequest request) {
        log.error(exception.toString());
//        String message = exception.getBindingResult().getFieldError().getDefaultMessage();

        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.BAD_REQUEST)
//                .message(message)
                .build();
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }

    /**
     * 400
     */
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException exception, HttpHeaders headers, HttpStatus status, WebRequest request) {
        log.error(exception.toString());
        String message = exception.getBindingResult().getFieldError().getDefaultMessage();

        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.BAD_REQUEST)
                .message(message)
                .build();
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }

    // 401
    @ResponseStatus(HttpStatus.UNAUTHORIZED)
    @ExceptionHandler({AccessDeniedException.class})
    public ResponseEntity<?> handleAccessDeniedException(final AccessDeniedException exception) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.UNAUTHORIZED)
                .build();
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(errorResponse);
    }

    /**
     * 401
     * request header의 Authorization이 비어있을 경우
     */
    @ResponseStatus(HttpStatus.UNAUTHORIZED)
    @ExceptionHandler({MissingRequestHeaderException.class})
    protected ResponseEntity<?> missingRequestHeaderException(final MissingRequestHeaderException exception) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.UNAUTHORIZED)
                .build();
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(errorResponse);
    }


    /**
     * 405
     */
    @ResponseStatus(HttpStatus.METHOD_NOT_ALLOWED)
    @Override
    protected ResponseEntity<Object> handleHttpRequestMethodNotSupported(HttpRequestMethodNotSupportedException exception, HttpHeaders headers, HttpStatus status, WebRequest request) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.METHOD_NOT_ALLOWED)
                .build();
        return ResponseEntity.status(HttpStatus.METHOD_NOT_ALLOWED).body(errorResponse);
    }

    /**
     * 415
     * content type error
     */
    @ResponseStatus(HttpStatus.UNSUPPORTED_MEDIA_TYPE)
    @ExceptionHandler({HttpMediaTypeException.class})
    protected ResponseEntity<?> httpMediaTypeException(final HttpMediaTypeException exception) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.UNSUPPORTED_MEDIA_TYPE)
                .build();
        return ResponseEntity.status(HttpStatus.UNSUPPORTED_MEDIA_TYPE).body(errorResponse);
    }


    /**
     * 500
     */
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    @ExceptionHandler({SocketTimeoutException.class})
    protected ResponseEntity<?> socketTimeoutException(final SocketTimeoutException exception) {
        log.error(exception.toString());
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .message("Timeout On Connection")
                .build();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResponse);
    }

    /**
     * 500
     */
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    @ExceptionHandler({Exception.class})
    public ResponseEntity<?> handleAll(final Exception exception) {
        ErrorResponse errorResponse = ErrorResponse.builder()
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .message("Unexpected error occurred")
                .build();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResponse);
    }
}
```

- ErrorResponse
```java
@Getter
@Builder
public class ErrorResponse {
    private final LocalDateTime timestamp = LocalDateTime.now();
    private final int statusCode;
    private final HttpStatus status;
    private final String message;

    public static class ErrorResponseBuilder {
        public ErrorResponseBuilder status(HttpStatus status) {
            this.status = status;
            this.statusCode = status.value();
            this.message = status.getReasonPhrase();
            return this;
        }
    }
}
```