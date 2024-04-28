from setuptools import find_packages, setup

setup(
    name= 'mcqgenerator',
    version= '0.0.1',
    author= 'brijesh kapadiya',
    author_email= 'brijesh29.it11@gmail.com',
    install_requires= ['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)
