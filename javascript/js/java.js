function mudarBG(cor) {
    document.body.style.backgroundColor = cor;
    let titulo = document.getElementById('titulo');
    if (cor.toLowerCase() === 'black' || cor === '#000000') {
        titulo.style.color = 'white';
    } else if (cor.toLowerCase() === 'white' || cor === '#FFFFFF') {
        titulo.style.color = 'black';
    } else {
        titulo.style.color = '';
    }
}

let cor = prompt("Digite a cor ou o código hexadecimal para o fundo:");
mudarBG(cor);
