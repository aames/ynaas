from distutils.core import setup


setup(
    name='ye-na-aas',
    version='1.0.0',
    packages=['yeah_nah_aas'],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'flask'
    ]
)