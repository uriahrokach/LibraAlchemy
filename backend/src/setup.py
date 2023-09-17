from setuptools import setup, find_packages


def read_requirements(requirements_file: str = 'requirements.txt'):
    with open(requirements_file, 'r') as requirements:
        return list(requirements.readlines())


setup(
    name="alchemy_backend",
    version="0.0.1",
    author="Uriah Rokach",
    description="Backend for Libra Alchemy App",
    packages=find_packages(),
    requirments=read_requirements()
)