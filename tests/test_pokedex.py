from matplotlib.axes import Axes
import pytest

from palettetown import pokedex, pokemon

@pytest.fixture
def pokedex_obj():
    return pokedex.Pokedex()

def test_Pokedex_getitem_success(pokedex_obj):
    assert isinstance(pokedex_obj['zubat'],pokemon.Pokemon)

def test_Pokedex_getitem_fail(pokedex_obj):
    with pytest.raises(pokedex.MissingPokemonError):
        pokedex_obj['missingno']

def test_Pokedex_choice_success(pokedex_obj):
    pokedex_obj.choice = 'pikachu'
    assert pokedex_obj.choice == 'pikachu'

def test_Pokedex_choice_success(pokedex_obj):
    pokedex_obj.choice = 'pikachu'
    assert pokedex_obj.choice == 'pikachu'
