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
