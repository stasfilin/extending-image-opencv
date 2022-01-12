import cv2
import numpy as np


def generate_image(width: int, height: int) -> np.array:
    blank_image = np.ones((width, height, 3), np.uint8) * (107, 142, 35)
    return blank_image


blank_image = generate_image(80, 100)

cv2.imwrite("blank_image.png", blank_image)
