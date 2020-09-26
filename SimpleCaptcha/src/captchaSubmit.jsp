<%@page session="true" language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="nl.captcha.Captcha" %>
<%

    response.setHeader("Pragma-directive", "no-cache");
    response.setHeader("Cache-directive", "no-cache");
    response.setHeader("Pragma", "no-cache");
    response.setHeader("Cache-Control", "no-cache");
    response.setDateHeader("Expires",0);
    
    Captcha captcha = (Captcha) session.getAttribute(Captcha.NAME);
    String answer = request.getParameter("answer");

    if ( answer != null && !"".equals(answer) ) {
        if (captcha.isCorrect(answer)) {
            session.removeAttribute(Captcha.NAME);
            out.print("입력값이 일치합니다.");
        } else {
            out.print("입력값이 일치하지 않습니다.");
        }
    }
%>