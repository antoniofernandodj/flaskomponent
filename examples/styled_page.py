import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from components import MyHeader
from flaskomponent.css import css_rule, stylesheet
from flaskomponent.elements import (
    h1, html, body, button, div, html,
)

stylesheet = stylesheet().add_style(
    css_rule('.container',
        margin='0 auto',
        padding='20px',
        max_width='600px'
    )).add_style(css_rule(
        '.primary-button',
        background='#28a745',
        color='white',
        padding='10px 20px',
        border_radius='5px'
    ))

root = html(
    {'lang': 'en'},
    MyHeader('', stylesheet),
    body(
        div(h1('Página Estilizada'), {'class': 'container'}),
        button('Clique Aqui', {'class': 'primary-button'})
    )
)