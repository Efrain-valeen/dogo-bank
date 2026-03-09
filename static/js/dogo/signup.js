document.getElementById("btn-register").addEventListener("click", register);
function register() {
    password: document.getElementById("user-password").value,
    repeatPassword: document.getElementById("user-repeat-password").value

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
}
    