# Web extentions

borderify


## some useful javascript code snippets
- check if manifest key mandatory or not
```javascript
var mandatory = document.getElementsByClassName("fullwidth-table")[0].childNodes[1].childNodes[3].childNodes[3].childNodes[0].textContent.toLowerCase();
```

- Open URL in same window and in same tab
```javascript
window.location.replace("https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name");
```
- Addblocker for only https://www.w3schools.com/
```javascript
document.getElementById("mainLeaderboard").remove()
document.getElementById("google_ads_iframe_/22152718/sws-hb//w3schools.com//main_leaderboard_0__container__").remove()
```

- Inject jquery in html head tag using javascript.
 ```javascript
 var script = document.createElement("script");
 script.src = "https://code.jquery.com/jquery-3.6.0.slim.min.js";
 script.integrity = "sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=";
 script.crossOrigin = "anonymous"
 ```
