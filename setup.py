import setuptools

with open("README.md",'r') as ld:
    long_description = ld.read()

setuptools.setup(
    name="pendfetch",
    version="1.0.0",
    author="Nekurone",
    author_email="florencesecure@protonmail.com",
    description="A small double pendulum based neofetch clone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nekurone/double-pendulum-ascii/",
    py_modules = ["pendulum",'grabsys'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Terminals"
    ],
    install_requires=[
        'windows-curses; platform_system == "Windows"'
    ],
    entry_points = {
        "console_scripts":[
            "pendfetch=pendulum:main"
        ]
    },
    python_requires=">=3.6",
)
