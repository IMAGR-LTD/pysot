import os
from distutils.extension import Extension
# from Cython.Build import cythonize
from setuptools import find_packages, setup


def find_yaml_files():
    yaml_files = []
    for root, dirs, files in os.walk("experiments"):
        for file in files:
            if file.endswith(".yaml"):
                yaml_files.append(os.path.join(root, file))
    print(yaml_files)
    return yaml_files


ext_modules = [
    Extension(
        name='toolkit.utils.region',
        sources=[
            'toolkit/utils/region.pyx',
            'toolkit/utils/src/region.c',
        ],
        include_dirs=[
            'toolkit/utils/src'
        ]
    )
]


setup(
    name='pysot',
    version='0.0.1',
    python_requires='>=3.7',
    packages=find_packages(),
    data_files=[("configs", find_yaml_files())],
    include_package_data=True,
    install_requires=[
        "yacs",
        "opencv-python-headless",
        "numpy"
    ],
    # ext_modules=cythonize(ext_modules),
    platforms=["linux"],
)
