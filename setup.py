from setuptools import setup
from ghPublish import _VERSION
setup(
    name='ghPublish',
    packages=['ghPublish'],
    version=_VERSION,
    description='Directly publish your blog posts to GitHub Pages from the command line.',
    long_description='Please visit https://github.com/MiteshNinja/ghPublish for more details.',
    author='Mitesh Shah',
    author_email='mitesh@miteshshah.com',
    url='https://github.com/MiteshNinja/ghPublish',
    download_url='https://github.com/MiteshNinja/ghPublish/tarball/' +
    _VERSION,
    keywords=['github', 'publish', 'blog', 'pages', 'cli'],
    classifiers=[],
    install_requires=[
        'pygments', 'mistune', 'requests'
    ],
    entry_points={
        'console_scripts': [
            'ghPublish=ghPublish:cli',
        ],
    })
