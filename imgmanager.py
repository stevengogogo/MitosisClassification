from skimage.io import imread

def get_image(filename, loc=None):
    imgs = imread(filename)
    if loc == 'nuc':
        imgs = imgs[:,60:260,60:290,0]
    elif lic == 'mito':
        imgs = imgs[:,60:260,60:290,1]  
    return imgs

if __name__ == '__main__':
    filename = 'data/12282017_dual_decon_c15-normal.tif'
    imgs_nuc = get_image(filename, loc='nuc')