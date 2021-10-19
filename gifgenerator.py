#%%
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
from skimage.io import imread
import numpy as np 
from skimage.segmentation import mark_boundaries

def video2gif(imgs, obs_stages, pred_stages, entropys=None, max_entropy=None,
            figsize = (7,7), dpi=70, interval=50, 
            savepath=None,fps=60):
    """
    Save Video to GIF
    Example: ani = PlayAnimation(video[:,60:260,60:290], obs_stages=[], pred_stages=[], savepath='test.gif', fps=60)
    """
    fig = plt.figure(figsize=figsize)
    fig.set_dpi(dpi)
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    ax = fig.add_subplot(111)
    line = ax.imshow(imgs[0,:,:])
    time_text = ax.text(0.02, 0.95,'',transform=ax.transAxes, color='white') # Label frame number
    ax.set_axis_off()
    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove Borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    fig.add_axes(ax)
    
    def init():
        line.set_data(imgs[0,:,:])
        time_text.set_text(str(0))
        return line, time_text
    
    def animate(i):
        line.set_data(imgs[i,:,:])
        if True:
            if entropys == None:
                time_text.set_text("Frame: {}\nObserved Status: {}\nPredicted Status: {}".format(i, obs_stages[i], pred_stages[i]))
            else:
                time_text.set_text("Frame: {}\nObserved Status: {}\nPredicted Status: {}\nEntropy: {}/{}".format(i, obs_stages[i], pred_stages[i], entropys[i], max_entropy))
            if obs_stages[i] == pred_stages[i]:
                time_text.set_color('white')
            else:
                time_text.set_color('red')
        else:
            time_text.set_text("Frame: {}".format(i))
            time_text.set_color('white')
        return line, time_text
    
    ani = animation.FuncAnimation(fig, animate, frames=imgs.shape[0], interval=interval, blit=True, init_func=init)
    
    if savepath!=None:
        ani.save(savepath, writer='imagemagick', fps= fps)
    
    return ani 

def get_image(filename, loc=None):
    imgs = imread(filename)
    if loc == 'nuc':
        imgs = imgs[:,60:260,60:290,0]
    elif lic == 'mito':
        imgs = imgs[:,60:260,60:290,1]  
    return imgs

def video2gif_mask(imgs, masks, obs_stages, pred_stages, entropys=None, max_entropy=None,figsize = (7,7), dpi=70, interval=50, savepath=None,fps=60):
    """
    Arguments:
        imgs: (t, 200,230)
        masks: (t, 200,230)
        obs_stages: list. t in length
        pred_stages: list. t in length
    """
    mark_imgs = []
    for i in range(0, imgs.shape[0]):
        mark_imgs.append(mark_boundaries(imgs[i]/255 , masks[i]))
    ani = video2gif(np.array(mark_imgs), 
                    obs_stages, 
                    pred_stages, 
                    entropys=entropys, 
                    max_entropy=max_entropy,
                    figsize = figsize, 
                    dpi=dpi, 
                    interval=interval, 
                    savepath=savepath,fps=fps)
    return ani



def half(l):
    s = []
    for i, e in enumerate(l):
        if i %2 ==0:
            continue
        s.append(e)
    return np.array(s)

def to_mitostage(obs_indexes):
    d = {
        0:'anaphase', 
        1:'concentration', 
        2:'cytokinesis', 
        3:'g0', 
        4:'stretching'}
    obs_stages = []
    for i in obs_indexes:
        obs_stages.append(d[i])
    return obs_stages

def max_entropy(N_cat):
    N_cat = float(N_cat)
    return -N_cat*(1/N_cat * np.log2(1/N_cat))

def round_vec(vec, decimal = 2):
    return [format(i, '.{}f'.format(decimal)) for i in vec]

if __name__ == '__main__':

    """
    SETTING
    """

    locs = ['mito', 'nuc']
    IDs = [
        '11302017_c3_dual_decon-normal',
        '12282017_dual_decon_c3-normal',
        '12282017_dual_decon_c3-normal',
        '12292017_dual_decon_c40',
        '12292017_dual_decon_c40'
    ]
    n_category = 5


    def loaddata(ID, loc):
    

        masks = np.load('data/masks_{}_{}.npy'.format(ID, loc))
        obs_stages = to_mitostage(np.load('data/observe_stages_{}.npy'.format(ID)))
        preds = np.load('data/preds_{}_{}.npy'.format(ID, loc))
        temps = np.load('data/temps_{}_{}.npy'.format(ID, loc))
        entropys = np.load('data/entropy_{}_{}.npy'.format(ID, loc))
        return masks,obs_stages,preds,temps,entropys


    for ID in IDs:
        for loc in locs:
            if True:
                masks,obs_stages,preds,temps,entropys = loaddata(ID, loc)
                
                while masks.shape[0] < temps.shape[0]:
                    temps = half(temps)

                video2gif_mask(temps, 
                                masks, 
                                obs_stages, 
                                preds, 
                                entropys = round_vec(entropys),
                                max_entropy = format(max_entropy(n_category), '.2f'),
                                figsize = (7,7), 
                                dpi=70, 
                                interval=50, 
                                savepath='VIDEO_exlpain_{}_{}.gif'.format(ID, loc),
                                fps=10)

                print('SAVED: {}'.format('VIDEO_exlpain_{}_{}.gif'.format(ID, loc)))
            else:
                print('FAILED: {}'.format('VIDEO_exlpain_{}_{}.gif'.format(ID, loc)))
                pass

    print('DONE')