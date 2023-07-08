var SimpleCaptchaManager = function(options) {
    this.options = _.cloneDeep(options);
    this.$refreshBtn = $("#captcha-refresh-btn");
    this.$captcha = $("#input-captcha");
    this.$captchaImage = $("#captcha-img");

    this.initEvent();
}

SimpleCaptchaManager.prototype.certificateCaptcha = function() {
    var self = this;
    var data = {
        inputCaptcha: this.$captcha.val(),
    };
    var result = false;

    $.ajax({
        url: '/captcha/validCaptcha',
        type: 'POST',
        data: JSON.stringify(data),
        async: false,
        success: function (res) {
            if (!res.data.isCorrect) {
                alert(res.data.message);
            } else {
                result = true;
            }
        }, error: function (err) {
            alert('보안 문자 인증 중 오류가 발생하였습니다. 잠시 후 다시 시도해 주세요.');
            return false;
        }
    });

    return result;
}

SimpleCaptchaManager.prototype.initEvent = function() {
    var self = this;

    self.$refreshBtn.on('click', function(e) {
        document.getElementById("captcha-img").src = "/captcha?" + Math.random();
    });
}