from setuptools import find_packages
from setuptools import setup

install_requires = ['numpy', 'matplotlib', 'pandas']
tests_require = ['pytest']
setup_requires = ["pytest-runner"]

setup(
    name='utils',
    version='0.0.1',
    description='Useful functions for my research',
    author='Shunichi Sekiguchi',
    author_email='quick1st97of@gmail.com',
    install_requires=install_requires,
    url='https://github.com/Shunichi09/Utils',
    license='MIT License',
    packages=find_packages(exclude=('tests')),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require
)