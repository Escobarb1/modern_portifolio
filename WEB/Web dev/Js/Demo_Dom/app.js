document.addEventListener("DOMContentLoaded", function(){
    
    const list = document.querySelector("#movie-list ul");
    const forms = document.forms;

    //delete movie
    list.addEventListener("click", (e)=>{
        if(e.target.className == 'delete'){
            const li = e.target.parentElement;
            li.parentNode.removeChild(li);      
        }
    });

    //add movie
    const addForm = forms["add movie"];
    addForm.addEventListener('submit', function(e){     
        e.preventDefault();


        //creating elements
        const value = addForm.querySelector('input[type="text"]').value;
        const li = document.createElement("li");
        const movieName = document.createElement("span");
        const deleteBin = document.createElement("span");

    
        //add text content
        movieName.textContent = value;
        deleteBin.textContent = "delete";

        //add classes
        movieName.classList.add('name');
        deleteBin.classList.add("delete");
    
        //append to DOM
        li.appendChild(movieName);
        li.appendChild(deleteBin);
        list.appendChild(li);
    });

    })
