@Slf4j
@Controller
@RequiredArgsConstructor
@RequestMapping("/captcha")
public class CaptchaController {

    private final String captchaAnswerKey = "captchaAnswer";

    /**
     * 보안이미지 생성
     */
    @RequestMapping(value = "")
    public void captcha(HttpServletRequest request, HttpServletResponse response, ModelMap model) throws Exception {

        try {

            // 200 * 50 에해당하는 이미지 사이즈를 지정하고, 자동가입방지 문자 길이를 설정한다.
            Captcha captcha = new Captcha.Builder(150, 50)
                    .addText()
                    .addBackground()
                    .addNoise()
                    .build();

            response.setHeader("Cache-Control", "no-store");
            response.setHeader("Pragma", "no-cache");

            // 캐쉬를 지우기 위해 헤더값을 설정
            response.setDateHeader("Expires", 0);

            // 리턴값을 image형태로 설정
            response.setContentType("image/png");

            // Image를 write 한다
            writeImage(response, captcha.getImage());

            // 세션에 자동가입방지 문자를 저장한다.
            request.getSession().setAttribute(captchaAnswerKey, captcha.getAnswer());
            log.debug("captcha 자동가입방지 문자 : " + captcha.getAnswer());
        } catch (Exception e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
    }

    /**
     * 보안이미지값 검증
     */
    @RequestMapping(value = "/validCaptcha")
    public ResponseEntity<?> getCaptcha(HttpServletRequest request, HttpServletResponse response, @RequestBody CaptchaDto captchaDto, ModelMap model) throws Exception {

        Map<String, Object> result = new HashMap<>();

        boolean isCorrect = captchaDto.checkAnswer(request, captchaAnswerKey);

        result.put("isCorrect", isCorrect);
        result.put("message", captchaDto.getMessage());

        return new ApiResponse(result);
    }

    private void writeImage(HttpServletResponse response, BufferedImage bi) {
        response.setHeader("Cache-Control", "private,no-cache,no-store");
        response.setContentType("image/png");
        try {
            writeImage(response.getOutputStream(), bi);
        } catch (IOException e) {
            log.error("Error occurred while writing the image(HttpServletResponse): " + e.getMessage());
        }
    }

    private void writeImage(OutputStream os, BufferedImage bi) {
        try {
            ImageIO.write(bi, "png", os);
            os.close();
        } catch (IOException e) {
            log.error("Error occurred while writing the image(OutputStream): " + e.getMessage());
        }
    }

}