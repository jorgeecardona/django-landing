from setuptools import setup, find_packages


setup(
    name='djlanding',
    version='0.1.3',
    description='Basic landing page for Django projects.',
    author='NuageHQ',
    author_email='djlanding@nuagehq.com',
    license='BSD',
    keywords='landing django',
    url='http://pypi.python.org/pypi/djlanding/',
    packages=find_packages(),
    install_requires=[
        'greatape',
        ])
