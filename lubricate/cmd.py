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
import venv
from docopt import docopt
import lubricate as lc

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_PATH = os.path.join(BASE_PATH, "templates")
TEMPLATES = {t: os.path.join(TEMPLATES_PATH, t) for t in ["base", "analysis"]}
VENV_FOLDER = "venv"


def initialise_project(path, kind):
    """The main initialisation routine to create a project."""
    if os.path.exists(path):
        print("The folder named '{}' already exists, exiting." .format(path))
        exit(1)
    create_folder_structure(path, kind)
    initialise_git(path)
    create_virtualenv(path)
    install_packages(path)
    print("A new project was successfully initialised in '{}'.".format(path))


def create_folder_structure(path, kind):
    """Creates the folder structure in the given path"""
    shutil.copytree(TEMPLATES[kind], path)
    merge_folders(TEMPLATES[kind], path)


def merge_folders(source, destination):
    """Copy all files to the destination and overwrite existing files."""
    for src_dir, dirs, files in os.walk(source):
        dst_dir = src_dir.replace(source, destination, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)


def initialise_git(path):
    """Initialise a Git repository"""
    base_cmd = ["git", "-C", path]
    subprocess.run(base_cmd + ["init"])
    subprocess.run(base_cmd + ["add", "."])
    subprocess.run(base_cmd + ["commit", "-m", "Initial commit"])


def create_virtualenv(path):
    venv.create(os.path.join(path, VENV_FOLDER), with_pip=True)


def install_packages(path):
    pip_cmd = os.path.join(path, VENV_FOLDER, "bin", "pip")
    with open(os.path.join(path, "requirements.txt")) as fobj:
        for package in fobj.readlines():
            subprocess.run([pip_cmd, "install", package])


def main():
    args = docopt(__doc__)

    if args["--version"]:
        print(lc.version)

    if args["new"]:
        initialise_project(args["PROJECT_PATH"], kind="analysis")


if __name__ == "__main__":
    main()
