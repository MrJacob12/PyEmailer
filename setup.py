from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='PyMails',
  version='0.0.3',
  description='Simple tools for sending mail',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/MrJacob12/PyMails',  
  author='MrJacob',
  author_email='jacob@fern.fun',
  license='MIT', 
  classifiers=classifiers,
  keywords='email', 
  packages=find_packages(),
  install_requires=[''] 
)
