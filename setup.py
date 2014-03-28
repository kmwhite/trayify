from setuptools import setup, find_packages
setup(
    name = "trayify",
    version = "0.0.3",
    packages = find_packages(),
    scripts = [],

    # Purposely left empty. This could contain PyQT or PyGTK, but we're not
    # enforcing that a package be installed on the machine before we can be
    # used. If someone only wants GTK apps, they shouldn't be required to have
    # the PyQT libraries installed as well.
    install_requires = [],

    package_data = {
        'trayify': ['*.py'],
    },

    # metadata for upload to PyPI
    author = "Kristofer M White",
    author_email = "me@kmwhite.net",
    description = "A python module for super simple system tray applications",
    license = "BSD",
    keywords = "system tray gtk qt",
    url = "http://kmwhite.github.com/trayify/",
)
