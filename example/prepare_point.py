import numpy as np

def _invert_y(pts_in, ref):
	ref = ref
	dat = np.loadtxt(pts_in)
	dat -= ref
	dat[:,1] = - dat[:,1]
	return dat

def patch_clamp_prepare_point(pts_in, ref = np.array([551.76, 127.072])):
	"""
	 partition the points into several groups of 4 points,
	 change the reference point to the origin,
	 and invert the y-axis
	"""
	dat = _invert_y(pts_in, ref)
	npts = dat.shape[0]
	return dat.reshape((npts // 4, 4 ,2))

def patch_clamp_ref_prepare_point(pts_in, ref = np.array([551.76, 127.072])):
	dat = _invert_y(pts_in, ref)
	return dat

def arrow_prepare_point(pts_in, ref = np.array([551.76, 127.072])):
	dat = _invert_y(pts_in, ref)
	npts = dat.shape[0]
	return dat.reshape((npts // 2, 2, 2))


if __name__ == "__main__":
	pass
