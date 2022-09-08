import numpy as np
from scipy.interpolate import BPoly
import copy 

class PatchClamp(object):
	"""
	Contains the controll points and the Bezier curves defined by the points 
	to plot axisymmetric patch clamp.

	parameters:
		ref_points (ndarray, shape(2)): reference point, relative to the origin
		n_spline (int): number of splines
		control_points: (ndarray, shape(n_spline,4,2): control points defining one Bezier curve
	"""
	## TODO: exception handler ##
	def __init__(self, ref_point = np.array([0,0]), n_spline = 1, control_points = None):
		self.ref_point = ref_point
		if np.all(control_points == None):
			self.control_points = np.zeros((self.n_spline,4,2))
		else:
			self.control_points = control_points
		self._mirror(0);
		self.control_points += ref_point
		self.n_spline = self.control_points.shape[0]
		

	## TODO: exception handler ##
	def set_control_points(self, control_points):
		"""
		At the moment it is more of a place holder than a real method,
		though it is functional, it cannot handle exceptions or parsing a variety of inputs
		"""
		self.control_points = control_points


	def bezier_curve(self, t):
		"""
		evaluate 3rd order Bezier curve defined by control points at t
		return: ndarray with elements ordered pair x(t), y(t)
		"""
		if t.max() > 1 or t.min() < 0:
			print("You are too stupid to use this script! Please read literatures about Bezier curve")
		curves = np.zeros((self.n_spline, t.shape[0], 2))
		for i in range(self.n_spline):
			curve = BPoly(self.control_points[i,:,None, :], [0, 1])
			curves[i] = curve(t)

		return curves

	def _mirror(self, axis):
		"""
		mirror control points of one electrode to obtain controll points for another
		at the moment the symetric axis is parallel to y-axis so it is defined by x only. 
		Why? Because I only need this function for plotting purpose, I am not confident of 
		my derivation, and most importantly, I am lazy :D
		"""
		control_points_mirrored = copy.deepcopy(self.control_points)
		control_points_mirrored[:,:,0] = 2 * axis - control_points_mirrored[:,:,0]
		self.control_points = np.concatenate((self.control_points, control_points_mirrored), axis = 0)
