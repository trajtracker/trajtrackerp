from setuptools import setup, find_packages
from os import listdir
import trajtrackerp


ver = trajtrackerp.version()

setup(name='trajtrackerp',
      version='{:}.{:}.{:}'.format(ver[0], ver[1], ver[2]),
      description='Trajectory-tracking experiment scripts',
      url='http://trajtracker.com',
      author='Dror Dotan',
      author_email='dror@trajtracker.com',
      license='GPL',
      packages=find_packages(),
      install_requires=['trajtracker'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6'
      ],
      package_dir={'trajtrackerp': 'trajtrackerp'},
      package_data={'trajtrackerp': ['../trajtrackerp_res/sounds/*', '../trajtrackerp_res/images/*']},
      zip_safe=False)
