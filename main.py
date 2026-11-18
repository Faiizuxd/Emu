
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 1000

PHOTO = "https://i.postimg.cc/RhvySnyW/Screenshot-20261118-231129.png"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Only For My Emu ❤️</title>

<style>
*{margin:0;padding:0;box-sizing:border-box}

body{
 min-height:100vh;
 overflow-x:hidden;
 text-align:center;
 font-family:'Segoe UI',Arial,sans-serif;
 color:#994365;
 background:linear-gradient(135deg,#ffe3ee,#fff5f9,#ffd6e7);
}

.container{
 width:92%;
 max-width:500px;
 margin:28px auto;
 padding:12px;
}

.banner{
 padding:18px;
 background:linear-gradient(135deg,#ff9fc5,#ffd1e2);
 border:3px solid white;
 border-radius:28px;
 box-shadow:0 12px 32px #d96b9950;
 animation:appear 1.2s ease;
}

.banner img{
 width:100%;
 max-height:520px;
 object-fit:contain;
 background:#fff0f6;
 border-radius:20px;
 border:3px solid white;
}

.banner h1{
 color:white;
 font-size:29px;
 margin:17px 0 6px;
 text-shadow:0 2px 8px #bd4777;
}

.banner p{
 color:white;
 font-size:13px;
 letter-spacing:2px;
}

.card{
 margin-top:22px;
 padding:25px 20px;
 background:#ffffffdf;
 border:2px solid white;
 border-radius:25px;
 box-shadow:0 8px 25px #e78bb655;
 animation:appear 1.6s ease;
}

h2{
 color:#e34d8b;
 font-size:23px;
 margin-bottom:17px;
}

.message{
 font-size:15px;
 line-height:2;
 color:#82405e;
}

.poetry{
 margin-top:23px;
 padding:20px;
 background:#ffe6f0;
 border-radius:20px;
 line-height:2.1;
 font-style:italic;
 color:#b33970;
}

.signature{
 margin-top:25px;
 font-size:23px;
 color:#e34d8b;
 font-weight:bold;
}

.love{
 margin-top:18px;
 font-size:25px;
 color:#e83e83;
 animation:pulse 1.5s infinite;
}

.footer{
 margin:25px 0;
 font-size:13px;
 color:#b75a80;
 line-height:1.9;
}

.heart{
 position:fixed;
 bottom:-40px;
 font-size:22px;
 animation:float 7s linear forwards;
 opacity:.75;
 pointer-events:none;
 z-index:5;
}

@keyframes float{
 0%{transform:translateY(0) rotate(0);opacity:0}
 20%{opacity:1}
 100%{transform:translateY(-110vh) rotate(360deg);opacity:0}
}

@keyframes pulse{
 50%{transform:scale(1.07)}
}

@keyframes appear{
 from{opacity:0;transform:translateY(25px)}
 to{opacity:1;transform:translateY(0)}
}
</style>
</head>

<body>

<div class="container">

<section class="banner">

<img src="PHOTO_URL" alt="Emu">

<h1>Hey My Emu Ji! 🧸💗</h1>

<p>A LITTLE WORLD MADE ONLY FOR YOU 🎀</p>

</section>

<section class="card">

<h2>💌 A Message For You</h2>

<p class="message">

Hey Emu, I'm Faiizi ❤️

<br><br>

This little page is only for you.

<br><br>

I never thought I would fall in love with you this deeply. But as we started talking, getting to know each other, and understanding each other, something beautiful happened.

<br><br>

You understood me, and I tried to understand you. And somewhere along the way, you became someone incredibly special in my life.

<br><br>

I started falling for you, and now I love you more than words can ever explain.

<br><br>

I hope we always keep understanding and supporting each other. I want to stand by your side, listen to you, respect you, and share all the beautiful moments with you.

<br><br>

I want to keep choosing you, not just today, but through all the days ahead.

<br><br>

I love you so much, Emu. I swear, I'm falling in love with you more and more every day.

</p>

<div class="love">
I LOVE YOU EMU JI ❤️
</div>

<div class="poetry">

"You're not just a person in my life,<br>
You're a beautiful part of my story.<br>
Among all the moments I could choose,<br>
I'd choose you in every lifetime. 💗"

</div>

<div class="signature">
Apka Faiizi 🧸
</div>

</section>

<div class="footer">
Made With Love, Only For Emu Ji 🌷
<br>
A little page with a lot of love ❤️
</div>

</div>

<script>

const emojis=["❤️","💕","💗","🌸","💖","🎀"];

function createHeart(){

 const heart=document.createElement("div");

 heart.className="heart";

 heart.textContent=emojis[
 Math.floor(Math.random()*emojis.length)
 ];

 heart.style.left=Math.random()*100+"%";

 heart.style.animationDuration=
 (4+Math.random()*5)+"s";

 document.body.appendChild(heart);

 setTimeout(()=>heart.remove(),9000);
}

setInterval(createHeart,450);

</script>

</body>
</html>
"""

HTML = HTML.replace("PHOTO_URL", PHOTO)

class Website(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path not in ("/", "/index.html"):
            self.send_error(404)
            return

        content = HTML.encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.send_header(
            "Content-Length",
            str(len(content))
        )
        self.end_headers()

        self.wfile.write(content)

    def log_message(self, format, *args):
        print("[SERVER]", format % args)


if __name__ == "__main__":

    server = ThreadingHTTPServer(
        ("0.0.0.0", PORT),
        Website
    )

    print("\n💕 EMU LOVE WEBSITE STARTED")
    print("🌸 http://127.0.0.1:1000")
    print("🎀 Made by Faiizi")
    print("❤️ Press CTRL+C to stop\n")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nWebsite stopped!")
        server.server_close()
