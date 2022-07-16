import difflib
import json
from typing import Dict
import pkgutil

from palettetown.pokemon import Pokemon

class MissingPokemonError(Exception):
    pass

class Pokedex:
    """Container object to load and retrieve Pokemon objects.

    Usage:
    >>> dex = Pokedex()
    >>> pokemon = dex['pikachu'] # retrieve a Pokemon object
    >>> dex['pikahcu'] # raises an error
    palettetown.pokedex.MissingPokemonError: "pikahcu" is not in the pokedex. Did you mean: pikachu, pichu?
    """
    def __init__(self):
        table = json.loads(pkgutil.get_data('palettetown', 'data/pokedex.json').decode('utf-8'))
        self.pokedata: Dict[str, Pokemon] = {
            row['name']: Pokemon(**row)
            for row in table
        }

    def __getitem__(self, pokemon_name: str) -> Pokemon:
        self.assert_pokemon_exists(pokemon_name)
        return self.pokedata[pokemon_name]

    def assert_pokemon_exists(self, pokemon_name):
        """Check if a pokemon is in the pokedex. Give a helpful error if not.

        Args:
            pokemon_name (str): The name of a pokemon.

        Raises:
            MissingPokemonError: The pokemon name is not in the Pokedex. Suggest pokemon names the user might have meant.
        """
        if pokemon_name not in self.pokedata:
            matches = difflib.get_close_matches(pokemon_name, self.pokedata.keys())
            extra_info =  f' Did you mean: {", ".join(matches)}?' if matches else ''
            raise MissingPokemonError(f'"{pokemon_name}" is not in the pokedex.{extra_info}')
