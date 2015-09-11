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
    </head>
    <body>
        <br><br>
        <h2>Hall Of Fame</h2>
        <br>
        <div id="center">
            <br>
            <p>
            {{table}}
            </p>
        </div>
    </body>
</html>
