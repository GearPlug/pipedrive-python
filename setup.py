from setuptools import setup

setup(name='pipedrive',
      version='0.1',
      description='API wrapper for Pipedrive written in Python',
      url='https://github.com/GearPlug/pipedrive-python',
      author='Yordy Gelvez',
      author_email='yordy.gelvez@gmail.com',
      license='GPL',
      packages=['pipedrive'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
