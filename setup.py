from distutils.core import setup
from setuptools import setup
import glob

subpackages = glob.glob("hypergan/*/")
subpackages += glob.glob("hypergan/*/*/")
subpackages += glob.glob("hypergan/*/*/*/")
subpackages = [s.replace("/", ".") for s in subpackages]

setup(
  name = 'hypergan',
  packages = ['hypergan']+subpackages,
  include_package_data=True,
  version = '0.10.2',
  description = 'A customizable generative adversarial network with reproducible configurations.  Build your own content generator.',
  author = 'HyperGAN',
  author_email = 'hypergan@protonmail.com',
  maintainer = "hypergan developers",
  maintainer_email = 'hypergan@protonmail.com',
  license = "MIT",
  url = 'https://github.com/255BITS/hypergan', 
  keywords = ['hypergan', 'neural network', 'procedural content generation', 'generative adversarial network', 'tensorflow'], # arbitrary keywords
  classifiers = [
      'Development Status :: 4 - Beta',
      'Topic :: Scientific/Engineering :: Artificial Intelligence', 
      'Topic :: Artistic Software', 
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      'Intended Audience :: Science/Research',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Operating System :: POSIX',
      'Operating System :: Unix',
      'Operating System :: MacOS',
      ],
  platforms = ["Linux", "Mac OS-X", "Unix", "Windows"],
  scripts = ['bin/hypergan']
)
