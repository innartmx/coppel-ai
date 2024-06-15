from setuptools import setup, find_packages

setup(
    name='Coppel AI',
    version='1.0',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    packages=find_packages()
)