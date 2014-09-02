#noinspection PyUnusedLocal
def copy(source, destination):
    """Copy file to destination, returns true/false.

    source: string - file to copy.
    destination: string - destination file

    Example:
        success = xbmcvfs.copy(source, destination)"""
    return bool

#noinspection PyUnusedLocal
def delete(file):
    """Deletes a file.

    file: string - file to delete

    Example:
        xbmcvfs.delete(file)"""
    pass

#noinspection PyUnusedLocal
def rename(file, newFileName):
    """Renames a file, returns true/false.

    file: string - file to rename
    newFileName: string - new filename, including the full path

    Example:
        success = xbmcvfs.rename(file,newFileName)"""
    return bool

#noinspection PyUnusedLocal
def mkdir(path):
    """Create a folder.

    path: string - folder

    Example:
        success = xbmcfvs.mkdir(path)"""
    return bool

#noinspection PyUnusedLocal
def rmdir(path):
    """Remove a folder.

    path: string - folder

    Example:
        success = xbmcfvs.rmdir(path)"""
    return bool

#noinspection PyUnusedLocal
def exists(path):
    """Checks for a file or folder existance, mimics Pythons os.path.exists()

    path: string - file or folder

    Example:
        success = xbmcvfs.exists(path)"""
    return bool
