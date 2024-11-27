from setuptools import find_packages
from setuptools import setup

setup(
    name='Sample_package',
    version='0.1',
    description='A package for predictions using a trained ML model',
    author='Yamini Yamali',
    author_email='yamini.yamali@tigeranalytics.com',
    packages=find_packages(),
    install_requires=[
        'numpy','pandas',  
    ],
    include_package_data=True,
)