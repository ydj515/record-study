package captcha;
 
import nl.captcha.text.producer.TextProducer;
 
/**
 * 전달받은 문자열을 그대로 오디오캡차가 이용할수있도록 생성한 클래스 
 */
public class SetTextProducer  implements TextProducer {
 
 
    private final String inputString;
 
    public SetTextProducer(String inputString) {    
        this.inputString = inputString; 
    }
 
    @Override
    public String getText() {        
        return inputString;
    }
}