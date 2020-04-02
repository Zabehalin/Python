from subprocess import call
import os
if __name__ == "__main__":
    start


def start():
    exit = True
    while exit:
        vyb = int(
            input("1. Download movie\t2. Download movies plylist\t0. EXIT => "))
        if vyb == 1:
            URL = input("Enter movie url => ")
            get_movie(URL)
        elif vyb == 2:
            URL = input("Enter plylist url => ")
            get_plylist(URL)
        elif vyb == 0:
            exit = False
        else:
            print("Eroor --help")


def get_movie(URL):
    movie_info = "youtube-dl " + URL + " -F"
    call(movie_info.split(), shell=False)
    choice_format = input("Format code => ")
    command = "youtube-dl -f " + choice_format + " " + URL + " -c"
    os.chdir("Downloads")
    call(command.split(), shell=False)


def get_plylist(URL):
    command = "youtube-dl -f " + URL + " - c"
    os.chdir("Downloads_Plylist")
    call(command.split(), shell=False)
