import setuptools

with open("README.md", "r", encoding="utf-8") as stream:
    long_description = stream.read()

setuptools.setup(
    name="urdf-inertia-script",
    version="1.1",
    author="Anthony Lew",
    author_email="anthony@v01dbreaker.com",
    description="A Python script used to modify generated URDFs and recalculate inertias. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/V01DBREAKER/urdf-inertia-script",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "urdf-modifier=src:script.main",
            "inertia-calc=src:manual.main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="robot robotics urdf gazebo ros kinematics",
    install_requires=[
        "pymeshlab",
    ],
    include_package_data=True,
    package_data={"": ["README.md"]},
    python_requires=">=3.12",
)