document.getElementById('enviar').addEventListener('click', function() {
    const sabor = document.getElementById('pizza-sabor').value;
    const pagamento = document.getElementById('pagamento').value;

    fetch('/fazer_pedido', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sabor: sabor, metodo_pagamento: pagamento }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Sabor não encontrado.');
        }
        return response.json();
    })
    .then(data => {
        swal("Pedido Recebido!", data.mensagem, "success").then(() => {
            window.location.href = '/progresso';
        });
    })
    .catch(error => {
        swal("Erro!", error.message, "error");
    });
});
