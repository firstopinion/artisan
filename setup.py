# stdlib
import os
from setuptools import setup, find_packages


# Use register to create temporary README.txt from README.md.
# Default incase README.txt was not created
long_description = 'CLI build tool to help ease the pain of developing emails.'
if os.path.exists('README.txt'): long_description = open('README.txt').read()


# Setup Package
setup(
    name = 'Artisan',
    version = '0.0.1',
    description = 'CLI build tool to help ease the pain of developing emails.',
    long_description = long_description,
    keywords = 'Artisan, Email, Premailer, Templating',
    url = 'firstopinion.github.io/artisan',
    author = 'Jarid Margolin',
    author_email = 'jaridmargolin@gmail.com',
    license ='MIT',
    install_requires = [
		'Jinja2==2.7',
		'premailer==1.2.2',
		'watchdog==0.6.0',
	],
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    entry_points = {
        'console_scripts': ['artisan = artisan:console']
    },
    test_suite = "artisan.tests.artisan_test"
)