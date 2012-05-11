"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="zach",
    version="1.1",
    url="http://github.com/zachwill/import_zach",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    keywords=['zach', 'zachwill', 'zach will', 'useless'],
    description="See what Zach's been up to.",
    long_description="Just because.",
    packages=[
        'zach'
    ],
    license='Public Domain',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
