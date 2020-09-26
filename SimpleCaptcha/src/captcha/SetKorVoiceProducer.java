package captcha;
 
import java.util.HashMap;
import java.util.Map;
 
import nl.captcha.audio.Sample;
import nl.captcha.audio.producer.VoiceProducer;
import nl.captcha.util.FileUtil;
 
public class SetKorVoiceProducer  implements VoiceProducer  {
    
    private static final Map<Integer, String> DEFAULT_VOICES_MAP;
 
    static {
        DEFAULT_VOICES_MAP = new HashMap<>();
        StringBuilder sb;
        
        for (int i = 0; i < 10; i++) { // 현재 숫자 0~9 까지만 해놨으니까 알파벳도 추가하려면 더 늘려야함
            sb = new StringBuilder("/sounds/ko/numbers/"); // 파일 경로 넣기
            sb.append(i);            
            sb.append(".wav");            
            DEFAULT_VOICES_MAP.put(i, sb.toString());
        }
    }
    
    private final Map<Integer, String> voices;
 
    public SetKorVoiceProducer() {
        this(DEFAULT_VOICES_MAP);
    }
 
 
    public SetKorVoiceProducer(Map<Integer, String> voices) {
        this.voices = voices;
    }
 
    @Override
    public Sample getVocalization(char num) {
       try {
            Integer.parseInt(num + "");
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Expected <num> to be a number, got '" + num + "' instead.",e);
        }
 
        int idx = Integer.parseInt(num + "");
        String filename = voices.get(idx); 
        return FileUtil.readSample(filename);
    }
}