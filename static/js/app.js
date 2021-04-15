let dropdown=document.getElementsByClassName('dropdown')
for(let i=0;i<dropdown.length; i++){
  dropdown[i].addEventListener('mouseover',()=>{
    dropdown[i].classList.add("open")
  })
  dropdown[i].addEventListener('mouseout',()=>{
    dropdown[i].classList.remove("open")
  })
}
