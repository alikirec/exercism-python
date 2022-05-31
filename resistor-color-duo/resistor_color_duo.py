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

color_indices = {value: index for index, value in enumerate(COLORS)}

def value(colors):
    first, second = [color_indices.get(color, 0) for color in colors[:2]]
    
    return first * 10 + second
