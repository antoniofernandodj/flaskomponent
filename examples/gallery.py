import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent.parent.resolve())
)


from components import MyHeader
from flaskomponent.css import css_rule, stylesheet
from flaskomponent.elements import (
    h1, html, body, div, script, html, span, img, a
)


stylesheet = stylesheet().add_style(
    css_rule('.gallery',
        display='grid',
        grid_template_columns='repeat(auto-fill, minmax(200px, 1fr))',
        gap='10px',
        padding='20px'
    )).add_style(css_rule('.gallery img',
        width='100%',
        border_radius='5px',
        cursor='pointer',
        transition='transform 0.2s'
    )).add_style(css_rule('.gallery img:hover',
        transform='scale(1.05)'
    )).add_style(css_rule('.modal',
        display='none',
        position='fixed',
        z_index='1000',
        left='0',
        top='0',
        width='100%',
        height='100%',
        background_color='rgba(0, 0, 0, 0.8)',
        justify_content='center',
        align_items='center'
    )).add_style(css_rule('.modal img',
        max_width='90%',
        max_height='90%',
        border_radius='5px'
    )).add_style(css_rule('.close',
        position='absolute',
        top='20px',
        right='30px',
        color='white',
        font_size='40px',
        cursor='pointer'
    ))


def ImageCard(i: int):
    return div(
        a({'href': '#'},
            img({
                'src': f'/static/image{i}.jpg',
                'alt': f'Imagem {i}',
                'onclick': f'showImage(this.src);'
            }),
        )
    )

script_element = script({'src': '/static/js/gallery.js'})


root = html(
    {'lang': 'en'},
    MyHeader('Galeria de Imagens', stylesheet, script_element),
    body(
        div(
            div(
                {'class': 'gallery'},
                h1('Galeria de Imagens'),
                *map(ImageCard, range(1, 4))
            )
        ),
        div(
            {'class': 'modal', 'id': 'imageModal'},
            span({'class': 'close', 'onclick': 'closeModal()'}, '&times;'),
            img({'id': 'modalImage'})
        )
    )
)