/**
 * Created by Anonymous on 1/28/14.
 */

$(document).ready(function () {
//    function getCookie(name) {
//        var cookieValue = null;
//        if (document.cookie && document.cookie != '') {
//            var cookies = document.cookie.split(';');
//            for (var i = 0; i < cookies.length; i++) {
//                var cookie = jQuery.trim(cookies[i]);
//                // Does this cookie string begin with the name we want?
//
//                if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                    break;
//                }
//            }
//        }
//        return cookieValue;
//    }
//
//    $.ajaxSetup({
//        beforeSend: function (xhr, settings) {
//            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//                // Only send the token to relative URLs i.e. locally.
//                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//            }
//        }
//    });


    $("#sendComment").click(function () {
        var ajaxData = {
            category: 0,
            search: "",
            page: 1
        };

        var url = "http://127.0.0.1:80/MyShop/writeComment/";
        $.post(url,
            ajaxData,
            function (data, status) {
                alert("Data: " + "\nStatus: " + status);
            });


    });

});