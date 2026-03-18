document.getElementById("btn-login").addEventListener("click", login);

function login() {

    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;

    if(email == ""){
        alert("Por favor ingresa tu correo electrónico.");
        return;
        //TODO completar con sweet alert
    }
    if(password == ""){
        alert("Por favor ingresa tu contraseña.");
        return;
        //TODO completar con sweet alert

    }
    const data = {
        email: email,
        password: password
    }
     fetch('/api/login',{
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result => {
        if(result.success) {
            window.location.href = "/welcome";
        } else {
            alert("sus datos son incorrectos");
            //TODO completar con sweet alert
        }
    })
    .catch(error => {
        console.error(error);
    })
}

