from setuptools import setup, find_packages
from version import get_git_version


setup(
    name='thecut-media',
    author='The Cut',
    author_email='development@thecut.net.au',
    url='https://projects.thecut.net.au/projects/thecut-media',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['djangorestframework>=2.3.13', 'python-magic>=0.4.6',
                      'pillow>=2.0.0', 'sorl-thumbnail>=11.12.1b,<12'],
)
