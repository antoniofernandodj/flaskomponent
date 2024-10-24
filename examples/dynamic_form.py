import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from components import MyHeader
from flaskomponent.elements import (
    h1, html, body, div, script,
    option, html, form, label, select
)


script_element = script("""
    const updateForm = () => {
        const selectedOption = document.getElementById('options').value;
        const additionalFields = document.getElementById('additionalFields');
        additionalFields.innerHTML = '';
        if (selectedOption === 'option1') {
            additionalFields.innerHTML = '<input type="text" placeholder="Campo Extra 1">';
        } else if (selectedOption === 'option2') {
            additionalFields.innerHTML = '<input type="text" placeholder="Campo Extra 2">';
        }
    };
    """
)

root = html(
    {'lang': 'en'},
    MyHeader('Formulário dinâmico', script_element),
    body(
        h1('Formulário Dinâmico'),
        form({'id': 'dynamicForm'}, 
            label('Escolha uma opção:'),
            select({'id': 'options', 'onchange': 'updateForm();'},
                option('Selecione', {'value': ''}),
                option('Opção 1', {'value': 'option1'}),
                option('Opção 2', {'value': 'option2'})
            ),
            div({'id': 'additionalFields'})  # Campos adicionais
        )
    )
)

print(root)