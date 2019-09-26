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
const autocomplete=document.getElementById("autocomplete")
let resArray=[]
let timeout=null
function visit(){window.location.pathname="/users/"+event.target.innerText}
searchInput.onkeydown=(e)=>{clearTimeout(timeout)
timeout=setTimeout(()=>{if(e.target.value){if(e.code=="Enter"){window.location.pathname="/users/"+resArray[0].username}else{let xhr=new XMLHttpRequest()
xhr.onreadystatechange=function(){if(this.readyState==4&&this.status==200){const data=JSON.parse(this.response)
if(data.length){let res=""
resArray=data
for(let i=0;i<resArray.length;i++){res+=`<div onclick="visit()"class="result"><img src='${data[i].image}'>${data[i].username}</div><hr>`}
autocomplete.innerHTML=res.slice(0,-4)
autocomplete.classList.remove("hidden")}else{autocomplete.classList.add("hidden")}}}
xhr.open("GET","/users/search"+`?name=${e.target.value}`,true)
xhr.send()}}else{autocomplete.classList.add("hidden")}},500)}
const requests=document.getElementById("requests")
requests.onclick=(e)=>{requests.classList.toggle("toggle")}
const reqButtons=document.getElementsByClassName("reqButtons")
for(let i=0;i<reqButtons.length;i++){reqButtons[i].onclick=(e)=>{e.stopPropagation()
e.preventDefault()
const userId=e.target.dataset.userid
let xhr=new XMLHttpRequest()
xhr.onreadystatechange=function(){if(this.readyState==4){e.target.parentElement.parentElement.remove()}}
if(e.target.innerHTML=="Accept"){xhr.open("POST",`/follows/accept/${userId}`,true)}else{xhr.open("POST",`/follows/delete/${userId}`,true)}
xhr.send()}}