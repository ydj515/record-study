<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="captcha.AudioCaptCha, nl.captcha.Captcha"%>
<%

    String getAnswer = request.getParameter("ans");

    if ("y".equals(getAnswer)) {
        Captcha captcha = (Captcha) session.getAttribute(Captcha.NAME);
        
        getAnswer = captcha.getAnswer();
        out.print(getAnswer);

        return;
    }

    out.clear();

    pageContext.pushBody();

    new AudioCaptCha().getAudioCaptCha(request, response, getAnswer);
%>