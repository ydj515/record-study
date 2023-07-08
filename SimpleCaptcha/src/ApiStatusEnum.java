@Getter
@RequiredArgsConstructor
public enum ApiStatusEnum {
    OK(HttpStatus.OK, "정상 처리되었습니다"),
    PAGE_NOT_FOUND(HttpStatus.NOT_FOUND, "페이지를 찾을 수 없습니다"),
    BAD_REQUEST(HttpStatus.BAD_REQUEST, "잘못된 요청입니다"),
    UNAUTHORIZED(HttpStatus.UNAUTHORIZED, "권한이 부족합니다"),
    INTERNAL_ERROR(HttpStatus.INTERNAL_SERVER_ERROR, "서버에러가 발생하였습니다");

    private final HttpStatus status;
    private final String msg;
}