from setuptools import setup, find_packages
from bot_utils import version, package_name

package_config = {
    'name': package_name,
    'version': version,
    'packages': find_packages(exclude=['*test*', 'examples']),
    'url': 'https://github.com/jtara1/bot_utils',
    'license': 'Apache-2.0',
    'author': 'James T',
    'author_email': 'github.jtara1@gmail.com',
    'description': 'visual scripting, macros, bot tools'
}

setup(**package_config)
