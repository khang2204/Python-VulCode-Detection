from setuptools import setup, find_packages
import sys, os
from distutils import versionpredicate
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
version = '0.3.22'
install_requires = ['pymongo>=2.8,<3', 'pysaml2==1.2.0beta5',
    'python-memcached==1.53', 'cherrypy==3.2.4', 'vccs_client==0.4.1',
    'eduid_am>=0.5.3']
testing_extras = ['nose==1.2.1', 'coverage==3.6']
setup(name='eduid_idp', version=version, description=
    'eduID SAML frontend IdP', long_description=README, classifiers=[],
    keywords='eduID SAML', author='Fredrik Thulin', author_email=
    'fredrik@thulin.net', license='BSD', packages=['eduid_idp'],
    package_dir={'': 'src'}, zip_safe=False, install_requires=
    install_requires, extras_require={'testing': testing_extras},
    entry_points={'console_scripts': ['eduid_idp=eduid_idp.idp:main']})
