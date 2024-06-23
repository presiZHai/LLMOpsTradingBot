from setuptools import find_packages, setup

setup(
     name = "financebot",
     version="0.01",
     author="Wale Ogundeji",
     author_email="waleabiodun85@gmail.com",
     packages=find_packages(),
     install_requires=["langchain", "langchain-openai", "langchain-astradb", "datasets", "pypdf", "python-dotenv", "flask"]
)