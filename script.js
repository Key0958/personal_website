showMessage
function showMessage() { 
    alert("Hello! Welcome to my website."); 
}

function displayGreeting(){    
    let name= document.getElementById("nameInput").value;
    document.getElementById("greeting").innerHTML ="Hello, " +name + "! Welcome to my website!";
}

checkAge()
function checkAge() {
    const age =prompt("Enter your real age");
    if (age>=18){
      alert("You're an adult!")
    } else{
      alert("You're still a kid!")
    }
}

function changeBgColor() {
    document.body.style.backgroundColor = "lightblue";
}

changeBackgroundColor()
function changeBackgroundColor() {
    const color = prompt("Enter you favorite color");
    document.body.style.backgroundColor = color;
}


const fontsize = prompt("Enter the font size that you want");
document.getElementById("heading").style.fontSize = fontSize;

function favorite() {
    let msg = document.getElementById("favoriteMessage");
    msg.innerText = "You like this!";
}

function unfavorite() {
    let msg = document.getElementById("favoriteMessage");
    msg.innerText = "";
}