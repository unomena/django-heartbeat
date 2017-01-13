from setuptools import setup, find_packages

setup(
    name='django-heartbeat',
    version='0.0.3',
    description='Django Heartbeat Application',
    author='Unomena',
    author_email='dev@unomena.com',
    url='http://unomena.com',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [],
    zip_safe=False,
)
