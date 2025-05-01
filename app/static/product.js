document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const nome = form.querySelector("input[name='nome']");
    const quantidade = form.querySelector("input[name='quantidade']");
    const valor = form.querySelector("input[name='valor']");

    form.addEventListener("submit", function (e) {
        let mensagensErro = [];

        if (!nome.value.trim()) {
            mensagensErro.push("O nome do produto é obrigatório.");
        }

        if (!quantidade.value || parseInt(quantidade.value) <= 0) {
            mensagensErro.push("A quantidade deve ser maior que 0.");
        }

        if (!valor.value || parseFloat(valor.value) <= 0) {
            mensagensErro.push("O valor deve ser maior que 0.");
        }

        if (mensagensErro.length > 0) {
            e.preventDefault(); // Impede o envio do formulário
        
            // Remove mensagens antigas
            const mensagensAntigas = document.querySelector(".mensagens-js");
            if (mensagensAntigas) mensagensAntigas.remove();
        
            // Cria um bloco de mensagens no topo do formulário
            const divErros = document.createElement("div");
            divErros.classList.add("mensagens-js");
        
            mensagensErro.forEach(msg => {
                const p = document.createElement("p");
                p.classList.add("flash", "erro");
                p.textContent = msg;
                divErros.appendChild(p);
            });
        
            form.parentElement.insertBefore(divErros, form);
        
            // Remove automaticamente depois de 5 segundos
            setTimeout(() => {
                divErros.remove();
            }, 5000);
        }
        
    });
});






function editarLinha(botao) {
    const linha = botao.closest('tr');
    const colunas = linha.querySelectorAll('td');

    const valoresOriginais = [];

    for (let i = 0; i < colunas.length - 1; i++){
        valoresOriginais.push(colunas[i].textContent.trim());
    }


    for (let i = 1; i <= 3; i++) {
        colunas[i].innerHTML = `<input type="text" value="${valoresOriginais[i]}" />`;
    }

    //Confirmar e cancelar
    colunas[4].innerHTML = `
        <button class="botao-confirmar" onclick="confirmarEdicao(this, ${valoresOriginais[0]})">Confirmar</button>
        <button class="botao-cancelar" onclick="cancelarEdicao(this, ${JSON.stringify(valoresOriginais).replace(/"/g, '&quot;')})">Cancelar</button>
        `;
}

function cancelarEdicao(botao, valores){
    const linha = botao.closest('tr');
    const colunas = linha.querySelectorAll('td');

    for (let i = 1; i <= 3; i++){
        colunas[i].textContent = valores[i];
    }

    colunas[4].innerHTML = `
    <form class="form01" action="/deletar/${valores[0]}" method="post" onsubmit="return confirm('Tem certeza que deseja excluir este cliente?');">
        <button type="submit">Excluir</button>
    </form>
    <form class="form01" onsubmit="return false;">
        <button type="button" onclick="editarLinha(this)">Editar</button>
    </form>
    `;
 }


function confirmarEdicao(botao, id) {
    const linha = botao.closest('tr');
    const inputs = linha.querySelectorAll('input');

    const dados = {
        nome: inputs[0].value,
        quantidade: inputs[1].value,
        valor: inputs[2].value.replace('R$', '').trim().replace(',', '.')
    };

    fetch(`/editar-produto/${id}`,{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
    }).then(response => {
        if (response.ok){

            inputs.forEach((input, i) => {
                input.parentElement.textContent = input.value;
            });

            linha.querySelector('td:last-child').innerHTML = `
                <form class="form01" action="/deletar/${id}" method="post" onsubmit="return confirm('Tem certeza que deseja excluir este produto?');">
                    <button type="submit">Excluir</button>
                </form>
                <form class="form01" onsubmit="return false;">
                    <button type="button" onclick="editarLinha(this)">Editar</button>
                </form>
            `;

        } else {
            alert("Erro ao salvar as alterações.");
        }
    }).catch(error => {
        console.error('Erro: ', error);
        alert("Erro na requisição.");
    });
}

