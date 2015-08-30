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
        <p><a href="javascript:window.location.reload();">Reload</a><p>
        <br>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt="{{text}}" align="middle"/>
            <p><b>Share</b></p>
             <textarea class="displayed" rows="4" cols="50">{{permalink}}</textarea> 
        </div>
    </body>
</html>
