from setuptools import find_packages
from setuptools import setup

setup(
    name="Sample_package",                # Name of the package
    version="0.1.0",                      # Package version
    author="Yamini Yamali",                   # Your name or organization
    author_email="yamini.yamali@tigeranalytics.com", # Your contact email
    description="A simple house price prediction package",  # Short description
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type="text/markdown",  # Use markdown for the README
    url="https://github.com/YaminiYamali/Sample_package",  # Optional: project URL
    packages=find_packages(),  # Automatically include all subpackages under Sample_package
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    classifiers=[  # Classifiers to help others find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # External dependencies (if any)
        "pandas",
        "scikit-learn",
        "numpy",
    ],
    python_requires='>=3.6',  # Minimum Python version
)
