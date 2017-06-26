### image analysis


- we've already dealt a bit with images using numpy and matplotlib
- 3 main packages specifically for image manipulation and analysis in python:
    1. scikit image (skimage)
    2. scipy ndimage
    3. opencv

- recall how we can display numpy arrays as images:
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import io # functions for image file input/output
    faceg = io.imread('face_gray.png') # 2D array, dtype is uint8
    f, ax = plt.subplots()
    im = ax.imshow(faceg) # this uses default colormap 'viridis'
    ````
    - why is matplotlib displaying colour, when we know the image is grayscale?
    - for single channel images (i.e., 2D arrays where each value is just luminance), MPL puts each pixel value through a color map, default is 'viridis', but we can choose 'gray' instead:
    ```python
    f.colorbar(im) # add color bar to figure
    plt.colormaps() # list all available colormaps
    im.set_cmap('gray') # use grayscale instead
    ````
    - or can directly specify desired colormap in imshow():
    ```python
    f, ax = plt.subplots()
    im = ax.imshow(faceg, cmap='gray')
    f.colorbar(im)
    ````
    - how do we turn off the axes x and y ticks? set them to empty lists:
        - `ax.set_xticks([]), ax.set_yticks([])`

    - how do we rotate arrays, and therefore images?
    ```python
    f, ax = plt.subplots()
    ax.imshow(np.rot90(faceg), cmap='gray') # 90 deg counterclockwise
    io.imsave('rot_face_gray.png') # save it back to a new file
    ````
    - for other kinds of rotation, see ndimage.rotate?
    - can use `np.flipud` and `np.fliplr` to flip arrays vertically or horizontally

    - imshow can display images using different kinds of interpolation, default is 'nearest', which means no interpolation
    - `ax.imshow(face, interpolation='nearest')`
    - 'bilinear', 'bicubic', and 'gaussian' are probably the most common, see https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html for examples

- colour
    - if you have image data in a 2D array, the values for each pixel can only represent luminance, there's no colour information
    - can map the luminance to colour using a colour map, but you can't independently represent luminance and colour with a single value per pixel
    - how can colour be represented in an array? as red, green and blue channels (RGB)
    - you could use 3 separate 2D arrays to represent RGB for an image, but normally these are combined into a single 3D array: `nrows x ncols x 3`
    ```python
    cface = io.imread('face.png')
    cface.shape # notice it's a 3D array, last dimension represents colour
    f, ax = plt.subplots()
    ax.imshow(face) # no colormap used when image already has color info
    ````
    - scikit-image has several demo images built in, let's start with a colour image:
    ```python
    from skimage import data
    immun = data.immunohistochemistry()
    immun.shape # notice it's a 3D array, last dimension represents colour
    f, ax = plt.subplots()
    ax.imshow(immun)
    ````
    - we can modify the R, G and B channels separately. Let's remove all the red from the image. How can we do this by manipulating the array data
        - set the R channel to 0:



- spatial filter:
    - smooth the image with a gaussian filter:
    ```python
    from skimage import filters
    gimmun = filters.gaussian(immun, sigma=2) # sigma in number of pixels
    plt.imshow(gimmun)
    ````

- edge detection:
    ```python
    ohki = io.imread('ohki2005.png')
    f, ax = plt.subplots()
    ax.imshow(ohki, cmap='gray')
    f, ax = plt.subplots()
    ax.hist(ohki.ravel(), bins=np.arange(256))
    edges = filters.sobel(ohki)
    f, ax = plt.subplots()
    ax.imshow(edges, cmap='gray')
    ````

- edge-based segmentation:
    ```python
    from skimage.feature import canny
    edges = canny(ohki, sigma=1.5)
    from scipy import ndimage
    mask = ndimage.binary_fill_holes(edges)
    f, ax = plt.subplots()
    ax.imshow(mask, cmap='gray')
    ````

- watershed-based segmentation:







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



