var oauth = require('oauth.js');

var urlLink = 'https://api.twitter.com/1.1/statuses/update.json';

var twitterStatus = "Sample tweet";

var oauth_consumer_key = "d6T0PcnqxxxxxxxxxxUB7Jok2f";
var consumerSecret = "NFbG1H7CGRxukJTPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxze02qH8";

var oauth_token = "306673734-RQanTkxxxxxxxxxxxxxxxxxxeH4NuqQ8Z";
var tokenSecret = "YnF5vpjclMMVWhuxxxxxxxxxxxxxxxl3xejqAu";

var nonce = oauth.nonce(32);
var ts = Math.floor(new Date().getTime() / 1000);
var timestamp = ts.toString();

var accessor = {
    "consumerSecret": consumerSecret,
    "tokenSecret": tokenSecret
};

var params = {
    "status": twitterStatus,
    "oauth_consumer_key": oauth_consumer_key,
    "oauth_nonce": nonce,
    "oauth_signature_method": "HMAC-SHA1",
    "oauth_timestamp": timestamp,
    "oauth_token": oauth_token,
    "oauth_version": "1.0"
};
var message = {
    "method": "POST",
    "action": urlLink,
    "parameters": params
};

//lets create signature
oauth.SignatureMethod.sign(message, accessor);
var normPar = oauth.SignatureMethod.normalizeParameters(message.parameters);
var baseString = oauth.SignatureMethod.getBaseString(message);
var sig = oauth.getParameter(message.parameters, "oauth_signature") + "=";
var encodedSig = oauth.percentEncode(sig); //finally you got oauth signature

$.ajax({
    url: urlLink,
    type: 'POST',
    data: {
        "status": twitterStatus
    },
    beforeSend: function(xhr){
        xhr.setRequestHeader("Authorization",'OAuth oauth_consumer_key="'+oauth_consumer_key+'",oauth_signature_method="HMAC-SHA1",oauth_timestamp="' + timestamp + '",oauth_nonce="' + nonce + '",oauth_version="1.0",oauth_token="'+oauth_token+'",oauth_signature="' + encodedSig + '"');  
   },
   success: function(data) { 
        alert("Tweeted!"); 
   },
   error:function(exception){
       alert("Exeption:"+exception);
    }
  });