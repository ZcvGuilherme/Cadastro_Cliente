document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const nome = form.querySelector("input[name='nome']");
    const email = form.querySelector("input[name='email']");
    const telefone = form.querySelector("input[name='telefone']");
    const dataNasc = form.querySelector("input[name='data_nasc']");
    const sexo = form.querySelector("select[name='sexo']");

    const erroTelefone = document.querySelector('.erro-telefone');
    if (erroTelefone) erroTelefone.style.display = 'none';

    // Aplica a máscara no telefone conforme o usuário digita
    telefone.addEventListener('input', () => {
        telefone.value = aplicarMascaraTelefone(telefone.value);
        telefone.classList.remove('erro');
        if (erroTelefone) erroTelefone.style.display = 'none';
    });

    form.addEventListener('submit', (e) => {
        let mensagensErro = [];

        if (!nome.value.trim()) {
            mensagensErro.push("O nome é obrigatório.");
        }

        if (!email.value.trim()) {
            mensagensErro.push("O e-mail é obrigatório.");
        }

        if (!telefone.value.trim()) {
            mensagensErro.push("O telefone é obrigatório.");
        } else if (!validarTelefone(telefone.value)) {
            mensagensErro.push("Telefone inválido. Use o formato (99) 99999-9999.");
        }

        if (!dataNasc.value.trim()) {
            mensagensErro.push("A data de nascimento é obrigatória.");
        }

        if (!sexo.value.trim()) {
            mensagensErro.push("Selecione o sexo.");
        }

        if (mensagensErro.length > 0) {
            e.preventDefault();

            // Remove mensagens anteriores, se houver
            const mensagensAntigas = document.querySelector(".mensagens-js");
            if (mensagensAntigas) {
                mensagensAntigas.remove(); // Remove as mensagens antigas
            }

            // Cria um novo bloco de mensagens no topo do formulário
            const divErros = document.createElement("div");
            divErros.classList.add("mensagens-js");

            mensagensErro.forEach(msg => {
                const p = document.createElement("p");
                p.classList.add("flash", "erro");
                p.textContent = msg;
                divErros.appendChild(p);
            });

            form.parentElement.insertBefore(divErros, form); // Insere as novas mensagens

            // Faz a div sumir com efeito suave após 5s
            setTimeout(() => {
                divErros.classList.add("esconder");
            
                // Remove do DOM após o fim da transição (500ms)
                setTimeout(() => {
                    divErros.remove();
                }, 500);
            }, 5000);
            
        }
    });

    function validarTelefone(telefone) {
        const regexTelefone = /^\(\d{2}\) \d{5}-\d{4}$/;
        return regexTelefone.test(telefone);
    }

    function aplicarMascaraTelefone(valor) {
        valor = valor.replace(/\D/g, '');
        if (valor.length > 11) valor = valor.slice(0, 11);

        if (valor.length > 6) {
            return `(${valor.slice(0, 2)}) ${valor.slice(2, 7)}-${valor.slice(7)}`;
        } else if (valor.length > 2) {
            return `(${valor.slice(0, 2)}) ${valor.slice(2)}`;
        } else {
            return `(${valor}`;
        }
    }
});



function editarLinha(botao) {
    const linha = botao.closest('tr');
    const colunas = linha.querySelectorAll('td');

    const valoresOriginais = [];
    for (let i = 0; i < colunas.length - 1; i++) {
        valoresOriginais.push(colunas[i].textContent.trim());
    }

    // Substituir campos por inputs (pula o ID)
    for (let i = 1; i <= 5; i++) {
        colunas[i].innerHTML = `<input type="text" value="${valoresOriginais[i]}" />`;
    }

    // Botões de Confirmar e Cancelar
    colunas[6].innerHTML = `
        <button onclick="confirmarEdicao(this, ${valoresOriginais[0]})">Confirmar</button>
        <button onclick="cancelarEdicao(this, ${JSON.stringify(valoresOriginais).replace(/"/g, '&quot;')})">Cancelar</button>
    `;
}

function cancelarEdicao(botao, valores) {
    const linha = botao.closest('tr');
    const colunas = linha.querySelectorAll('td');

    for (let i = 1; i <= 5; i++) {
        colunas[i].textContent = valores[i];
    }

    colunas[6].innerHTML = `
        <form class="form01" onsubmit="return false;">
            <button type="button" onclick="editarLinha(this)">Editar</button>
        </form>
        <form class="form01" action="/deletar/${valores[0]}" method="post" onsubmit="return confirm('Tem certeza que deseja excluir este cliente?');">
            <button type="submit">Excluir</button>
        </form>
    `;
}

function confirmarEdicao(botao, id) {
    const linha = botao.closest('tr');
    const inputs = linha.querySelectorAll('input');

    const dados = {
        nome: inputs[0].value,
        idade: inputs[1].value,
        telefone: inputs[2].value,
        email: inputs[3].value,
        sexo: inputs[4].value
    };

    fetch(`/editar-cliente/${id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    }).then(response => {
        if (response.ok) {
            // Atualiza a linha com os novos dados
            inputs.forEach((input, i) => {
                input.parentElement.textContent = input.value;
            });

            linha.querySelector('td:last-child').innerHTML = `
                <form class="form01" onsubmit="return false;">
                    <button type="button" onclick="editarLinha(this)">Editar</button>
                </form>
                <form class="form01" action="/deletar/${id}" method="post" onsubmit="return confirm('Tem certeza que deseja excluir este cliente?');">
                    <button type="submit">Excluir</button>
                </form>
            `;
        } else {
            alert("Erro ao salvar as alterações.");
        }
    }).catch(error => {
        console.error('Erro:', error);
        alert("Erro na requisição.");
    });
}
