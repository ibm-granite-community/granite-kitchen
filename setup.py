from setuptools import setup, find_packages

setup(
    name='granite-kitchen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "ibm-granite-community-utils @ git+https://github.com/ibm-granite-community/utils",
        "langchain_community<0.3.0",
        "langchain_ollama<0.2.0",
        "replicate",
    ],
    author='The IBM Granite Community Team',
    description='A collection of setup instructions and component recipes for IBM Granite Community notebooks.',
    url='https://github.com/ibm-granite-community/granite-kitchen',
    keywords='notebook colab api key granite kitchen',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
