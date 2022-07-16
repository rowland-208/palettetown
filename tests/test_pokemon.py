import cycler
import matplotlib.colors as mpl_colors
import numpy as np
import pytest

from palettetown import pokemon

@pytest.fixture
def missingno():
    """No name pokemon has sprite load fail, passes other tests"""
    return pokemon.Pokemon('',[[0,0,0]])

def test_Pokemon_rgb_float(missingno):
    assert missingno.rgb_float[0] == [0.,0.,0.]

def test_Pokemon_rgb_hex(missingno):
    assert missingno.rgb_hex == ['#000000']

def test_Pokemon_cmap(missingno):
    assert isinstance(missingno.cmap,mpl_colors.LinearSegmentedColormap)

def test_Pokemon_cycler(missingno):
    assert isinstance(missingno.cycler,cycler.Cycler)

def test_Pokemon_sprite_fail(missingno):
    with pytest.raises(FileNotFoundError):
        missingno.sprite

@pytest.fixture
def pokemon_named_pikachu():
    """Pokemon with valid name has sprite load success"""
    return pokemon.Pokemon('pikachu',[[0,0,0]])

def test_Pokemon_sprite_success(pokemon_named_pikachu):
    assert isinstance(pokemon_named_pikachu.sprite,np.ndarray)
