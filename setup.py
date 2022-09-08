from distutils.core import setup
from distutils import util
from bezier_learn import __version__ as version

setup(name='bezier_learn',
		version=version,
		description = 'A collection of classes of complex shapes \
					   defined by control points of Bezier curves',
        author = 'Qi Li',
        author_email=['lq3552@gmail.com'],
        url='https://github.com/lq3552/bezier_learn',
        requires=['numpy(>=1.12.0)', 'scipy(>=1.6.2)'],
        package_dir={'bezier_learn': 'bezier_learn'}, # the present directory maps to src 
        packages = ['bezier_learn']
     )
