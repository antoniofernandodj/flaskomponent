import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from examples.components import MyHeader
from flaskomponent.css import css_rule, stylesheet
from flaskomponent.elements import (
    h1, html, p, body, button, div, html,
)


stylesheet = stylesheet().add_style(
    css_rule('body',
        font_family="'Helvetica Neue', sans-serif",
        background="linear-gradient(to right, #f8f9fa, #e0e0e0)",
        margin='0',
        padding='0',
        display='flex',
        justify_content='center',
        align_items='center',
        height='100vh'
    )).add_style(css_rule('.container',
        text_align='center',
        background_color='white',
        padding='40px',
        border_radius='15px',
        box_shadow='0 4px 8px rgba(0, 0, 0, 0.1)',
        max_width='500px',
        width='100%'
    )).add_style(css_rule('h1',
        color='#333',
        font_size='36px',
        margin_bottom='20px'
    )).add_style(css_rule('p',
        font_size='18px',
        color='#666',
        margin_bottom='30px'
    )).add_style(css_rule('button',
        background_color='#28a745',
        color='white',
        padding='10px 20px',
        border='none',
        border_radius='5px',
        cursor='pointer',
        font_size='16px'
    )).add_style(css_rule('button:hover',
        background_color='#218838'
    )).add_style(css_rule('.footer',
        margin_top='30px',
        font_size='14px',
        color='#888'
    )
)


root = html(
    {'lang': 'en'},
    MyHeader('Beautiful Interface', stylesheet),
    body(
        div({'class': 'container'},
            h1('Welcome to the Beautiful Page'),
            p('This page is designed with simplicity and elegance in mind.'),
            button('Click Me', {"onclick": "alert('Hello, world!')"}),
            div(
                {'class': 'footer'},
                p('© 2024 Beautiful Interface')
            )
        )
    )
)

print(root)