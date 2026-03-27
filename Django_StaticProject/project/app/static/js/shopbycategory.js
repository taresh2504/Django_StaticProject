document.querySelectorAll(".filter-btn").forEach(btn => {

    btn.addEventListener("click", function(e){

        const dropdown = this.nextElementSibling
        const arrow = this.querySelector("#arrow")

        document.querySelectorAll(".dropdown").forEach(d => {
            if(d !== dropdown){
                d.style.display = "none"
            }
        })

        document.querySelectorAll("#arrow").forEach(a=>{
            if(a !== arrow){
                a.classList.remove("rotate")
            }
        })

        if(dropdown.style.display === "block"){
            dropdown.style.display = "none"
            arrow.classList.remove("rotate")
        }else{
            dropdown.style.display = "block"
            arrow.classList.add("rotate")
        }

        e.stopPropagation()
    })
})

document.addEventListener("click", ()=>{
    document.querySelectorAll(".dropdown").forEach(d=>{
        d.style.display="none"
    })

    document.querySelectorAll(".arrow").forEach(a=>{
        a.classList.remove("rotate")
    })
})