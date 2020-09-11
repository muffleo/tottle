import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="tottle",
    version="0.2.1",
    author="muffle",
    description="Fast async Telegram API wrapper built by community",
    url="https://github.com/muffleo/tottle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements
)