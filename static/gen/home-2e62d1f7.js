const closeBtns=document.getElementsByClassName("flash-close")
let seconds=2000
for(let i=0;i<closeBtns.length;i++){const btn=closeBtns[i]
setTimeout(()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
btn.parentElement.remove()},seconds)
seconds=seconds*2
btn.onclick=()=>{btn.onclick=()=>{}
btn.parentElement.classList.add("close")
setTimeout(()=>{btn.parentElement.remove()},1000)}}