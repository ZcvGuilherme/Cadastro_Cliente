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
        }
    });
});
