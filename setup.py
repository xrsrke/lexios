from setuptools import setup, find_packages

def read_file(fpath):
  with open(fpath) as fp:
    data = fp.read()
  return data

setup(
  name = 'lexios',
  version = '0.0.1',
  author = 'xariusrke',
  author_email = 'b3f0cus@icloud.com',
  maintainer = 'xariusrke',
  url = 'https://github.com/xrsrke/lexios',
  python_requires = '>=3.7',
  install_requires = read_file('requirements.txt').split('\n'),
  description = 'A symbolic framework for scientific computation',
  license = 'GPL-3.0',
  keywords = 'symbolic framework',
  packages = find_packages(),
  long_description = read_file('README.md'),
  long_description_content_type='text/markdown'
)