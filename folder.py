"""This program makes a new folder and creates some files in the folder"""
import os
import logging

curr_path = os.getcwd()
name_of_folder = "Natural_Numbers"

logging.getLogger().setLevel("INFO")

path = os.path.join(curr_path, name_of_folder)


def make_directory():
    try:
        os.mkdir(path)
        logging.info("Folder is created")
    except FileExistsError:
        logging.info("Folder is already present")


def create_file():
    number_of_file = 10
    for number in range(1, number_of_file+1):
        cwd = os.path.join(path, f"{str(number)}.txt")
        writing_file = open(cwd, "a+")
        writing_file.write(str(number))
    logging.info("Files are written")


if __name__ == "__main__":
    make_directory()
    create_file()
