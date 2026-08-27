const btn = document.getElementById('btnTarea');
const inp = document.getElementById('inputTarea');
const lista = document.getElementById('listaTareas');

const agregarTarea = () => {
    const tarea = inp.value.trim();
    if (tarea === '') return;

    const li = document.createElement('li');
    li.textContent = tarea;

    li.addEventListener('click', () => {
        lista.removeChild(li);
    });

    lista.appendChild(li);
    inp.value = '';
    inp.focus();
};

btn.addEventListener('click', agregarTarea);
