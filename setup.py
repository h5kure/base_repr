import setuptools

with open("README.rst", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="base_repr",
    version='1.0.0',
    author="Hyouk Oh",
    author_email="h.5.kure@gmail.com",
    description="This is for representation of Python data (int, bytes, str) in the desired base system, "
                "like base62 system.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/h5kure/base_repr.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
