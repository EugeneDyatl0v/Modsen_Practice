import os
from PIL import Image
import matplotlib.pyplot as plt


def display_duplicates(duplicates, output_folder='output'):
    """
        Displays and saves pairs of duplicate images side by side.

        Parameters:
        duplicates (list of tuples): List of tuples containing file paths of duplicate images.
        output_folder (str): Folder to save the output images displaying duplicates.

        Output:
        Saves images showing duplicates side by side in the specified output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, dup in enumerate(list(set(duplicates))):
        try:
            img1 = Image.open(dup[0])
            img2 = Image.open(dup[1])
            fig, axes = plt.subplots(1, 2, figsize=(10, 5))
            axes[0].imshow(img1)
            axes[0].set_title(f'Duplicate 1: {dup[0]}')
            axes[0].axis('off')
            axes[1].imshow(img2)
            axes[1].set_title(f'Duplicate 2: {dup[1]}')
            axes[1].axis('off')
            plt.savefig(os.path.join(output_folder, f'duplicate_{i}.png'))
            plt.close(fig)
        except Exception as e:
            print(f"Error displaying duplicates {dup[0]} and {dup[1]}: {e}")
