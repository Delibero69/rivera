



document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems);
  });

const elemsDropdown = document.querySelectorAll(".dropdown-trigger");
const instancesDropdown = M.Dropdown.init(elemsDropdown,{
    coverTrigger:false
});

// let btn = document.getElementById('navbar1')
// btn.onmouseout = () =>{
//   btn.style.color ='red'
// }
 
// document.getElementById("navbar1").style.color = "red";
