"""Set up the pai project"""


from setuptools import setup

import pai

setup(
    name=pai.__name__,
    packages=[pai.__name__],
    version=pai.__version__,
    url='https://github.com/jalanb/%s' % pai.__name__,
    download_url='https://github.com/jalanb/%s/tarball/v%s' % (
        pai.__name__, pai.__version__),
    license='GPL License',
    author="jalanb",
    author_email='github@al-got-rhythm.net',
    description=pai.__doc__,
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[
        'pytest>=3.1.0',
        'pprintpp',
        'pdir',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
