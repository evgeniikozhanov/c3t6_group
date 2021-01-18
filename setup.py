from setuptools import setup, find_packages

version = '0.0.0'


DEPENDENCY_LINKS = []
REQUIRED = []


with open('requirements.txt', mode='r', encoding='utf-8') as f:
    requirements = f.read().splitlines()
for package in requirements:
    if not package.startswith('--'):
        REQUIRED.append(package)


setup(
    name='c3t6_group',
    version=version,
    description='Some implementations of methods to work with c3t6 groups',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Topic :: Theory of groups',
        'Intended Audience :: Developers',
    ],
    keywords='Some implementations of methods to work with c3t6 groups',
    url='',
    license='LGPLv2',
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=REQUIRED,
    dependency_links=DEPENDENCY_LINKS,
    zip_safe=True,
    include_package_data=True
)
