"""
base_dehaze.py
--------------
Dummy template for the original dehazing algorithm based on the paper:
'Lower Bound on Transmission Using Non-Linear Bounding Function in Single Image Dehazing'.

This file contains placeholders for:
- Airlight estimation
- Bounding function delta estimation
- Transmission computation
- Image recovery

Replace all TODO sections with final implementations.
"""

import cv2
import numpy as np
import argparse
from utils import load_image, save_image, min_channel


def estimate_airlight(image):
    """
    Estimate atmospheric light A.
    Dummy placeholder: returns a constant (white-ish) value.
    TODO: replace with real implementation.
    """
    return np.array([240, 240, 240])  # placeholder


def estimate_delta(image):
    """
    Estimate bounding function delta(x,y).
    Dummy placeholder using min channel.
    TODO: replace with real implementation based on the paper.
    """
    min_I = min_channel(image)
    delta = 1.0 / (min_I + 1e-6)  # very rough placeholder
    return delta


def compute_transmission(image, A, delta):
    """
    Compute lower bound transmission.
    TODO: replace with actual formula from the paper.
    """
    transmission = np.exp(-delta * 0.1)  # placeholder
    return np.clip(transmission, 0.05, 1.0)


def recover_image(image, t, A):
    """
    Recover haze-free image using the estimated transmission.
    TODO: replace with the real recovery equation.
    """
    A = A.reshape(1, 1, 3)
    restored = (image - A) / np.maximum(t[..., None], 0.1) + A
    return np.clip(restored, 0, 255).astype(np.uint8)


def dehaze(image_path, output_path):
    """
    Full pipeline: load → estimate → compute → restore → save.
    """
    image = load_image(image_path)
    A = estimate_airlight(image)
    delta = estimate_delta(image)
    t = compute_transmission(image, A, delta)
    restored = recover_image(image, t, A)
    save_image(restored, output_path)


def main():
    parser = argparse.ArgumentParser(description="Base dehazing algorithm (dummy template).")
    parser.add_argument("--input", required=True, help="Path to hazy input image")
    parser.add_argument("--output", required=True, help="Output path for restored image")
    args = parser.parse_args()

    dehaze(args.input, args.output)
    print(f"Saved dehazed output to {args.output}")


if __name__ == "__main__":
    main()
    