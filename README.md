Palletetown is a python library that makes it easy to style matplotlib plots using a color palettes based on pokemon.

You can use palletetown to:
* set global matplotlib settings based on a pokemon,
* set a colormap for a pokemon,
* set a color cycler for a pokemon,
* draw a pokemon sprite,
* get RGB color values from the sprite.

The pokeplot module handles high-level user interactions.
Check out the jupyter notebook on our homepage for examples,
or try these pokeplot features with your own plots.
```
import matplotlib.pyplot as plt
import numpy as np
import palletetown.pokeplot as pkp

# Get a colormap with colors set based on the pokemon sprite
cmap = pkp.get_cmap('pikachu')

# Use it with whatever plot you are working on.
data = np.random.random((10,10))
plt.imshow(data, cmap=cmap)

# Draw a pikachu sprite in the top right corner.
pkp.draw_sprite()

plt.show()

# The default colormap can be set.
pkp.set_rc('pikachu')
```

Pokemon and Pokedex objects can be manipulated directly for advanced use cases.
A Pokemon object contains color data related to that pokemon.
Pokedex objects are dictionary-like containers for Pokemon objects.
```
pikachu = pkp.get_pokemon('pikachu')
# matplotlib linear segmented colormap
cmap = pikachu.cmap
# color cycler
cycler = pikachu.cycler
# image of the pokemon as an ndarray
sprite = pikachu.sprite
# list of rgb colors as 8 bit integers
colors_int = pikachu.rgb_int
# list of rgb colors as floats normalized from 0. to 1.
colors_float = pikachu.rgb_float
# list of rgb colors as hex strings
colors_hex = pikachu.rgb_hex
```
