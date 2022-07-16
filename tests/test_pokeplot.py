import pytest

from palettetown import pokedex, pokeplot

def test_draw_sprite_success():
    pokeplot.draw_sprite('pikachu')

def test_draw_sprite_error():
    with pytest.raises(pokedex.MissingPokemonError):
        pokeplot.draw_sprite('missingno')

def test_get_cmap_success():
    pokeplot.get_cmap('pikachu')

def test_get_cmap_failure():
    with pytest.raises(pokedex.MissingPokemonError):
        pokeplot.get_cmap('missingno')

def test_get_pokemon_success():
    pokeplot.get_pokemon('pikachu')

def test_get_pokemon_failure():
    with pytest.raises(pokedex.MissingPokemonError):
        pokeplot.get_pokemon('missingno')

def test_set_rc_success():
    pokeplot.set_rc('pikachu')

def test_set_rc_error():
    with pytest.raises(pokedex.MissingPokemonError):
        pokeplot.set_rc('missingno')
