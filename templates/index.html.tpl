<html>
    <head>
        <style>
        h2 {
            text-align:center;
            font-family: "Arial",  arial, sans-serif;
        }
        a:link {
            color: #AAAAAA;
            font-family: "Arial",  arial, sans-serif;
            text-decoration: none;
        }
        a:visited {
            color: #AAAAAA;
            font-family: "Arial",  arial, sans-serif;
            text-decoration: none;
        }
        a:hover {
            color: #AAAADD;
            font-family: "Arial",  arial, sans-serif;
            text-decoration: none;
        }
        a:active {
            color: #AAAAFF;
            font-family: "Arial",  arial, sans-serif;
            text-decoration: none;
        }
        b {
            text-align:center;
            font-family: "Arial",  arial, sans-serif;
            color: #AAAAAA;
        }
        p {
            text-align:center;
            font-family: "Arial",  arial, sans-serif;
            color: #AAAAAA;
        }
        img.displayed {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 66%;
            text-align: center;
        }
        textarea.displayed {
            display: block;
            color: #AAAAAA;
            margin-left: auto;
            margin-right: auto;
            max-width: 66%;
        }
        button.plain {
            background: none;
            border: none;
            cursor: pointer;
            color: #AAAAAA;
            font-family: "Arial",  arial, sans-serif;
            font-size: 1em;
            margin: 0;
            padding: 0;
        }
        button.plain:hover {
            color: #AAAADD;
        }
        div.center {
            align: middle;
        }
        </style>
        <script language="JavaScript">
            function anim() {
                var x = document.getElementById("animatedGifs");
                if(x.checked){
                    return 'a=1&';
                }
                return "";
            }   
            function unsf() {
                var x = document.getElementById("unsafeContent");
                if(x.checked){
                    return 'u=1&';
                }
                return "";
            }  
            function rndmr() {
                var x = document.getElementById("randomNouns");
                if(x.checked){
                    return 'r=1';
                }
                return "";
            }  
            function shufflelink() {
                window.location.href =
                  "{{current_url}}" + "/?" + anim() + unsf() + rndmr();
            }
        </script>
            
    </head>
    <body>
        <br><br>
        <p><button class="plain" onClick="shufflelink();" >Shuffle</button><p>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt=" Oh, Google. Really? No images for {{text}}?" align="middle"/>
            <br>
            <p>
            <b>Share</b>&nbsp
            <a href="https://www.facebook.com/sharer/sharer.php?u={{quotelink}}">
            <img src="{{baseurl}}/static/images/facebook_gray_small.jpg" alt="fb" 
                onmouseover="this.src='{{baseurl}}/static/images/facebook_blue_small.jpg'" 
                onmouseout="this.src='{{baseurl}}/static/images/facebook_gray_small.jpg'"/></a>
            <a href="https://twitter.com/home?status={{quotelink}}">
            <img src="{{baseurl}}/static/images/twitter_gray_small.jpg" alt="twitter"
                onmouseover="this.src='{{baseurl}}/static/images/twitter_blue_small.jpg'" 
                onmouseout="this.src='{{baseurl}}/static/images/twitter_gray_small.jpg'"/></a>
            <a href="https://plus.google.com/share?url={{quotelink}}">
            <img src="{{baseurl}}/static/images/googleplus_gray_small.jpg" alt="gplus"
                onmouseover="this.src='{{baseurl}}/static/images/googleplus_red_small.jpg'"
                onmouseout="this.src='{{baseurl}}/static/images/googleplus_gray_small.jpg'"/></a>
            </p>
            <textarea class="displayed" rows="4" cols="50">{{permalink}}</textarea> 
            <p>
            <input id="animatedGifs" type="checkbox" name="a" {{animchecked}} />animated&nbsp
            <input id="unsafeContent" type="checkbox" name="u" {{unsfchecked}}/>not easily offended&nbsp
            <input id="randomNouns" type="checkbox" name="r" {{randchecked}}/>randomer&nbsp
            </p>
        </div>
    </body>
</html>
