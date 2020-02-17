var searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\
다스베이더 070-9999-9999 darth_vader@gmail.com\
princess leia 010 2454 3457 leia@gmail.com";

/* 아래 코드의 /와 /g가운데에 정규표현식을 넣으세요.
 * g는 global의 약자로, 정규표현식과 일치하는 모든 내용을 찾아오라는 옵션입니다.
 */
var regex = /\d/g;    // 여기에 정규표현식을 입력하세요.
console.log(searchTarget.match(regex));