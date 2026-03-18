document.getElementById("btn-register").addEventListener("click", register);

function register() {
    const password = document.getElementById("user-password").value;
    const repeatPassword = document.getElementById("user-repeat-password").value;

    if(password !== repeatPassword) {
        alert("Las contraseñas no coinciden");
        return;

        //sweetalert
    }

    const data = {
        name: document.getElementById("user-name").value,
        email: document.getElementById("user-email").value,
        password: document.getElementById("user-password").value,
        
    }
    //endpoint
    fetch('api/user',{
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result => {
        if(result.success) {
            alert("Usuario se guardo correctamente");
        } else {
            alert(result.message);
        }
    })
    .catch(error => {
        console.error(error);
    })

}
