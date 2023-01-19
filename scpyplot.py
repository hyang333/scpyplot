# ax: matplotlib.pyplot.axes
# xlablel_pos: (left, bottom), axes fraction coords
# ylablel_pos: (left, bottom), axes fraction coords
# fontsize: 13

def arrowAxes(ax=ax, xlabel_pos=(0.26, 0.005), ylabel_pos=(0.005, 0.28), fontsize=13):
    ax.axis('off')
    ax.annotate("", xy=(0.02, 0.015), xycoords='axes fraction', textcoords='axes fraction', xytext=(0.02, 0.25), arrowprops=dict(arrowstyle="<-"))
    ax.annotate("", xy=(0.015, 0.02), xycoords='axes fraction', textcoords='axes fraction', xytext=(0.25,0.02), arrowprops=dict(arrowstyle="<-"))
    ax.text(xlabel_pos[0], xlabel_pos[1], s='UMAP-1', transform=ax.transAxes, fontsize=fontsize)
    ax.text(ylabel_pos[0], ylabel_pos[1],  s='UMAP-2', transform=ax.transAxes, rotation=90, fontsize=fontsize)
    
    return ax
