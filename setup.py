from setuptools import setup, find_packages

setup(
    name="egat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy", "pandas", "matplotlib", "seaborn", "scipy", "scikit-learn", "geopandas", "rasterio"
    ],
)