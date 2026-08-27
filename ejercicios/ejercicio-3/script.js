const formulario = document.getElementById('formulario');
const nombreInput = document.getElementById('nombre');
const emailInput = document.getElementById('email');
const errorNombre = document.getElementById('errorNombre');
const errorEmail = document.getElementById('errorEmail');
const mensajeExito = document.getElementById('mensajeExito');

function verificarCampos(e)
{
    e.preventDefault();
    errorNombre.textContent = '';
    errorEmail.textContent = '';
    errorNombre.style.display = 'none';
    errorEmail.style.display = 'none';
    mensajeExito.style.display = 'none';
    nombreInput.classList.remove('input-error', 'input-ok');
    emailInput.classList.remove('input-error', 'input-ok');

    let hayError = false;

    if (nombreInput.value.trim() === '') {
        errorNombre.textContent = 'El nombre es obligatorio';
        errorNombre.style.display = 'block';
        nombreInput.classList.add('input-error');
        hayError = true;
    } else {
        nombreInput.classList.add('input-ok');
    }

    if (emailInput.value.trim() === '') {
        errorEmail.textContent = 'El correo electrónico es obligatorio';
        errorEmail.style.display = 'block';
        emailInput.classList.add('input-error');
        hayError = true;
    } else {
        emailInput.classList.add('input-ok');
    }

    if (!hayError) {
        mensajeExito.textContent = 'Formulario enviado correctamente!';
        mensajeExito.style.display = 'block';
        formulario.reset();
        nombreInput.classList.remove('input-ok');
        emailInput.classList.remove('input-ok');

        setTimeout(() => {
            mensajeExito.style.display = 'none';
        }, 3000);
    }

    return;
}

formulario.addEventListener('submit', verificarCampos);