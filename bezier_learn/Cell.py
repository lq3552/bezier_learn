import numpy as np
from scipy.interpolate import BPoly
import copy 

class Cell(object):
	"""
	[Currently EMPTY]
	Contains the controll points and the Bezier curves defined by the points 
	to plot cells of any shape.

	parameters:
		ref_points (ndarray, shape(2)): reference point, relative to the origin
		n_spline (int): number of splines
		control_points: (ndarray, shape(n_spline,4,2): control points defining one Bezier curve
	"""
	def __init__(self, ref_point = np.array([0,0]), n_spline = 1, control_points = None):
		pass
