const handleMenu=()=>{
    const toggle = document.getElementById('menu-toggle')
    const menu = document.getElementById('menu')

    if (menu.classList.contains('hidden')){
        menu.classList.remove('hidden')
        menu.classList.add('flex')
        toggle.classList.remove('bg-sky-950')
        toggle.classList.add('bg-sky-600')
        console.log("menu mostrado")
    }
    else{
        menu.classList.add('hidden')
        toggle.classList.remove('bg-sky-600')
        toggle.classList.add('bg-sky-950')
        console.log("menu escondido")
    }
};
