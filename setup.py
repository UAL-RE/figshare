import setuptools

setuptools.setup(
    name='figshare',

    # This repo was original forked from cognoma (https://github.com/cognoma/figshare).
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.3.5',

    description='Figshare client for Research Engagement of  University of Arizona Libraries data curation',

    # The project's main homepage.
    url='https://github.com/UAL-RE',

    # Author details
    author='UAL-RE',

    # Choose your license
    license='BSD 3-Clause',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
    ],

    # What does your project relate to?
    keywords='redata data repository figshare',
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=setuptools.find_packages(),
    
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'requests == 2.32.3',
        'pytest == 8.3.5',
    ],

    # pytest integration
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
