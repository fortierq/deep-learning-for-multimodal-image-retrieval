from pathlib import Path
from itertools import islice
import matplotlib.pyplot as plt
import PIL

def rm_dir(path):  # delete a directory
    if path.exists():
        for child in path.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                rm_dir(child)
        path.rmdir()

def plots(images, caption=None, n=5):
    import warnings
    warnings.filterwarnings("ignore", message="Glyph.* missing from current font")

    figure = plt.figure(figsize=(5*n, 20))
    for i, f in enumerate(islice(images, n)):
        figure.add_subplot(1, n, i+1)
        plt.axis("off")
        plt.title(caption(i, f))
        plt.imshow(PIL.Image.open(f))
