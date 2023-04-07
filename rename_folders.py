import os


def ls(ruta=os.getcwd()):
    return [os.path.abspath(arch.path) for arch in os.scandir(ruta) if arch.is_dir()]


# get the files name in the directories, and return if the file is a mp4 video
def get_files(ruta):
    return [arch.name for arch in os.scandir(ruta) if arch.name.endswith('.mp4')]


# rename the dir with the name of the file mp4 in the dir, without the extension
def rename_dir(ruta):
    for dir in ls(ruta):
        files = get_files(dir)
        print(files)
        if len(files) == 1:
            os.rename(dir, files[0][:-4])


# use rename_dir in this path
rename_dir(ruta=os.getcwd())
