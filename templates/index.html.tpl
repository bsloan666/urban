<html>
    <head>
        <style>
        html,body {
            margin: 0; 
            padding: 0;
        }
        img.banner {
            margin-left: auto;
            margin-right: auto;
            max-width: 100%;
        }
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
            function halloffame() {
                window.location.href =
                  "{{current_url}}" + "/?hof=1";
            }
        </script>
            
    </head>
    <body>
        <img src="{{baseurl}}/static/images/urbanator_v002.png" class="banner" margin="0" padding="0" alt="banner logo"/>
        <br><br>
        <p><button class="plain" onClick="shufflelink();" >Shuffle</button></p>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt=" Oh, Google. Really? No images for {{text}}?" align="middle"/>
            <br>
            <p>
            <input id="animatedGifs" type="checkbox" name="a" {{animchecked}} />animated&nbsp
            <input id="unsafeContent" type="checkbox" name="u" {{unsfchecked}}/>not easily offended&nbsp
            <input id="randomNouns" type="checkbox" name="r" {{randchecked}}/>randomer&nbsp
            </p>
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
            <p><button class="plain" onClick="halloffame();" >Hall of Fame</button></p>
        </div>
        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <!-- urbanator_adsense_unit_v001 -->
        <ins class="adsbygoogle"
        style="display:inline-block;width:728px;height:90px"
        data-ad-client="ca-pub-7427143071084245"
        data-ad-slot="5052921614"></ins>
        <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </body>
</html>
