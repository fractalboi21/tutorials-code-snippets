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

# Injecting jquery in html head tag using `javascript`.
 ```javascript
function inject() {
    let script = document.createElement("script");
    script.src = "https://code.jquery.com/jquery-3.6.0.slim.min.js";
    script.integrity = "sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=";
    script.crossOrigin = "anonymous"
}
inject()
 ```
 `minifed version` 
 ```javascript
 function inject(){let e=document.createElement("script");e.src="https://code.jquery.com/jquery-3.6.0.slim.min.js",e.integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=",e.crossOrigin="anonymous"}inject();
 ```
# Inject bootstrap using javascript `minified version`
```javascript
function injectBootstrap(){let t=document.createElement("link");t.href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",t.rel="stylesheet",t.integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",t.crossOrigin="anonymous";let s=document.createElement("script");s.src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js",s.integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM",s.crossOrigin="anonymous";let e=document.createElement("script");e.src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js",e.integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p",e.crossOrigin="anonymous";let n=document.createElement("script");n.src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js",n.integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF",n.crossOrigin="anonymous",document.head.appendChild(t),document.head.appendChild(s),document.head.appendChild(e),document.head.appendChild(n)} injectBootstrap()

```



# Online tools
- [JavaScript Minifier](https://javascript-minifier.com/)
- [Online JavaScript Beautifier](https://beautifier.io/)
