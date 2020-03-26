__version__ = '0.2.0'
__author__ = 'Sondre Lillebø Gundersen'

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

setup(
    name='django-qc',
    version=__version__,
    description='DB utility to help you catch query inefficiencies in Django.',
    py_modules=['django_qc'],
    include_package_data=True,
    long_description=readme + '\n\n' + changelog,
    license='BSD',
    author=__author__,
    author_email='sondrelg@live.no',
    url='https://github.com/sondrelg/django-query-counter',
    download_url='https://pypi.org/project/django-qc',
    packages=find_packages(exclude=['']),
    install_requires=['django'],
    keywords=['orm', 'database', 'queries', 'testing', 'performance'],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
)
