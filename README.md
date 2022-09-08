# bezier_learn
This package containes classes of complex shapes defined by multiple control points of Bezier curves

## Dependance

`bezier_learn` requires:

 * python(>=3.5)
 * numpy(>=1.12.0)
 * scipy(>=1.6.2)

## Example

See `example\/` for examples that use classes of this package to plot complex shapes.
```python
from bezier_learn import PatchClamp

pclamp = PatchClamp(control_points = control_points, ref_point = ref_point)
beziers = pclamp.bezier_curve(np.linspace(0,1,50))
for bezier in beziers:
	plt.plot(*bezier.T, 'C0', lw = 0.8)
```
