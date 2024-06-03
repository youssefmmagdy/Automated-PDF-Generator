from setuptools import setup, find_packages

setup(
    name='PDF4RoomKey',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-decouple==3.8',
        'requests==2.31.0',
        'fpdf==1.7.2'
    ],
    entry_points={
        'console_scripts': [
            'pdf4roomkey=PDF4RoomKey.index:main',
        ],
    },
)