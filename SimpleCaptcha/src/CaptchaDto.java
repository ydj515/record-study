@Getter
@Setter
public class CaptchaDto {
    private String captchaAnswerKey; // 세션에 저장되는 이름
    private String inputCaptcha; // 사용자 입력값
    private String message; // return message

    private void setCaptcha(String captchaAnswerKey) {
        this.captchaAnswerKey = captchaAnswerKey;
    }

    public boolean checkAnswer(HttpServletRequest request, String captchaAnswerKey) {
        setCaptcha(captchaAnswerKey);
        String answer = (String) request.getSession().getAttribute(captchaAnswerKey);
        boolean result = inputCaptcha.equals(answer);
        message = result ? "보안 문자 인증 성공하였습니다." : "보안 문자 인증에 실패하였습니다. 다시 입력해주세요.";
        return result;
    }
}