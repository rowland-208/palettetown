from typing import Optional

import matplotlib.cm as mpl_cm
import matplotlib.pyplot as plt
import matplotlib.axes as mpl_axes

from palettetown.pokedex import Pokedex

DEX = Pokedex()

def draw_sprite(pokemon_name: str, ax: Optional[mpl_axes.Axes]=None):
    """Draw a pokemon sprite.

    Args:
        pokemon_name (str): A valid pokemon name.
        ax (matplotlib.axes.Axes or None, optional): Axis to draw the sprite on. Defaults to None.
            If None, create an axis in the top-right corner of the current figure.

    Returns:
        matplotlib.axes.Axes: The axis that contains the pokemon sprite.
    """
    ax = ax or plt.gcf().add_axes(rect=[0.8, 0.8, 0.2, 0.2], anchor='NE', zorder=1)
    ax.imshow(DEX[pokemon_name].sprite)
    ax.axis('off')
    return ax

def get_cmap(pokemon_name: str):
    """Get a colormap for a pokemon.

    Args:
        pokemon_name (str): A valid pokemon name.

    Returns:
        matplotlib.colors.LinearSegmentedColormap: Linear colormap with colors from the pokemon sprite.
    """
    return DEX[pokemon_name].cmap

def get_pokemon(pokemon_name: str):
    """Get a Pokemon object by name.

    Args:
        pokemon_name (str): A valid pokemon name.

    Returns:
        Pokemon: The corresponding pokemon object.
    """
    return DEX[pokemon_name]

def set_rc(pokemon_name: str, update_cmap = True, update_prop_cycle = False):
    """Update matplotlib rc params for cmap and prop_cycler colors based on the pokemon sprite.

    Args:
        pokemon_name (str): A valid pokemon name.
        update_cmap (bool, optional): If false, skip updating the cmap property. Defaults to True.
        update_prop_cycle (bool, optional): If false, skip updating the color cycler property. Defaults to False.
    """
    if update_prop_cycle:
        plt.rc('axes', prop_cycle=DEX[pokemon_name].cycler)
    if update_cmap:
        mpl_cm.register_cmap(pokemon_name, DEX[pokemon_name].cmap)
        plt.rc('image', cmap=pokemon_name)
