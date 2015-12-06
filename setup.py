try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple Pushbullet client',
    'author': 'Andrea Pivetta',
    'url': '',
    'download_url': '',
    'author_email': 'vanpivix@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['pusher'],
    'name': 'pusher'
}

setup(**config)