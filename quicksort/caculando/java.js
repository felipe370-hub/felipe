function calcularCompra(valorCompra, numeroParcelas = 1, descontoAVista = 0) {
    if (numeroParcelas === 1) {
        const valorComDesconto = valorCompra - (valorCompra * (descontoAVista / 100));
        return `Valor à vista com desconto de ${descontoAVista}%: R$${valorComDesconto.toFixed(2)}`;
    } else {
        const valorParcela = valorCompra / numeroParcelas;
        return `Valor parcelado em ${numeroParcelas}x: R$${valorParcela.toFixed(2)} por parcela`;
    }
}

console.log(calcularCompra(1000, 1, 10));

console.log(calcularCompra(1000, 5));
