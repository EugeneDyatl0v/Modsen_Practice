# Duplicate Image Finder

This project is a tool for finding and displaying duplicate images from multiple folders. It uses image hashing and neural network-based feature extraction to identify duplicate images. The tool can optionally use parallel processing to enhance performance when working with a large number of images.

## Features

- Load images from multiple folders
- Calculate image hashes using different methods ('phash', 'dhash', 'whash', 'ahash')
- Extract features from images using a pre-trained VGG16 model
- Identify duplicate images based on hashes and/or feature vectors
- Display and save pairs of duplicate images side by side
- Optional parallel processing for improved performance

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/duplicate-image-finder.git
   cd duplicate-image-finder
   ```
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
## Usage

Prepare your image folders. Ensure the images are stored in folders that you want to check for duplicates.

Run the script:

```bash
python main.py
```
Modify the folders list in the main.py file to include the paths to your image folders:

```python
folders = ['path/to/folder1', 'path/to/folder2', 'path/to/folder3']
```
The script will process the images, find duplicates, and save the results in the output folder. The duplicates will be displayed side by side in the output images.

## Configuration

You can configure the following parameters in the find_duplicates_app function in main.py:

    method: Hashing method to use ('phash', 'dhash', 'whash', 'ahash')
    use_nn: Use neural network for feature extraction if True
    threshold: Threshold for cosine similarity to consider images as duplicates
    use_parallel: Use parallel processing if True

Example:

```pydoc
duplicates = find_duplicates_app(folders, method='phash', use_nn=True, threshold=0.9, use_parallel=True)
```
## License

This project is licensed under the MIT License. See the LICENSE file for details.

