<html>
    <head>
        <title>Urbanator: Hall of Fame</title>
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
    </head>
    <body>
        <img src="{{baseurl}}/static/images/urbanator_v002.png" margin="0" padding="0" class="banner" alt="banner logo"/>
        <br>
        <h2>Hall of Fame</h2>
        <a href="/"><p style="text-align:center">Back to Shuffle</p></a>
        <div id="center">
            <br>
            <p>
            <table align="center" border="0" cellpadding="10">
              {% for fav_row in favorites|batch(3) %}
              <tr>
                {% for fav in fav_row %}
                <td align=center bgcolor="#FFFFFF">
                  <a href="{{fav['url']}}">
                    <b>{{fav['adj'][0]}} {{fav['noun'][0]}}</b><br/>
                    <p>
                      <img align=center height="128" src="{{fav['imgurl'][0]}}" alt="{{fav['adj'][0]}} {{fav['noun'][0]}}"/>
                    </p>
                    <br/><br/>
                  </a>
                </td>
                {% endfor %}
              </tr>
              {% endfor %}
            </table>
            </p>
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
