import os
from setuptools import find_packages, setup

def find_yaml_files():
    yaml_files = []
    for root, dirs, files in os.walk("experiments"):
        for file in files:
            if file.endswith(".yaml"):
                yaml_files.append(os.path.join(root, file))
    print(yaml_files)
    return yaml_files

setup(
    name='pysot',
    version='0.0.1',
    python_requires='>=3.8  ',
    packages=find_packages(),
    package_data={"experiments": ["**/*.yaml"]},
    include_package_data=True,
    install_requires=[
        "yacs",
        "opencv-python-headless",
        "numpy"
    ],
    platforms=["linux"],
)
