from dataclasses import dataclass
import io
import pkgutil
from typing import List

from cycler import cycler
import matplotlib.colors as mpl_colors
import matplotlib.pyplot as plt

class SpriteNotFoundError(Exception):
    pass

@dataclass(frozen=True)
class Pokemon:
    """Read-only dataclass representing the colors of a pokemon sprite.
    This class is intended to be used with a Pokedex object.

    Usage:
    >>> from palettetown.pokedex import Pokedex
    >>> dex = Pokedex()
    >>> pikachu = dex['pikachu']
    >>> assert isinstance(pikachu, Pokemon)
    >>> print(pikachu.cmap)
    <matplotlib.colors.LinearSegmentedColormap object at 0x11bb44ac0>
    >>> print(pikachu.cycler)
    cycler('color', ['#f8d938', '#f7d73f', '#c3a530', '#9c7d39', '#f76357', '#45423c', '#000002'])
    >>> assert isinstance(pikachu.sprite, np.ndarray)
    >>> print(pikachu.sprite.shape)
    (42, 56, 4)

    If you want to use the Pokemon class without a Pokedex you can.
    It's really just a container for color data with a name.
    For example:
    >>> missingno = Pokemon('missingno',[[255,255,255]])
    >>> print(missingno.rgb_float)
    [[1.,1.,1.]]
    >>> print(missingno.rgb_hex)
    ['#ffffff']

    However, there is no sprite for this pokemon, so an error is raised when accessing the sprite property
    >>> print(missingno.sprite.shape)
    palettetown.pokemon.SpriteNotFoundError: The palettetown library does not have a sprite for Pokemon name "missingno".
    """
    name: str
    rgb_int: List[List[int]]

    @property
    def rgb_float(self):
        """RGB values for the pokemon represented as float vectors with values from 0 to 1.

        Returns:
            List[List[str]]: List of colors, each color is a list of r,g,b floating point values.
        """
        return [[c/255. for c in rgb] for rgb in self.rgb_int]

    @property
    def rgb_hex(self):
        """RGB values for the pokemon represented as hex strings.

        Returns:
            List[str]: List of colors, each color is a hex string for the RGB values.
        """
        return list(map(lambda tup: f'#{tup[0]:02x}{tup[1]:02x}{tup[2]:02x}', self.rgb_int))

    @property
    def cmap(self):
        """Matplotlib linear colormap using the pokemon colors.

        Returns:
            matplotlib.colors.LinearSegmentedColormap
        """
        return mpl_colors.LinearSegmentedColormap.from_list(
            f'{self.name}_linear',
            self.rgb_float
        )

    @property
    def cycler(self):
        """Matplotlib color cycler object using the pokemon colors.

        Returns:
            cycler: Cycler object that cycles through the pokemon colors.
        """
        return cycler(color=self.rgb_hex)

    @property
    def sprite(self):
        """Pokemon sprite represented as a numpy ndarray.

        Raises:
            SpriteNotFoundError: The Pokemon name is not known so we cannot load a sprite.

        Returns:
            np.ndarray: (X,Y,C) dimensional array representing the pokemon sprite.
                        X=42 and Y=56 are spatial dimensions.
                        C=4 is the RGBA colorspace dimension.
        """
        sprite_path = f'data/sprites/{self.name}.png'
        sprite_bytes = pkgutil.get_data('palettetown', sprite_path)
        sprite_io = io.BytesIO(sprite_bytes)
        try:
            return plt.imread(sprite_io)
        except SyntaxError:
            raise SpriteNotFoundError(f'The palettetown library does not have a sprite for Pokemon name "{self.name}". Try using a Pokedex object reinstalling palettetown.')
