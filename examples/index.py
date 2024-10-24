import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from email import header
from components import MyHeader
from flaskomponent.css import css_rule, stylesheet
from flaskomponent.elements import (
    h1, html, p, body, button, div, html, form, label,
    header, nav, ul, li, a, h2, footer, span, input
)

stylesheet = stylesheet().add_style(css_rule('body',
    font_family='Arial, sans-serif',
    background_color='#f0f0f0',
    margin='0',
    padding='20px'
)).add_style(css_rule('header',
    background_color='#333',
    color='white',
    padding='10px',
    text_align='center'
)).add_style(css_rule('nav',
    list_style='none',
    padding='0'
)).add_style(css_rule('nav ul li',
    display='inline',
    margin_right='10px'
)).add_style(css_rule('nav ul li a',
    color='white',
    text_decoration='none'
)).add_style(css_rule('footer',
    margin_top='20px',
    background_color='#333',
    color='white',
    padding='10px',
    text_align='center'
))

root = html(
    {'lang': 'en'},
    MyHeader('Interface Complexa', stylesheet),
    body(
        header(
            nav(
                ul(
                    li(a('Home', {'href': '/'})),
                    li(a('Sobre', {'href': '/about'})),
                    li(a('Contato', {'href': '/contact'})),
                )
            )
        ),
        h1('Bem-vindo à Interface Complexa'),
        p('Esta é uma página com múltiplos componentes de interface.'),
        div(
            h2('Formulário de Login'),
            form(
                {'action': '/login', 'method': 'POST'},
                label('Usuário: ', {'for': 'username'}),
                input({'type': 'text', 'name': 'username', 'id': 'username'}),
                p(),
                label('Senha: ', {'for': 'password'}),
                input({'type': 'password', 'name': 'password', 'id': 'password'}),
                p(),
                button('Login', {'type': 'submit'}),
            )
        ),
        div(
            h2('Lista de Tarefas'),
            ul(
                li('Tarefa 1'),
                li('Tarefa 2'),
                li('Tarefa 3'),
                li('Tarefa 4')
            )
        ),
        footer(
            p('© 2024 Meu Site. Todos os direitos reservados.'),
            span('Siga-nos: '),
            a('Twitter', {'href': 'https://twitter.com', 'target': '_blank'}),
            a(' | Facebook', {'href': 'https://facebook.com', 'target': '_blank'}),
        )
    )
)

print(root)