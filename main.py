
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8080

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Only For My Emu ❤️</title>

<style>
*{margin:0;padding:0;box-sizing:border-box}

body{
background:linear-gradient(145deg,#250019,#650039,#c21870);
font-family:Georgia,serif;
color:white;
min-height:100vh;
overflow-x:hidden;
}

.hearts span{
position:fixed;
bottom:-50px;
font-size:22px;
animation:float 9s linear infinite;
opacity:.7;
z-index:0;
}

@keyframes float{
0%{transform:translateY(0) rotate(0);opacity:0}
20%{opacity:.8}
100%{transform:translateY(-110vh) rotate(360deg);opacity:0}
}

.container{
position:relative;
z-index:2;
width:92%;
max-width:480px;
margin:35px auto;
padding:25px 19px;
border:1px solid #ff9acb66;
border-radius:28px;
background:rgba(255,255,255,.09);
backdrop-filter:blur(15px);
box-shadow:0 0 35px #ff3e9b35;
text-align:center;
}

.top{
color:#ffafd5;
letter-spacing:4px;
font-size:11px;
margin-bottom:20px;
}

h1{
font-size:35px;
color:#ffb9d9;
text-shadow:0 0 20px #ff3d9b;
margin-bottom:10px;
}

.subtitle{
font-size:14px;
color:#ffd5e8;
margin-bottom:23px;
}

.photo{
width:100%;
max-height:340px;
object-fit:cover;
border-radius:20px;
border:2px solid #ffb1d4;
box-shadow:0 0 25px #ff4b9d55;
margin-bottom:24px;
}

.heart{
font-size:45px;
animation:pulse 1.5s infinite;
}

@keyframes pulse{
50%{transform:scale(1.2)}
}

h2{
color:#ffafd4;
font-size:25px;
margin:15px 0;
}

.letter{
text-align:left;
line-height:1.9;
font-size:15px;
color:#fff0f7;
padding:15px 5px;
}

.letter p{margin-bottom:17px}

.highlight{
color:#ffb2d7;
font-weight:bold;
}

.time{
background:#ffffff12;
border:1px solid #ff9acb66;
border-radius:18px;
padding:17px;
margin:20px 0;
}

.time h3{
color:#ffb2d7;
margin-bottom:10px;
}

.time p{
font-size:17px;
line-height:2;
}

.divider{
height:1px;
background:#ffafd455;
margin:22px 0;
}

.poetry{
color:#ffc1df;
font-style:italic;
line-height:2;
font-size:17px;
padding:12px;
}

button{
background:linear-gradient(90deg,#ff3e96,#ff83bd);
border:none;
border-radius:30px;
padding:15px 25px;
color:white;
font-size:15px;
font-weight:bold;
margin:15px 0;
box-shadow:0 0 20px #ff3e9666;
cursor:pointer;
}

#ending{
display:none;
font-size:19px;
line-height:2;
color:#ffc4df;
margin:20px 0;
}

.footer{
font-size:12px;
color:#ffb8d9;
margin-top:25px;
letter-spacing:2px;
}

</style>
</head>

<body>

<div class="hearts" id="hearts"></div>

<div class="container">

<div class="top">A LITTLE WORLD MADE ONLY FOR YOU 🎀</div>

<div class="heart">💗</div>

<h1>My Emu Ji</h1>
<div class="subtitle">Someone is really sorry today 🥺</div>

<img class="photo"
src="https://i.postimg.cc/RhvySnyW/Screenshot-20261118-231129.png"
alt="My Emu">

<h2>Ek Baat Suno Na Emu ❤️</h2>

<div class="letter">

<p>
Hey My Emu Ji 🥺❤️
</p>

<p>
Mujhe pata hai tumne mujhe <span class="highlight">7:45</span> pe aane ko kaha tha aur main <span class="highlight">9 baje</span> aaya
</p>

<p>
Main doston ke saath tha aur waqt ka khayal nahi rakha lekin iska matlab ye bilkul nahi ke tumhari baat mere liye important nahi thi
</p>

<p>
Emu mujhe samajhna chahiye tha ke tum mera wait kar rahi hogi aur maine tumhe wait karwaya
</p>

<p>
Main apni galti ko justify nahi karunga na hi koi bahana banaunga
Mujhe bas dil se sorry kehna hai
</p>

<p>
Tumhara waqt bhi important hai aur tumhari feelings bhi
Mujhe pehle hi tumhe inform kar dena chahiye tha ke main late ho raha hoon
</p>

<p>
I am really sorry meri Emu 🥺
Main promise karta hoon ke agli baar tumhe aise wait nahi karwaunga aur agar kabhi late hua toh pehle bata dunga
</p>

<p>
Please meri is galti ko maaf kar dena
Main chahta hoon ke tum mujhse naraz hone ke bajaye mujhse khul kar apni baat keh sako
</p>

<p class="highlight">
Tum mere liye important ho Emu aur tumhari respect aur waqt dono ki qadar karni chahiye mujhe ❤️
</p>

</div>

<div class="time">
<h3>That Little Mistake ⏰</h3>
<p>💗 You said: 7:45 PM</p>
<p>🥺 I arrived: 9:00 PM</p>
<p>❤️ My apology: From my heart</p>
</div>

<div class="divider"></div>

<div class="poetry">
Tum naraz ho toh dil udaas rehta hai<br>
Tumhari khushi se hi mera din khaas rehta hai<br>
Galti meri thi toh maafi bhi meri hai<br>
Bas tumhari muskurahat ka intezar rehta hai ❤️
</div>

<div class="divider"></div>

<h2>One Last Thing 🥺</h2>

<p style="line-height:1.9;color:#ffe0ef">
Main perfect nahi hoon Emu<br>
Mujhse galtiyan hoti hain<br>
Lekin main apni galti samajh kar behtar ban sakta hoon
</p>

<button onclick="showLove()">
Tap Here My Emu ❤️
</button>

<div id="ending">
I AM REALLY SORRY EMU 🥺💗
<br>
Tumhara Faiizi ❤️
<br>
I LOVE YOU SO MUCH 🧸
</div>

<div class="footer">
MADE WITH LOVE BY FAIIZI
</div>

</div>

<script>
const heartBox=document.getElementById("hearts");

const symbols=["❤️","💗","💕","💖","🧸","🎀"];

for(let i=0;i<25;i++){
let s=document.createElement("span");
s.innerHTML=symbols[Math.floor(Math.random()*symbols.length)];
s.style.left=Math.random()*100+"%";
s.style.animationDuration=(5+Math.random()*8)+"s";
s.style.animationDelay=Math.random()*8+"s";
heartBox.appendChild(s);
}

function showLove(){
document.getElementById("ending").style.display="block";
}
</script>

</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

server=ThreadingHTTPServer(("0.0.0.0",PORT),Handler)

print("\n❤️ FAIZI X EMU APOLOGY WEBSITE ❤️")
print("Website: http://127.0.0.1:8080")
print("Server Started Successfully!\n")

server.serve_forever()
