const closeBtns=document.getElementsByClassName("flash-close")
let seconds=3000
for(let i=0;i<closeBtns.length;i++){const btn=closeBtns[i]
if(!btn.parentElement.classList.contains("danger")){setTimeout(()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
setTimeout(()=>{btn.parentElement.remove()},1000)},seconds)}
seconds+=1500
btn.onclick=()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
setTimeout(()=>{btn.parentElement.remove()},1000)}}