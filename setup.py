from setuptools import find_packages
from setuptools import setup

install_requires = ['numpy', 'tensorflow', 'slackclient', 'matplotlib<=2.2.3', 'six']
tests_require = ['pytest>=3.2.0', 'mock']
setup_requires = ["pytest-runner"]

setup(
    name='research_utils',
    version='0.0.1',
    description='For my research utils',
    author='Shunichi Sekiguchi',
    author_email='quick1st97@keio.jp',
    install_requires=install_requires,
    url='https://github.com/Shunichi09/Utils',
    license='MIT License',
    packages=find_packages(exclude=('tests')),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require
)