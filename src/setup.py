from setuptools import setup, find_packages
from os import listdir

res_directories = 'res/images', 'res/sounds'
data_files = [(dir_name, [dir_name + "/" + filename for filename in listdir(dir_name)]) for dir_name in res_directories]


setup(name='trajtrackerp',
      version='0.1.0',
      description='Trajectory-tracking experiment scripts',
      url='http://trajtracker.com',
      author='Dror Dotan',
      author_email='dror@trajtracker.com',
      license='GPL',
      packages=find_packages(),
      install_requires=['trajtracker'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6'
      ],
      data_files=data_files,
      zip_safe=False)
