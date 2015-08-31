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
        p {text-align:center;}
        img.displayed {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 66%;
        }
        textarea.displayed {
            display: block;
            color: #AAAAAA;
            margin-left: auto;
            margin-right: auto;
            max-width: 66%;
        }
        div.center {
            align: middle;
        }
        </style>
    </head>
    <body>
        <br><br>
        <!-- <p><a href="javascript:window.location.reload();">Reload</a><p>-->
        <p><a href={{current_url}}>Shuffle</a><p>
        <br>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt="{{text}}" align="middle"/>
            <br>
            <p><b>Share</b>
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
        </div>
    </body>
</html>
