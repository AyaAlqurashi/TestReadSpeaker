from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ReadSpeaker - Arabic Support</title>

    <!-- ReadSpeaker Script -->
    <script src="//cdn-me.readspeaker.com/script/9023/webReader/webReader.js?pids=wr&notools=1" type="text/javascript" id="rs_req_Init"></script>

    <!-- ReadSpeaker Custom Styles -->
    <style>
        body {
            font-family: 'Arial', sans-serif;
            direction: rtl;
            text-align: right;
        }
        .rs_splitbutton .rsbtn_exp .rsbtn_exp_inner button.rsbtn_pause.rsbtn_player_item {
            padding-left: 11px !important;
        }
        .rs_splitbutton .rsbtn_exp .rsbtn_exp_inner .rsbtn_volume,
        .rs_splitbutton .rsbtn_exp .rsbtn_exp_inner .rsbtn_speed {
            display: none !important;
        }
    </style>
</head>
<body>

    <h1>مرحبًا بك في قارئ النصوص ReadSpeaker</h1>

    <!-- ReadSpeaker Player -->
    <div id="xp1" class="rs_preserve rs_skip rs_addtools rs_splitbutton rs_exp"></div>

    <!-- Arabic Text to Read -->
    <p id="read_content">هذه فقرة تجريبية ليتم قراءتها بصوت عالٍ عند تفعيل القارئ.</p>

    <!-- ReadSpeaker Activation Link -->
    <a href="//app-me.readspeaker.com/cgi-bin/rsent?customerid=9023&lang=ar_ar&voice=Yasmin&readid=read_content&url="
       onclick="return readpage(this.href, 'xp1');"
       data-target="xp1">
       استمع إلى النص
    </a>

</body>
</html>

    """)

if __name__ == '__main__':
    app.run(debug=True)
