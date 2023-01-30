var userIds = "" // userids separated by a comma
var authToken = "" // fill in your auth token

var userIdArray = userIds.split(",");
var index = 0;
function doSomething(index) {
    if (index === userIdArray.length) {
        return;
    }
    var http = new XMLHttpRequest();
    var url = "https://prod.tritondive.co/apis/follow/v0/follow";
    http.open("POST", url, true);

    http.setRequestHeader("Content-type", "application/json; charset=utf-8");
    http.setRequestHeader("Authorization", authToken);
    http.setRequestHeader("Accept-Language", "en");

    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
        }
    }
    http.send(JSON.stringify({userId:userIdArray[index]}));

    setTimeout(function () {
        doSomething(index+1);
    }, 1000);
}

doSomething(0);
