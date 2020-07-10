from setuptools import setup, find_packages

setup(
    name='ictk',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
		'tqdm'
    ],
    entry_points='''
        [console_scripts]
        ictk=ictk.main:cli
    ''',
)