import os
from setuptools import setup
from category import __version__


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='category',
    version=__version__,
    packages=['category'],
    include_package_data=True,
    license='BSD License',    # example license
    description='A category for a django model.',
    long_description=README,
    author='Andreas.Neumeier',
    author_email='andreas@neumeier.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=1.9.0',
        'django-crispy-forms>=1.6.0',
        'djangorestframework>=3.6.0',
        'coreapi==2.1.1',
        'coreschema==0.0.4',
        'pyaml==16.12.2',
    ],
)
