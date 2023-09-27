from setuptools import setup, find_packages

setup(
    name='gh-index',
    version='0.1',
    packages=find_packages(),
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        gh-index=cli.main:cli
    ''',
)
