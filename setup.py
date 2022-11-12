import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='lexios',
      version='0.0.1',
      description='',
      author='xarius',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['lexios'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['numpy', 'requests', 'pillow', 'networkx'],
      python_requires='>=3.8',
      extras_require={
        'gpu': ["pyopencl", "six"],
        'testing': [
            "pytest",
            "mypy",
        ],
      },
      include_package_data=True)