#!/usr/bin/env python3
"""
The analysis lubricator.

Usage:
    lubricate [options] new PROJECT_PATH
    lubricate (-h | --help)
    lubricate --version

Options:
    -h --help     Show this screen.
    -v            Verbose output.
    --version     Show the version.
"""
import os
import shutil
import subprocess
from docopt import docopt
import lubricate as lc

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_FOLDER = os.path.join(BASE_PATH, "template")


def initialise_project(path):
    """The main initialisation routine to create a project."""
    if os.path.exists(path):
        print("The folder named '{}' already exists, exiting." .format(path))
        exit(1)
    create_folder_structure(path)
    initialise_git(path)
    # name = os.path.basename(path)
    print("A new project was successfully initialised in '{}'.".format(path))


def create_folder_structure(path):
    """Creates the folder structure in the given path"""
    shutil.copytree(TEMPLATE_FOLDER, path)


def initialise_git(path):
    """Initialise a Git repository"""
    base_cmd = ["git", "-C", path]
    subprocess.run(base_cmd + ["init"])
    subprocess.run(base_cmd + ["add", "."])
    subprocess.run(base_cmd + ["commit", "-m", "Initial commit"])


def main():
    args = docopt(__doc__)
    print(args)

    if args["--version"]:
        print(lc.version)

    if args["new"]:
        initialise_project(args["PROJECT_PATH"])


if __name__ == "__main__":
    main()
