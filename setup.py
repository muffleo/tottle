import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("tottle/const.py", "r") as f:
    exec(f.read())

setuptools.setup(
    name="tottle",
    version=locals()["__version__"],
    author=locals()["__author__"],
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
