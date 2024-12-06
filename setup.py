from setuptools import setup, find_packages

setup(
    name="racestorm",
    author="Pablo Magarinos",
    author_email="pablo.magarinos@outlook.com",
    version="0.0.1.dev1",
    #packages=find_packages(),
    packages=["racestorm"],
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
    ], 
    description="Race strategies and risk management for motorsport.",
    license="GPLv3",
)
