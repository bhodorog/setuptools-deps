from setuptools import setup, find_packages


setup(
    name="setuptools_relm",
    version="0.1",
    packages=find_packages(),
    author="Bogdan Hodorog",
    author_email="bogdan.hodorog@gmail.com",
    description="""setuptools extensions commands to deal with project"
    " dependencies of a python based package""",
    url="https://github.com/bhodorog/setuptools-deps.git",
    install_requires=[],
    entry_points={
        "distutils.commands": [
            "pd_test = prod_deploy.bento_pkgs:TestingGround",
        ], }
)

