# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '1.0.5'
tests_require = [
    'plone.app.testing',
    ]

setup(
    name='plone.app.lockingbehavior',
    version=version,
    description="Locking integration for dexterity content objects.",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),

    # Get more strings from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='dexterity locking behavior plone',
    author='Plone Foundation',
    author_email='mailto:dexterity-development@googlegroups.com',
    url='https://github.com/plone/plone.app.lockingbehavior/',
    license='GPL2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.locales >= 4.3.9',
        'plone.behavior',
        'plone.dexterity>=1.1',
        'plone.locking',
        ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
