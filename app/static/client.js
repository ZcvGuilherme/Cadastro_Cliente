document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const nomeInput = document.querySelector('input[name="nome"]');
    const emailInput = document.querySelector('input[name="email"]');
    const telefoneInput = document.querySelector('input[name="telefone"]');
    const dataNascInput = document.querySelector('input[name="data_nasc"]');
    const sexoInput = document.querySelector('select[name="sexo"]');

    const erroTelefone = document.querySelector('.erro-telefone');

    if (!form || !telefoneInput || !erroTelefone) return;

    erroTelefone.style.display = 'none';

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

    telefoneInput.addEventListener('input', () => {
        telefoneInput.value = aplicarMascaraTelefone(telefoneInput.value);
        telefoneInput.classList.remove('erro');
        erroTelefone.style.display = 'none';
    });

    form.addEventListener('submit', (e) => {
        let valido = true;
    
        const campos = [
            nomeInput,
            emailInput,
            telefoneInput,
            dataNascInput,
            sexoInput
        ];
    
        // Limpa estados anteriores
        campos.forEach(input => input.classList.remove('erro'));
        erroTelefone.style.display = 'none';
    
        campos.forEach(input => {
            const nomeCampo = input.getAttribute('name');
            const valor = input.value.trim();
    
            switch (nomeCampo) {
                case 'nome':
                case 'email':
                case 'data_nasc':
                case 'sexo':
                    if (valor === '') {
                        input.classList.add('erro');
                        valido = false;
                    }
                    break;
    
                case 'telefone':
                    if (!validarTelefone(valor)) {
                        input.classList.add('erro');
                        erroTelefone.style.display = 'block';
                        valido = false;
                    }
                    break;
            }
        });
    
        if (!valido) {
            e.preventDefault();
        }
    });
});
