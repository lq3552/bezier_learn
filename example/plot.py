import matplotlib.pyplot as plt
import numpy as np

from prepare_point import patch_clamp_prepare_point
from prepare_point import patch_clamp_ref_prepare_point
from prepare_point import arrow_prepare_point
from bezier_learn import PatchClamp

#TODO: much more elegant reference transformation (translation / reflection)#

pipette_control_points = patch_clamp_prepare_point("./data/patchClamp.txt")
refs_orig = np.loadtxt("./data/patchClampRefs.txt")
refs = patch_clamp_ref_prepare_point("./data/patchClampRefs.txt")
arrows = arrow_prepare_point("./data/arrows.txt")

i = 0
for ref in refs:
	pclamp = PatchClamp(control_points = pipette_control_points, ref_point = ref)
	beziers = pclamp.bezier_curve(np.linspace(0,1,50))
	for bezier in beziers:
		plt.plot(*bezier.T, 'b', lw = 0.8)
	cell_control_points = patch_clamp_prepare_point(f"./data/cell{i}.txt", ref = refs_orig[i])
	pclamp = PatchClamp(control_points = cell_control_points, ref_point = ref)
	beziers = pclamp.bezier_curve(np.linspace(0,1,50))
	for bezier in beziers:
		print(*bezier.T)
		plt.plot(*bezier.T, 'r', lw=0.8)
	i += 1

for arrow in arrows:
	x0, y0 = arrow[0]
	x1, y1 = arrow[1]
	dx, dy = x1 - x0, y1 - y0
	plt.arrow(x0,y0,dx,dy, width = 0.8, head_width = 4, facecolor = 'black', edgecolor = None) # width: ax.transData
	

plt.gca().set_aspect('equal')
plt.axis('off')
#plt.gca().axes.get_yaxis().set_visible(False)
#plt.gca().axes.get_xaxis().set_visible(False)
plt.savefig("BiuBiu.png",dpi=300)
#plt.show()
