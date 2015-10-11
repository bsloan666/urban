<html>
    <head>
        <title>Urbanator: {{ text }} </title>
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
            max-height: 40%;
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
            function shufflelink() {
                window.location.href =
                  "{{current_url}}" + "/"
            }
        </script>

    </head>
    <body>
        <img src="/static/images/urbanator_v002.png" class="banner" margin="0" padding="0" alt="banner logo"/>
        <br><br>
        <p><a href="/" class="plain" >Shuffle</button></p>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt="Photograph depicting {{text}}?" align="middle"/>
            <br>
            <p>
            <b>Share</b>&nbsp
            <a href="https://www.facebook.com/sharer/sharer.php?u={{quotelink}}">
            <img src="/static/images/facebook_gray_small.jpg" alt="fb"
                onmouseover="this.src='/static/images/facebook_blue_small.jpg'"
                onmouseout="this.src='/static/images/facebook_gray_small.jpg'"/></a>
            <a href="https://twitter.com/home?status={{quotelink}}">
            <img src="/static/images/twitter_gray_small.jpg" alt="twitter"
                onmouseover="this.src='/static/images/twitter_blue_small.jpg'"
                onmouseout="this.src='/static/images/twitter_gray_small.jpg'"/></a>
            <a href="https://plus.google.com/share?url={{quotelink}}">
            <img src="/static/images/googleplus_gray_small.jpg" alt="gplus"
                onmouseover="this.src='/static/images/googleplus_red_small.jpg'"
                onmouseout="this.src='/static/images/googleplus_gray_small.jpg'"/></a>
            </p>
            <textarea class="displayed" rows="4" cols="50">{{permalink}}</textarea>
            <p><a href="/hall-of-fame" class="plain">Hall of Fame</a></p>
            <div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 'urbanator';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
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
