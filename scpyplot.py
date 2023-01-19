fig, ax = plt.subplots()

x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))

ax.axis('off')

ax.annotate("", xy=(0.02, 0.015), xycoords='axes fraction', textcoords='axes fraction', xytext=(0.02, 0.25), arrowprops=dict(arrowstyle="<-"))
ax.annotate("", xy=(0.015, 0.02), xycoords='axes fraction', textcoords='axes fraction', xytext=(0.25,0.02), arrowprops=dict(arrowstyle="<-"))
ax.text(.26, 0.01, s='UMAP-1', transform=ax.transAxes)
ax.text(0.01, 0.26,  s='UMAP-2', transform=ax.transAxes, rotation=90)
