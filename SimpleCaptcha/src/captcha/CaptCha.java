package captcha;
 
import static nl.captcha.Captcha.NAME;
 
import java.awt.Color;
import java.awt.Font;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
 
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
 
import nl.captcha.Captcha;
import nl.captcha.backgrounds.GradiatedBackgroundProducer;
import nl.captcha.gimpy.DropShadowGimpyRenderer;
import nl.captcha.servlet.CaptchaServletUtil;
import nl.captcha.text.producer.NumbersAnswerProducer;
import nl.captcha.text.renderer.DefaultWordRenderer;
 
public class CaptCha {
    private static final long serialVersionUID = 1L;
    private static int _width = 150; //이미지 가로크기
    private static int _height = 50; //이미지 높이
    private static int _fontsize = 44; //폰트크기
 
    public CaptCha() {
        super();
    }
 
    public void getCaptCha(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        
        try {    
            // 폰트 설정 =========================================================
            List<Font> fontList = new ArrayList<Font>();
            fontList.add(new Font("", Font.HANGING_BASELINE, 40));//
            fontList.add(new Font("Courier", Font.ITALIC, 40));
            fontList.add(new Font("", Font.PLAIN, 40));
 
            List<Color> colorList = new ArrayList<Color>();
            // colorList.add(Color.green);
            // colorList.add(Color.pink);
            // colorList.add(Color.gray);
            colorList.add(Color.black);
            // colorList.add(Color.blue);
            // 폰트 설정 =========================================================
 
            Captcha captcha = new Captcha.Builder( _width, _height)
                    // .addText(wordRenderer)                    
                    .addText(new NumbersAnswerProducer(6), //6자리 숫자로 된 문자를 추가
                    new DefaultWordRenderer(colorList, fontList)) //글자 꾸미기(색상, 폰트)
                    .gimp(new DropShadowGimpyRenderer()).gimp()
                    // BlockGimpyRenderer,FishEyeGimpyRenderer,RippleGimpyRenderer,ShearGimpyRenderer,StretchGimpyRenderer
                    .addNoise().addNoise().addBorder()
                    .addBackground(new GradiatedBackgroundProducer()) 
                    // FlatColorBackgroundProducer,SquigglesBackgroundProducer,TransparentBackgroundProducer
                    .build();
 
            req.getSession().setAttribute(NAME, captcha);
            CaptchaServletUtil.writeImage(resp, captcha.getImage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}