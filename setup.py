import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pipedrive-python-lib',
      version='0.1.0',
      description='API wrapper for Pipedrive written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/pipedrive-python',
      author='Yordy Gelvez',
      author_email='yordy.gelvez@gmail.com',
      license='GPL',
      packages=['pipedrive'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
