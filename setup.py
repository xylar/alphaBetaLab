from setuptools import setup

setup(
    name='alphaBetaLab',
    version='1.1.0',
    author='Lorenzo Mentaschi',
    author_email='lorenzo.mentaschi@unige.it',
    packages=['alphaBetaLab', 'alphaBetaLab.plot'],
    install_requires=[
        "numpy >=1.8.2",
        "shapely >=2.0,<3.0",
        "basemap",
        "netcdf4",
        "pandas",
        "scipy"
    ],
)

