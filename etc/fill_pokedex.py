import json
import os
from typing import List

from colorsort.colorsort import image_to_vec, reduce_colors, sort_colors
import cv2
import numpy as np
from tqdm import tqdm

def array_rank(x):
    return len(x.shape)

def load_rgba(path):
    image_bgr = cv2.imread(path,-1)
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGRA2RGBA)

def to_rgba_if_grayscale(image):
    if array_rank(image)==2:
        return np.stack([image,image,image,np.ones_like(image)*255])
    else:
        return image

def remove_alpha(vec_rgba):
    vec_rgba = vec_rgba[vec_rgba[:,3]!=0]
    return vec_rgba[:,:3]

def generate_pokemon_data(sprite_path: str):
    image_rgba_or_gray = load_rgba(sprite_path)
    image_rgba = to_rgba_if_grayscale(image_rgba_or_gray)

    vec_rgba = image_to_vec(image_rgba)
    vec_rgb = remove_alpha(vec_rgba)
    reduced_rgb = reduce_colors(vec_rgb, max_num_colors=10)
    ordered_rgb = sort_colors(reduced_rgb)

    pokemon_name = os.path.basename(sprite_path).split('.')[0]
    return {
        'name': pokemon_name,
        'rgb_int': ordered_rgb.tolist()
    }

def main(sprite_paths: List[str], pokedex_path: str):
    json.dump(
        list(tqdm(map(generate_pokemon_data, sprite_paths))),
        open(pokedex_path,'w'))

def plot(sprite_paths: List[str]):
    import matplotlib.pyplot as plt

    for sprite_path in sprite_paths:
        data = generate_pokemon_data(sprite_path)
        plt.imshow(np.array(data['rgb_int'])[None])
        plt.figure()
    plt.show()

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--pokedex-path', '-p', type=str, required=True, help='Path to the pokedex.json file to store color data.')
    parser.add_argument('--sprite-paths', '-s', nargs='+', type=str, required=True, help='Path to sprite data to use for generating pokedex data.')
    args = parser.parse_args()

    main(args.sprite_paths, args.pokedex_path)
