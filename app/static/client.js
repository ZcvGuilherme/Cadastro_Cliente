document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const telefoneInput = document.querySelector('input[name="telefone"]');
    const erroTelefone = document.querySelector('.erro-telefone');

    if (!form || !telefoneInput || !erroTelefone) return;

    // Oculta o erro inicialmente
    erroTelefone.style.display = 'none';

    // Função para validar o formato do telefone
    function validarTelefone(telefone) {
        const regexTelefone = /^\(\d{2}\) \d{5}-\d{4}$/;
        return regexTelefone.test(telefone);
    }

    // Função para aplicar a máscara no telefone
    function aplicarMascaraTelefone(valor) {
        valor = valor.replace(/\D/g, '');

        if (valor.length > 11) valor = valor.slice(0, 11); // máximo de 11 dígitos

        if (valor.length > 6) {
            return `(${valor.slice(0, 2)}) ${valor.slice(2, 7)}-${valor.slice(7)}`;
        } else if (valor.length > 2) {
            return `(${valor.slice(0, 2)}) ${valor.slice(2)}`;
        } else {
            return `(${valor}`;
        }
    }

    // Aplica a máscara conforme o usuário digita
    telefoneInput.addEventListener('input', () => {
        telefoneInput.value = aplicarMascaraTelefone(telefoneInput.value);

        // Esconde erro enquanto digita
        telefoneInput.classList.remove('erro');
        erroTelefone.style.display = 'none';
    });

    // Validação no envio do formulário
    form.addEventListener('submit', (e) => {
        const telefone = telefoneInput.value;

        if (!validarTelefone(telefone)) {
            e.preventDefault();

            telefoneInput.classList.add('erro');
            erroTelefone.style.display = 'block';

            telefoneInput.focus();
        }
    });
});
