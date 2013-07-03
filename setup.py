try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Search',
    'author': 'Tomas Bjerre',
    'url': 'http://bjurr.se/',
    'download_url': 'http://bjurr.se/',
    'author_email': 'tomasbjerre@yahoo.com',
    'version': '0.1',
#    'install_requires': ['nose'],
    'packages': ['pythonsearch'],
    'scripts': [],
    'name': 'pythonsearch'
}

setup(**config)