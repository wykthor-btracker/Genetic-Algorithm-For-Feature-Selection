from setuptools import setup

setup(
    name = "GeneAlgo",
    version="0.1dev",
    author="Wykthor Gabriel",
    url="https://github.com/wykthor-btracker/Genetic-Algorithm-For-Feature-Selection",
    author_email ="wykthor.g@wgvale.com",
    long_description=open("README.txt").read(),
    packages=["AttributeUsage","CSVManipulation","MachineLearningProtocols"],
    install_requires=["pandas","scikit-learn","numpy"]
)
