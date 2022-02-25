from setuptools import setup, find_packages


setup(
    name='ntkutils',
    version='1.0',
    license='MIT',
    author="not-nef",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/not-nef/ntkutils',
    keywords='ntkutils',
)