from setuptools import setup


install_requires = [
    'pytest>=2.5',
]

setup(
    name='sandbox',
    version=__import__('sandbox').__version__,
    description='A sandbox project.',

    author='Benjamin Schwarze',
    author_email='benjamin.schwarze@mailboxd.de',
    maintainer='Benjamin Schwarze',
    maintainer_email='benjamin.schwarze@mailboxd.de',

    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],

    packages=['sandbox'],
    install_requires=install_requires,
    zip_safe=False,
)
