# Web Crawling Java

## Jsoup 설치
1. jsoup-1.11.2.jar core library를 https://jsoup.org/download 의 주소에서 다운
2. Maven에 dependency 추가
```xml
<dependency>
    <groupId>org.jsoup</groupId>
    <artifactId>jsoup</artifactId>
    <version>1.11.2</version>
</dependency>
```

## 사용
```java
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
```

## 크롤링 시 주의사항 robots.txt
- robots.txt 파일은 웹 크롤러가 해당 페이지의 접근을 제어하기 위한 하나의 약속
- robots.txt파일은 사이트의 최상위인 Root(/)에 위치해야 하며 로봇 배제 표준 프로토콜을 이용하여 섹션별, 웹 크롤러의 종류(데스크탑, 모바일, 구글)로 사이트에 대한 접근을 제어함

### 작성법
- 루트 경로 밑에 robots.txt가 있어야 한다.
- 예를들어, https://www.naver.com/robots.txt에 접속하면 robots.txt의 내용은 다음과 같다.
```
User-agent:검색봇 이름
Disallow:접근 설정
Crawl-delay:다음방문까지의 디레이(초)
```

### 예시
- 모든 봇을 허용
```
User-agent: *
Disallow: 
```

- 구글봇을 제외한 나머지는 차단
```
User-agent: Googlebot
Disallow:
User-agent: *
Disallow: /
```

- 모든 봇을 차단
```
User-agent: *
Disallow: / 
```
- 네이버 : https://www.naver.com/robots.txt
```
URL : https://www.naver.com/robots.txt 
User-agent: *
Disallow: /
Allow : /$ 
```

