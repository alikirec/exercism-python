COLORS = (
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
)

colors_dict = {k: v for v, k in enumerate(COLORS)}


def color_code(color):
    return colors_dict[color]


def colors():
    return list(COLORS)
