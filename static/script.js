function addMovie() {

    var movieTitle = document.getElementById("inputTitle").value;
    var movieYear = document.getElementById("inputYear").value;
    var movieActors = document.getElementById("inputActors").value;

    if (movieTitle ==""){
        alert("Title cannot be empty");
        return;
    }

    if (movieYear ==""){
        alert("Year cannot be empty");
        return;
    }

    if (movieActors==""){
        alert("Actors cannot be empty");
        return;
    }

    var li = document.createElement("li");
    li.innerHTML = "<input type='checkbox'> " + movieTitle + ", " + movieYear + ", " + movieActors;
    document.getElementById("moviesList").appendChild(li)

}

function deleteMovie() {
    var checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked");
    checkedBoxes.forEach(removalFunction);
        
    function removalFunction(item,index)
    {
        document.getElementById("moviesList").removeChild(checkedBoxes[index].parentNode);
    }
    
}