from setuptools import setup, find_packages

setup(
    name='Pybot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'pyttsx3'
    ],
    entry_points={
        'console_scripts': [
            'pybot=Pybot1:Pybot_chat',
            'voice=voice:droid'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple Python chatbot and voice setup for demonstration',
    keywords='chatbot voice pyttsx3 nltk',
    url='http://github.com/yourgithub/pybot'
)