- 구글 : https://google.com/robots.txt
```
User-agent: *
Disallow: /search
Allow: /search/about
Allow: /search/static
Allow: /search/howsearchworks
Disallow: /sdch
Disallow: /groups
Disallow: /index.html?
Disallow: /?
Allow: /?hl=
Disallow: /?hl=*&
Allow: /?hl=*&gws_rd=ssl$
Disallow: /?hl=*&*&gws_rd=ssl
Allow: /?gws_rd=ssl$
Allow: /?pt1=true$
Disallow: /imgres
Disallow: /u/
Disallow: /preferences
Disallow: /setprefs
Disallow: /default
Disallow: /m?
Disallow: /m/
Allow:    /m/finance
Disallow: /wml?
Disallow: /wml/?
Disallow: /wml/search?
Disallow: /xhtml?
Disallow: /xhtml/?
Disallow: /xhtml/search?
Disallow: /xml?
Disallow: /imode?
Disallow: /imode/?
Disallow: /imode/search?
Disallow: /jsky?
Disallow: /jsky/?
Disallow: /jsky/search?
Disallow: /pda?
Disallow: /pda/?
Disallow: /pda/search?
Disallow: /sprint_xhtml
Disallow: /sprint_wml
Disallow: /pqa
Disallow: /palm
Disallow: /gwt/
Disallow: /purchases
Disallow: /local?
Disallow: /local_url
Disallow: /shihui?
Disallow: /shihui/
Disallow: /products?
Disallow: /product_
Disallow: /products_
Disallow: /products;
Disallow: /print
Disallow: /books/
Disallow: /bkshp?*q=*
Disallow: /books?*q=*
Disallow: /books?*output=*
Disallow: /books?*pg=*
Disallow: /books?*jtp=*
Disallow: /books?*jscmd=*
Disallow: /books?*buy=*
Disallow: /books?*zoom=*
Allow: /books?*q=related:*
Allow: /books?*q=editions:*
Allow: /books?*q=subject:*
Allow: /books/about
Allow: /booksrightsholders
Allow: /books?*zoom=1*
Allow: /books?*zoom=5*
Allow: /books/content?*zoom=1*
Allow: /books/content?*zoom=5*
Disallow: /ebooks/
Disallow: /ebooks?*q=*
Disallow: /ebooks?*output=*
Disallow: /ebooks?*pg=*
Disallow: /ebooks?*jscmd=*
Disallow: /ebooks?*buy=*
Disallow: /ebooks?*zoom=*
Allow: /ebooks?*q=related:*
Allow: /ebooks?*q=editions:*
Allow: /ebooks?*q=subject:*
Allow: /ebooks?*zoom=1*
Allow: /ebooks?*zoom=5*
Disallow: /patents?
Disallow: /patents/download/
Disallow: /patents/pdf/
Disallow: /patents/related/
Disallow: /scholar
Disallow: /citations?
Allow: /citations?user=
Disallow: /citations?*cstart=
Allow: /citations?view_op=new_profile
Allow: /citations?view_op=top_venues
Allow: /scholar_share
Disallow: /s?
Allow: /maps?*output=classic*
Allow: /maps?*file=
Allow: /maps/d/
Disallow: /maps?
Disallow: /mapstt?
Disallow: /mapslt?
Disallow: /maps/stk/
Disallow: /maps/br?
Disallow: /mapabcpoi?
Disallow: /maphp?
Disallow: /mapprint?
Disallow: /maps/api/js/
Allow: /maps/api/js
Disallow: /maps/api/place/js/
Disallow: /maps/api/staticmap
Disallow: /maps/api/streetview
Disallow: /maps/_/sw/manifest.json
Disallow: /mld?
Disallow: /staticmap?
Disallow: /maps/preview
Disallow: /maps/place
Disallow: /maps/timeline/
Disallow: /help/maps/streetview/partners/welcome/
Disallow: /help/maps/indoormaps/partners/
Disallow: /lochp?
Disallow: /center
Disallow: /ie?
Disallow: /blogsearch/
Disallow: /blogsearch_feeds
Disallow: /advanced_blog_search
Disallow: /uds/
Disallow: /chart?
Disallow: /transit?
Allow:    /calendar$
Allow:    /calendar/about/
Disallow: /calendar/
Disallow: /cl2/feeds/
Disallow: /cl2/ical/
Disallow: /coop/directory
Disallow: /coop/manage
Disallow: /trends?
Disallow: /trends/music?
Disallow: /trends/hottrends?
Disallow: /trends/viz?
Disallow: /trends/embed.js?
Disallow: /trends/fetchComponent?
Disallow: /trends/beta
Disallow: /trends/topics
Disallow: /musica
Disallow: /musicad
Disallow: /musicas
Disallow: /musicl
Disallow: /musics
Disallow: /musicsearch
Disallow: /musicsp
Disallow: /musiclp
Disallow: /urchin_test/
Disallow: /movies?
Disallow: /wapsearch?
Allow: /safebrowsing/diagnostic
Allow: /safebrowsing/report_badware/
Allow: /safebrowsing/report_error/
Allow: /safebrowsing/report_phish/
Disallow: /reviews/search?
Disallow: /orkut/albums
Disallow: /cbk
Allow: /cbk?output=tile&cb_client=maps_sv
Disallow: /recharge/dashboard/car
Disallow: /recharge/dashboard/static/
Disallow: /profiles/me
Allow: /profiles
Disallow: /s2/profiles/me
Allow: /s2/profiles
Allow: /s2/oz
Allow: /s2/photos
Allow: /s2/search/social
Allow: /s2/static
Disallow: /s2
Disallow: /transconsole/portal/
Disallow: /gcc/
Disallow: /aclk
Disallow: /cse?
Disallow: /cse/home
Disallow: /cse/panel
Disallow: /cse/manage
Disallow: /tbproxy/
Disallow: /imesync/
Disallow: /shenghuo/search?
Disallow: /support/forum/search?
Disallow: /reviews/polls/
Disallow: /hosted/images/
Disallow: /ppob/?
Disallow: /ppob?
Disallow: /accounts/ClientLogin
Disallow: /accounts/ClientAuth
Disallow: /accounts/o8
Allow: /accounts/o8/id
Disallow: /topicsearch?q=
Disallow: /xfx7/
Disallow: /squared/api
Disallow: /squared/search
Disallow: /squared/table
Disallow: /qnasearch?
Disallow: /app/updates
Disallow: /sidewiki/entry/
Disallow: /quality_form?
Disallow: /labs/popgadget/search
Disallow: /buzz/post
Disallow: /compressiontest/
Disallow: /analytics/feeds/
Disallow: /analytics/partners/comments/
Disallow: /analytics/portal/
Disallow: /analytics/uploads/
Allow: /alerts/manage
Allow: /alerts/remove
Disallow: /alerts/
Allow: /alerts/$
Disallow: /ads/search?
Disallow: /ads/plan/action_plan?
Disallow: /ads/plan/api/
Disallow: /ads/hotels/partners
Disallow: /phone/compare/?
Disallow: /travel/clk
Disallow: /travel/hotelier/terms/
Disallow: /hotelfinder/rpc
Disallow: /hotels/rpc
Disallow: /commercesearch/services/
Disallow: /evaluation/
Disallow: /chrome/browser/mobile/tour
Disallow: /compare/*/apply*
Disallow: /forms/perks/
Disallow: /shopping/suppliers/search
Disallow: /ct/
Disallow: /edu/cs4hs/
Disallow: /trustedstores/s/
Disallow: /trustedstores/tm2
Disallow: /trustedstores/verify
Disallow: /adwords/proposal
Disallow: /shopping/product/
Disallow: /shopping/seller
Disallow: /shopping/ratings/account/metrics
Disallow: /shopping/reviewer
Disallow: /about/careers/applications/
Disallow: /landing/signout.html
Disallow: /webmasters/sitemaps/ping?
Disallow: /ping?
Disallow: /gallery/
Disallow: /landing/now/ontap/
Allow: /searchhistory/
Allow: /maps/reserve
Allow: /maps/reserve/partners
Disallow: /maps/reserve/api/
Disallow: /maps/reserve/search
Disallow: /maps/reserve/bookings
Disallow: /maps/reserve/settings
Disallow: /maps/reserve/manage
Disallow: /maps/reserve/payment
Disallow: /maps/reserve/receipt
Disallow: /maps/reserve/sellersignup
Disallow: /maps/reserve/payments
Disallow: /maps/reserve/feedback
Disallow: /maps/reserve/terms
Disallow: /maps/reserve/m/
Disallow: /maps/reserve/b/
Disallow: /maps/reserve/partner-dashboard
Disallow: /about/views/
Disallow: /intl/*/about/views/
Disallow: /local/dining/
Disallow: /local/place/products/
Disallow: /local/place/reviews/
Disallow: /local/place/rap/
Disallow: /local/tab/
Allow: /finance
Allow: /js/

# AdsBot
User-agent: AdsBot-Google
Disallow: /maps/api/js/
Allow: /maps/api/js
Disallow: /maps/api/place/js/
Disallow: /maps/api/staticmap
Disallow: /maps/api/streetview

# Certain social media sites are whitelisted to allow crawlers to access page markup when links to google.com/imgres* are shared. To learn more, please contact images-robots-whitelist@google.com.
User-agent: Twitterbot
Allow: /imgres

User-agent: facebookexternalhit
Allow: /imgres

Sitemap: https://www.google.com/sitemap.xml
```