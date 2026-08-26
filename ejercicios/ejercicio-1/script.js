const btn = document.getElementById('btnColor');

function color_random(){
    return Math.floor(Math.random() * 256)
}

btn.addEventListener('click', () => {
    const color = `rgb(${color_random()}, ${color_random()}, ${color_random()})`;
    document.body.style.backgroundColor = color;
});