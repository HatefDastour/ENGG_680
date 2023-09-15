import math
import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_colortable(colors, *, ncols=4, sort_colors=True):
    '''
    Code source: https://matplotlib.org/stable/gallery/color/named_colors.html
    '''
    # Set dimensions and spacing
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value, and name
    if sort_colors:
        names = sorted(colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    # Calculate figure dimensions
    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin / width, margin / height,
                        (width - margin) / width, (height - margin) / height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    # Iterate through colors and plot swatches with labels
    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        # Add color name text and swatch rectangle
        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y - 9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig
    
    
    
'''
# Testing the above function
# Example color dictionary
example_colors = {
    'red': 'red',
    'green': 'green',
    'blue': 'blue',
    'purple': 'purple',
    'yellow': 'yellow',
    'orange': 'orange'
}

# Call the function with the example colors
_ = plot_colortable(example_colors)
'''


def _CSS4_COLORS_df():
    # Convert the dictionary to a list of tuples (color_name, hex_code)
    CSS4_COLORS = sorted(mcolors.CSS4_COLORS, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    CSS4_COLORS = {key: mcolors.CSS4_COLORS[key] for key in CSS4_COLORS}
    color_items = list(CSS4_COLORS.items())

    # Calculate the split points for the four groups
    split_points = [len(color_items) // 4, 2 * len(color_items) // 4, 3 * len(color_items) // 4]

    # Split the list into four groups
    group1 = color_items[:split_points[0]]
    group2 = color_items[split_points[0]:split_points[1]]
    group3 = color_items[split_points[1]:split_points[2]]
    group4 = color_items[split_points[2]:]

    # Extract color names and corresponding hexadecimal codes from each group
    color_names1, hex_codes1 = zip(*group1)
    color_names2, hex_codes2 = zip(*group2)
    color_names3, hex_codes3 = zip(*group3)
    color_names4, hex_codes4 = zip(*group4)

    # Create a DataFrame with 8 columns: 
    # Color1, Hex Code 1, Color2, Hex Code 2, Color3, Hex Code 3, Color4, Hex Code 4
    data = {'Color 1': color_names1, 'Hex Code 1': hex_codes1,
            'Color 2': color_names2, 'Hex Code 2': hex_codes2,
            'Color 3': color_names3, 'Hex Code 3': hex_codes3,
            'Color 4': color_names4, 'Hex Code 4': hex_codes4
            }

    df = pd.DataFrame(data)
    return df