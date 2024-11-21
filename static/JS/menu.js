
const handleMenu=()=>{
    const menu = document.getElementById('menu')
    if (menu.classList.contains('hidden')){
        menu.classList.remove('hidden')
        menu.classList.add('flex')
        console.log("menu mostrad")
    }
    else{
        menu.classList.add('hidden')
        console.log("menu escondido")
    }

};
