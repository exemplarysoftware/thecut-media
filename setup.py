from setuptools import setup, find_packages
from version import get_git_version

setup(name='media',
    author='The Cut', author_email='development@thecut.net.au',
    url='http://projects.thecut.net.au/projects/thecut-media',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['distribute', 'PIL==1.1.7',
        'django-photologue==2.3', 'sorl-thumbnail==3.2.5'],
    #obsoletes=['thecut<0.01-5-gcfad22b']
    )

