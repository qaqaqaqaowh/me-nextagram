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
const nyan=document.createElement("img")
nyan.src="/static/nyan.gif"
nyan.style.position="absolute"
nyan.style.zIndex=-1
nyan.style.height='100px'
let body=document.body
let html=document.documentElement
let height=Math.random()*Math.max(body.scrollHeight,body.offsetHeight,html.clientHeight,html.scrollHeight,html.offsetHeight);nyan.style.top=height+'px'
body.appendChild(nyan)