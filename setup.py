from setuptools import setup

import lubricate

setup(name='lubricate',
      version=lubricate.__version__,
      url='https://github.com/tamasgal/lubricate/',
      description='Lubricate helps you decrease friction when stuck at' \
                  'starting a coding project.',
      author='Tamas Gal',
      author_email='himself@tamasgal.com',
      packages=['lubricate'],
      include_package_data=True,
      platforms='any',
      install_requires=[
          'docopt',
      ],
      entry_points={
          'console_scripts': [
              'lubricate=lubricate.app:main',
          ],
      },
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
      ],
)

__author__ = 'Tamas Gal'
