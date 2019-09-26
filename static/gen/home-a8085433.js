const closeBtns=document.getElementsByClassName("flash-close")
for(let i=0;i<closeBtns.length;i++){const btn=closeBtns[i]
btn.onclick=()=>{btn.parentElement.classList.add("close")
setTimeout(()=>{btn.remove.parentElement.remove()},1000)}}