from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='rishabh amga',
    author_email='rishbahamga@gmail.com',
    install_requires=['openai','langchain','streamlit','python', 'PyPDF2', 'charset-normalizer'],
    packages = find_packages()
)