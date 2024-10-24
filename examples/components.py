import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from typing import Any, TypedDict
from flaskomponent.css import stylesheet
from flaskomponent.elements import head, meta, style, title, button


class Theme(TypedDict):
    background: str
    color: str
    name: str


def MyHeader(title_name: str, *children: Any):

    def filter_html_element(child):
        if not isinstance(child, stylesheet):
            return True
        return False
        
    def filter_stylesheets(child):
        if isinstance(child, stylesheet):
            return True
        return False

    html_elements = list(filter(filter_html_element, children))
    styles_list = list(filter(filter_stylesheets, children))
    return head(
        meta({'charset': 'UTF-8'}),
        meta({'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}),
        title(title_name), *html_elements, *map(style, styles_list)
    )


def CustomButton(theme: Theme):
    return button(
        {'onclick': f'setTheme(`{theme["background"]}`, `{theme["color"]}`)'},
        theme['name']
    )

button_element = CustomButton({'background': 'dark', 'color': '#ffffff', 'name': 'Name'})
head_element = MyHeader('titlename', button_element)

print(button_element)
print(head_element)