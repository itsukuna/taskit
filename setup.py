from setuptools import setup

setup(
    name="taskit",
    version="0.1",
    py_modules=["taskit"],
    entry_points={"console_scripts": ["taskit=taskit:main"]},
)
