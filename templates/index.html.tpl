<html>
    <head>
        <style>
        h2 {
            text-align:center;
            font-face: arial;
        }
        p {text-align:center;}
        img.displayed {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 25%;
        }
        div.center {
            align: middle;
            font-size: tiny;
        }
        </style>
    </head>
    <body>
        <br><br><br><br><br>
        <h2>{{ text }}</h2>
        <br>
        <div id="center">
            <img class="displayed" src="{{img}}" alt="{{text}}" align="middle"/>
            <p><a href="/?s={{seed}}">Save</a></p>
        </div>
    </body>
</html>
