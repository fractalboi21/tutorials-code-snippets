function injectBootstrap() {
  
    let link = document.createElement("link");
    link.href = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css";
    link.rel = "stylesheet";
    link.integrity = "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC";
    link.crossOrigin = "anonymous";
  
    let script1 = document.createElement("script");
    script1.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js";
    script1.integrity = "sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM";
    script1.crossOrigin = "anonymous";
  
    let script2 = document.createElement("script");
    script2.src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js";
    script2.integrity = "sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p";
    script2.crossOrigin = "anonymous";
  
    let script3 = document.createElement("script");
    script3.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js";
    script3.integrity = "sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF";
    script3.crossOrigin = "anonymous";
  
    document.head.appendChild(link);
    document.head.appendChild(script1);
    document.head.appendChild(script2);
    document.head.appendChild(script3);
}
