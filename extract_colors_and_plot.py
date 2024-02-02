from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def extract_color_channels(src_path):
    src = Image.open(src_path)
    src = np.asarray(src)
    src_R, src_G, src_B = src[:, :, 0], src[:, :, 1], src[:, :, 2]
    return src, src_R, src_G, src_B

def plot_all_images(src, src_R, src_G, src_B):
    plt.subplot(2, 2, 1)
    plt.title('Source Image')
    plt.imshow(src)

    plt.subplot(2, 2, 2)
    plt.title('Red Channel')
    plt.imshow(src_R, cmap='Reds')

    plt.subplot(2, 2, 3)
    plt.title('Green Channel')
    plt.imshow(src_G, cmap='Greens')

    plt.subplot(2, 2, 4)
    plt.title('Blue Channel')
    plt.imshow(src_B, cmap='Blues')
    
    plt.show()