from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-Project1",
    version = "0.1",
    author = "DEVNEEL",
    packages = find_packages(),
    install_requires = requirements,
)