#paper every step relation and methodology
#implicit function torch autograd, how about with multiple inputs (>2)? calculate by hand and compare
#how autograd related to eigen
#what does vjp do


#remove global_parser's dependency on inkstone class (check legume)
#add docmentation on function for user: explain params and funcionality/ for developer: explain why
#better name (backend)
#understand vector in vjp/jvp, why they are for forward/backward calculation

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding="utf-8") as f:
        return f.read()


setup(name='inkstone',
      version='0.3.15',
      description='3D efficient solver for multi-stacked in-plane periodic structures using rcwa.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/alexysong/inkstone',
      # check https://pypi.org/pypi?%3Aaction=list_classifiers for classifiers
      classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
      ],
      keywords='rcwa',
      author='Alex Y. Song',
      author_email='song.alexy@gmail.com',
      packages=find_packages(),
      install_requires=[
          'numpy >= 1.11.3',
          'scipy',
      ],
      zip_safe=False)
