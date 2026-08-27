const btnIncrementador = document.getElementById('btnIncrementar');
const btnDisminuidor = document.getElementById('btnDisminuir');
const numero = document.getElementById('numero');

numero.textContent = '0';

btnIncrementador.addEventListener('click', () => {
    numero.textContent++;
});

btnDisminuidor.addEventListener('click', () => {
    numero.textContent--;
});