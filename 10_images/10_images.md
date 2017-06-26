### image analysis

- 3 main packages for image analysis in python
    1. scikit image (skimage)
    2. scipy ndimage
    3. opencv
    - these are used in addition to numpy and matplotlib

- recall how we can display arrays as images:
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    a = np.random.random((10, 10)) # 2D random array of floats, from 0 to 1
    f, ax = plt.subplots()
    im = ax.imshow(a) # this uses default colormap 'viridis'
    f.colorbar(im) # add color bar to figure
    plt.colormaps() # list all available colormaps
    im.set_cmap('gray') # use grayscale instead
    ````

    - or can directly specify desired colormap in imshow():
    ```python
    f, ax = plt.subplots()
    im = ax.imshow(a, cmap='gray')
    f.colorbar(im)
    ````
    - how do we turn off the x and y ticks? set them to empty lists:
        - `ax.set_xticks([]), ax.set_yticks([])`

- colour
    - if you have image data in a 2D array, like `a`, the values for each pixel can only represent luminance, there's no colour information
    - can map the luminance to colour using a colour map, but you can't independently represent luminance and colour with a single value per pixel
    - how can colour be represented in an array? as red, green and blue channels (RGB)
    - you could use 3 separate 2D arrays to represent RGB for an image, but normally these are combined into a single 3D array: `nrows x ncols x 3`
    - scikit-image has several demo images built in, let's start with a colour image:
    ```python
    from skimage import data
    immun = data.immunohistochemistry()
    immun.shape # notice it's a 3D array, last dimension represents colour
    f, ax = plt.subplots()
    ax.imshow(immun)
    ````

- spatial filter:
    - smooth the image with a gaussian filter:
    ```python
    from skimage import filters
    gimmun = filters.gaussian(immun, sigma=2) # sigma in number of pixels
    plt.imshow(gimmun)
    ````


- loading different image types as arrays
- change contrast of an image
- manipulate colours
- thresholding, masking an image
- image denoising/smoothing
- image segmentation
- motion correction?
- see skimage image gallery:
    - http://scikit-image.org/docs/dev/auto_examples/
- see recent local Python talk by Joe Donovan for lots of examples:
    - https://github.com/superpythontalks/image_analysis/blob/master/image%20processing.ipynb



