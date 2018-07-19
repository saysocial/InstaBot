from setuptools import setup

__version__ = '0.0.1'
__author__ = 'saysocial'

requirements = [
    'selenium==2.53.6',
    'clarifai==2.0.32',
    'pyvirtualdisplay',
    'emoji'
]

description = 'none'

setup(
    name='instagram_py',
    version=__version__,
    author=__author__,
    author_email='07saysocial@gmail.com',
    url='https://github.com/saysocial/InstaBot',
    py_modules='instapy',
    description=description,
    install_requires=requirements,
    packages=['instapy'],
    include_package_data=True,
)
