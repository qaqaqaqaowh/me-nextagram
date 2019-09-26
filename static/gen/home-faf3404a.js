const closeBtns=document.getElementsByClassName("flash-close")
let seconds=2000
for(let i=0;i<closeBtns.length;i++){const btn=closeBtns[i]
if(!btn.parentElement.classList.contains("danger")){setTimeout(()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
setTimeout(()=>{btn.parentElement.remove()},1000)},seconds)}
seconds+=1500
btn.onclick=()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
setTimeout(()=>{btn.parentElement.remove()},1000)}}
let body=document.body
let html=document.documentElement
setInterval(()=>{const chance=Math.random()
if(chance<0.5){console.log("NYAN")
const nyan=document.createElement("img")
nyan.src="/static/nyan.gif"
nyan.classList.add("nyan")
let height=Math.random()*Math.max(body.scrollHeight,body.offsetHeight,html.clientHeight,html.scrollHeight,html.offsetHeight);nyan.style.top=(height-200)+'px'
body.appendChild(nyan)
setTimeout(()=>{nyan.remove()},5000)}},10000)
const searchInput=document.getElementById("search")
let resArray=[]
searchInput.onkeydown=(e)=>{if(e.target.value){}}