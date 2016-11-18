from distutils.core import setup


setup(
    name='ye-na-aas',
    version='0.1.0',
    packages=['yeah_nah_aas'],
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires=[
        'flask'
    ]
)