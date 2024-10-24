import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from components import MyHeader, CustomButton
from flaskomponent.elements import (
    h1, html, body, div, script, html,
)


themes = [
    {'name': 'Light', 'background': '#f0f0f0', 'color': '#333'},
    {'name': 'Dark', 'background': '#333', 'color': '#f0f0f0'}
]

script_element = script({'src': '/static/js/theme.js'})

root = html(
    {'lang': 'en'},
    MyHeader('', script_element),
    body(
        h1('Select a Theme'),
        div(*map(CustomButton, themes)) # type: ignore
    )
)