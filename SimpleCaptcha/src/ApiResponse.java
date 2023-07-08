@Getter
public class ApiResponse extends ResponseEntity<ResponseResult> {

    public ApiResponse(Object data, ApiStatusEnum statusEnum) {
        super(new ResponseResult(
                statusEnum.getStatus().value(),
                statusEnum.getMsg(),
                data
        ), statusEnum.getStatus());
    }

    public ApiResponse(ApiStatusEnum statusEnum) {
        this(null, statusEnum);
    }

    public ApiResponse(Object data) {
        this(data, ApiStatusEnum.OK);
    }

    public ApiResponse() {
        this(ApiStatusEnum.OK);
    }
}