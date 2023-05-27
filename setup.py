from setuptools import setup, find_packages

setup(
    name='version-checker',
    version='0.0.3',
    author='Rafaellinos',
    url='https://github.com/Rafaellinos/version-checker',
    description='Check the version of your python packages',
    package_dir={'': "src"},
    packages=find_packages("src"),
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'check-version=version_checker.__main__:main',
        ]
    },
)
