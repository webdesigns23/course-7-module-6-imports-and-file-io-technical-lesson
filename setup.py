from setuptools import setup, find_packages

setup(
    name="imports_file_io_lesson",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Your Name",
    description="A simple project demonstrating Python imports and file I/O.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
