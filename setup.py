from setuptools import setup, find_packages
import cordport

setup(
    name='cordport',
    packages=find_packages(),
    version=cordport.__version__,
    description='Central Office Re-architecture as Datacenter(CORD) ovs debug tool',
    author=cordport.__author__,
    author_email='aweimeow.tw@gmail.com',
    license=cordport.__license__,
    entry_points={
        'console_scripts': [
            'port = cordport.__main__:main',
        ],
    },
)

