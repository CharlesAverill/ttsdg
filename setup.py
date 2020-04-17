import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttsdg",
    version="1.0.0",
    author="Charles Averill",
    author_email="charlesaverill20@gmail.com",
    description="A package to automate TTS data generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CharlesAverill/ttsdg",
    packages=['pyttsx3', 'pydub'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)