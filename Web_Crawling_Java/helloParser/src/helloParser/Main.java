package helloParser;

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class Main {

	public static void main(String[] args) {

		// URL 선언
		String url = "https://yahoo.com";

		Document doc = null;

		try {
			// GET 방식으로 HTML 가져오기
			doc = Jsoup.connect(url).get();

			// POST 방식으로 HTML 가져오기
			doc = Jsoup.connect(url).post();
			
			// 결과를 못가져오는 경우 header에 값을 추가해주어야한다.
			doc = Jsoup.connect(url)
		            .userAgent("Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
		            .header("scheme", "https")
		            .header("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
		            .header("accept-encoding", "gzip, deflate, br")
		            .header("accept-language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6")
		            .header("cache-control", "no-cache")
		            .header("pragma", "no-cache")
		            .header("upgrade-insecure-requests", "1")
		            .get();

			// 3. 가져온 HTML Document 를 확인하기
			System.out.println(doc.toString());
			
			// Elements els = doc.select(".trending-list");
			// System.out.println(els);
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
