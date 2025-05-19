from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Australian Weather Prediction - CI/CD Pipeline",
    description="A CI/CD pipeline for Australian weather prediction using Python, Docker, GitHub Actions, CircleCI, and GitLab.",
    version="0.1",
    author="Renswick Delvar",
    author_email="renswick.delver@gmail.com",
    packages=find_packages(include=['src', 'src.*']),
    install_requires = requirements,
)