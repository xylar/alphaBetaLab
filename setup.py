from setuptools import setup

setup(
    name='alphaBetaLab',
    version='1.1.0',
    author='Lorenzo Mentaschi',
    author_email='lorenzo.mentaschi@unige.it',
    packages=['alphaBetaLab', 'alphaBetaLab.plot'],
    install_requires=[
        "cartopy >=0.21.1",
        "fiona >=1.9.1",
        "numpy >=1.8.2",
        "matplotlib >=3.5.3",
        "netcdf4 >=1.6.0",
        "pandas >=1.4.3 ",
        "scipy >=1.9.1",
        "shapely >=2.0.1,<3.0"
    ],
)