"""
utils.py
--------
Common utility functions for image I/O, preprocessing,
and other helpers used across the project.
"""

import cv2
import numpy as np
import os


def load_image(path):
    """
    Load an image in BGR format and convert to RGB.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Failed to load image: {path}")

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)


def save_image(img, path):
    """
    Save an RGB image as BGR using OpenCV.
    """
    img_bgr = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, img_bgr)


def min_channel(image):
    """
    Compute the minimum across the RGB channels (used in many dehazing methods).
    """
    return np.min(image, axis=2)


def ensure_dir(path):
    """
    Create directory if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
