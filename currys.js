const users = {'a':"i"}

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
 
    if (users[username] == password) {
        window.alert("login sucessfully")
        window.location = "cc.html"
    } 
    else {
       window.alert("Please enter both username and password"); 
    }
 };
 