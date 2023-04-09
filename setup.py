from setuptools import setup, find_packages
import pathlib

path = pathlib.Path(__file__).parent.resolve()

description = (path / "README.md").read_text(encoding="utf-8")

setup(

    name="Veezum",
    version="0.1",
    long_description=description,
    description="Obscure Scrapper/Telegram Bot",
    url="https://github.com/KayserSoze42/Veezum",

    entry_points = {
        'console_scripts': [
            'Veezum=veezum.veezum:main'
            ],
    },

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3, <4",
    install_requires=["schedule", "selenium", "requests", "webdriver_manager"]

)