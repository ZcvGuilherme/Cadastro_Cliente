document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const telefoneInput = document.querySelector('input[name="telefone"]');
    const erroTelefone = document.querySelector('.erro-telefone');

    erroTelefone.style.display = 'none'

    // Máscara para o campo de telefone
    telefoneInput.addEventListener('input', () => {
        let valor = telefoneInput.value.replace(/\D/g, '');

        if (valor.length > 11) valor = valor.slice(0, 11); // máximo de 11 dígitos

        if (valor.length > 6) {
            telefoneInput.value = `(${valor.slice(0, 2)}) ${valor.slice(2, 7)}-${valor.slice(7)}`;
        } else if (valor.length > 2) {
            telefoneInput.value = `(${valor.slice(0, 2)}) ${valor.slice(2)}`;
        } else {
            telefoneInput.value = `(${valor}`;
        }

        // Esconde erro enquanto digita
        telefoneInput.classList.remove('erro');
        erroTelefone.style.display = 'none';
    });

    // Validação no envio do formulário
    form.addEventListener('submit', (e) => {
        const telefone = telefoneInput.value;
        const regexTelefone = /^\(\d{2}\) \d{5}-\d{4}$/;

        if (!regexTelefone.test(telefone)) {
            e.preventDefault();

            // Mostra erro
            telefoneInput.classList.add('erro');
            erroTelefone.style.display = 'block';

            telefoneInput.focus();
        }
    });
});
