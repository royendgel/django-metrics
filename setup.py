import os
from setuptools import setup, find_packages

from django_metrics import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-metrics',
    version=".".join(map(str, VERSION)),
    description='django-metrics is a reusable Django application for tracking and emailing application metrics.',
    long_description=readme,
    author='Royendgel Silberie',
    author_email='rsilberie@techprocur.com',
    url='https://github.com/Easycomputer/django-metrics',
    packages=find_packages(),
    package_data={
        'django_metrics': [
            'templates/django_metrics/*',
        ]
    },
    install_requires = [
        'celery',
        'django-celery',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)