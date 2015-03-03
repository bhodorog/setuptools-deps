import setuptools


class RelmListDependencies(setuptools.Command):
    description = """Print the list of dependencies of this project"""

    user_options = [
        ("pname=", "p", "Print just the named dependency")
    ]

    def initialize_options(self):
        self.pname = None

    def finalize_options(self):
        pass

    def run(self):
        self.distribution.install_requires
        self.distribution.extras_requires
