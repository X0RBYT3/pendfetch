import setuptools

with open("README.md",'r') as ld:
    long_description = ld.read()

setuptools.setup(
    name="double-pendulum",
    version="1.0.3",
    author="Nekurone",
    author_email="florencesecure@protonmail.com",
    description="A small double pendulum simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nekurone/double-pendulum-ascii/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Terminals"
    ],
)
