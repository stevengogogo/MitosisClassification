import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
def video2gif(imgs, obs_stages, pred_stages, figsize = (7,7), dpi=70, interval=50, savepath=None,fps=60):
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
        try:
            time_text.set_text("Frame: {}, Observed Status: {}, Predicted Status: {}".format(i, obs_stages[i], pred_stages[i]))
            if obs_stages[i] == pred_stages[i]:
                time_text.set_color('white')
            else:
                time_text.set_color('red')
        except:
            time_text.set_text("Frame: {}".format(i))
            time_text.set_color('white')
        return line, time_text
    
    ani = animation.FuncAnimation(fig, animate, frames=imgs.shape[0], interval=interval, blit=True, init_func=init)
    
    if savepath != None:
        ani.save(savepath, writer='imagemagick', fps= fps)
    
    return ani 