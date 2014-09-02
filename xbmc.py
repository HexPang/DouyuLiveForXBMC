#noinspection PyUnusedLocal
class Keyboard(object):
    def __init__(self, default=None, heading=None, hidden=False):
        """Creates a new Keyboard object with default text heading and hidden input flag if supplied.

        default: string - default text entry.
        heading: string - keyboard heading.
        hidden: boolean - True for hidden text entry.

        Example:
            kb = xbmc.Keyboard('default', 'heading', True)
            kb.setDefault('password') # optional
            kb.setHeading('Enter password') # optional
            kb.setHiddenInput(True) # optional
            kb.doModal()
            if (kb.isConfirmed()):
                text = kb.getText()
        """
        pass

    def doModal(self, autoclose=0):
        """Show keyboard and wait for user action.

        autoclose: integer - milliseconds to autoclose dialog.

        Note:
            autoclose = 0 - This disables autoclose

        Example:
            kb.doModal(30000)
        """
        pass

    def setDefault(self, default):
        """Set the default text entry.

        default: string - default text entry.

        Example:
            kb.setDefault('password')
        """
        pass

    def setHiddenInput(self, hidden):
        """Allows hidden text entry.

        hidden: boolean - True for hidden text entry.

        Example:
            kb.setHiddenInput(True)
        """
        pass

    def setHeading(self, heading):
        """Set the keyboard heading.

        heading: string - keyboard heading.

        Example:
            kb.setHeading('Enter password')
        """
        pass

    def getText(self):
        """Returns the user input as a string.

        Note:
            This will always return the text entry even if you cancel the keyboard.
            Use the isConfirmed() method to check if user cancelled the keyboard.
        """
        return str

    def isConfirmed(self):
        """Returns False if the user cancelled the input."""
        return bool


#noinspection PyUnusedLocal
class Player(object):
    def __init__(self, core=None):
        """Creates a new Player with as default the xbmc music playlist.

        Args:
            core: Use a specified playcore instead of letting xbmc decide the playercore to use.
                - xbmc.PLAYER_CORE_AUTO
                - xbmc.PLAYER_CORE_DVDPLAYER
                - xbmc.PLAYER_CORE_MPLAYER
                - xbmc.PLAYER_CORE_PAPLAYER
        """
        pass

    def play(self, item=None, listitem=None, windowed=False):
        """Play this item.

        item: string - filename, url or playlist.
        listitem: listitem - used with setInfo() to set different infolabels.
        windowed: bool - True=play video windowed, False=play users preference.

        Note:
            If item is not given then the player will try to play the current item in the current playlist.

        Example:
            listitem = xbmcgui.ListItem('Ironman')
            listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
            xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(url, listitem, windowed)
        """
        pass

    def stop(self):
        """Stop playing."""
        pass

    def pause(self):
        """Pause playing."""
        pass

    def playnext(self):
        """Play next item in playlist."""
        pass

    def playprevious(self):
        """Play previous item in playlist."""
        pass

    def playselected(self):
        """Play a certain item from the current playlist."""
        pass

    def onPlayBackStarted(self):
        """Will be called when xbmc starts playing a file."""
        pass

    def onPlayBackEnded(self):
        """Will be called when xbmc stops playing a file."""
        pass

    def onPlayBackStopped(self):
        """Will be called when user stops xbmc playing a file."""

    def onPlayBackPaused(self):
        """Will be called when user pauses a playing file."""
        pass

    def onPlayBackResumed(self):
        """Will be called when user resumes a paused file."""
        pass

    def isPlaying(self):
        """Returns True is xbmc is playing a file."""
        return bool

    def isPlayingAudio(self):
        """Returns True is xbmc is playing an audio file."""
        return bool

    def isPlayingVideo(self):
        """Returns True if xbmc is playing a video."""
        return bool

    def getPlayingFile(self):
        """Returns the current playing file as a string.

        Raises:
            Exception: If player is not playing a file.
        """
        return str

    def getVideoInfoTag(self):
        """Returns the VideoInfoTag of the current playing Movie.

        Raises:
            Exception: If player is not playing a file or current file is not a movie file.

        Note:
            This doesn't work yet, it's not tested.
        """
        return object

    def getMusicInfoTag(self):
        """Returns the MusicInfoTag of the current playing 'Song'.

        Raises:
            Exception: If player is not playing a file or current file is not a music file.
        """
        return object

    def getTotalTime(self):
        """Returns the total time of the current playing media in seconds.

        This is only accurate to the full second.

        Raises:
            Exception: If player is not playing a file.
        """
        return float

    def getTime(self):
        """Returns the current time of the current playing media as fractional seconds.

        Raises:
            Exception: If player is not playing a file.
        """
        return float

    def seekTime(self, pTime):
        """Seeks the specified amount of time as fractional seconds.

        The time specified is relative to the beginning of the currently playing media file.

        Raises:
            Exception: If player is not playing a file.
        """
        pass

    def setSubtitles(self):
        """Set subtitle file and enable subtitles.

        path: string or unicode - Path to subtitle.

        Example:
            setSubtitles('/path/to/subtitle/test.srt')
        """
        pass

    def getSubtitles(self):
        """Get subtitle stream name."""
        return str

    def disableSubtitles(self):
        """Disable subtitles."""
        pass

    def getAvailableAudioStreams(self):
        """Get audio stream names."""
        return list

    def setAudioStream(self, stream):
        """Set audio stream.

        stream: int
        """
        pass


#noinspection PyUnusedLocal
class PlayList(object):
    def __init__(self, playlist):
        """Retrieve a reference from a valid xbmc playlist

        playlist: int - can be one of the next values:
            0: xbmc.PLAYLIST_MUSIC
            1: xbmc.PLAYLIST_VIDEO

        Use PlayList[int position] or __getitem__(int position) to get a PlayListItem.
        """
        pass

    def add(self, url, listitem=None, index=-1):
        """Adds a new file to the playlist.

        url: string or unicode - filename or url to add.
        listitem: listitem - used with setInfo() to set different infolabels.
        index: integer - position to add playlist item.

        Example:
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            video = 'F:\\movies\\Ironman.mov'
            listitem = xbmcgui.ListItem('Ironman', thumbnailImage='F:\\movies\\Ironman.tbn')
            listitem.setInfo('video', {'Title': 'Ironman', 'Genre': 'Science Fiction'})
            playlist.add(url=video, listitem=listitem, index=7)
        """
        pass

    def load(self, filename):
        """Load a playlist.

        Clear current playlist and copy items from the file to this Playlist filename can be like .pls or .m3u ...

        Returns False if unable to load playlist, True otherwise.
        """
        return bool

    def remove(self, filename):
        """Remove an item with this filename from the playlist."""
        pass

    def clear(self):
        """Clear all items in the playlist."""
        pass

    def shuffle(self):
        """Shuffle the playlist."""
        pass

    def unshuffle(self):
        """Unshuffle the playlist."""
        pass

    def size(self):
        """Returns the total number of PlayListItems in this playlist."""
        return int

    def getposition(self):
        """Returns the position of the current song in this playlist."""
        return int


#noinspection PyUnusedLocal
class PlayListItem(object):
    """Creates a new PlaylistItem which can be added to a PlayList."""

    def getdescription(self):
        """Returns the description of this PlayListItem."""
        return str

    def getduration(self):
        """Returns the duration of this PlayListItem."""
        return long

    def getfilename(self):
        """Returns the filename of this PlayListItem."""
        return str


#noinspection PyUnusedLocal
class InfoTagMusic(object):
    def getURL(self):
        """Returns a string."""
        return str

    def getTitle(self):
        """Returns a string."""
        return str

    def getArtist(self):
        """Returns a string."""
        return str

    def getAlbumArtist(self):
        """Returns a string."""
        return str

    def getAlbum(self):
        """Returns a string."""
        return str

    def getGenre(self):
        """Returns a string."""
        return str

    def getDuration(self):
        """Returns an integer."""
        return int

    def getTrack(self):
        """Returns an integer."""
        return int

    def getDisc(self):
        """Returns an integer."""
        return int

    def getTrackAndDisc(self):
        """Returns an integer."""
        return int

    def getReleaseDate(self):
        """Returns a string."""
        return str

    def getListeners(self):
        """Returns an integer."""
        return int

    def getPlayCount(self):
        """Returns an integer."""
        return int

    def getLastPlayed(self):
        """Returns a string."""
        return str

    def getComment(self):
        """Returns a string."""
        return str

    def getLyrics(self):
        """Returns a string."""
        return str


#noinspection PyUnusedLocal
class InfoTagVideo(object):
    def getDirector(self):
        """Returns a string."""
        return str

    def getWritingCredits(self):
        """Returns a string."""
        return str

    def getGenre(self):
        """Returns a string."""
        return str

    def getTagLine(self):
        """Returns a string."""
        return str

    def getPlotOutline(self):
        """Returns a string."""
        return str

    def getPlot(self):
        """Returns a string."""
        return str

    def getPictureURL(self):
        """Returns a string."""
        return str

    def getTitle(self):
        """Returns a string."""
        return str

    def getOriginalTitle(self):
        """Returns a string."""
        return str

    def getVotes(self):
        """Returns a string."""
        return str

    def getCast(self):
        """Returns a string."""
        return str

    def getFile(self):
        """Returns a string."""
        return str

    def getPath(self):
        """Returns a string."""
        return str

    def getIMDBNumber(self):
        """Returns a string."""
        return str

    def getYear(self):
        """Returns an integer."""
        return int

    def getPremiered(self):
        """Returns a string."""
        return str

    def getFirstAired(self):
        """Returns a string."""
        return str

    def getRating(self):
        """Returns a float."""
        return float

    def getPlayCount(self):
        """Returns an integer."""
        return int

    def getLastPlayed(self):
        """Returns a string."""
        return str


PLAYLIST_MUSIC = 0
PLAYLIST_VIDEO = 1

PLAYER_CORE_AUTO = 0
PLAYER_CORE_DVDPLAYER = 1
PLAYER_CORE_MPLAYER = 2
PLAYER_CORE_PAPLAYER = 3

TRAY_OPEN = 16
DRIVE_NOT_READY = 1
TRAY_CLOSED_NO_MEDIA = 64
TRAY_CLOSED_MEDIA_PRESENT = 96

LOGDEBUG = 0
LOGINFO = 1
LOGNOTICE = 2
LOGWARNING = 3
LOGERROR = 4
LOGSEVERE = 5
LOGFATAL = 6
LOGNONE = 7

CAPTURE_STATE_WORKING = 0
CAPTURE_STATE_DONE = 3
CAPTURE_STATE_FAILED = 4

CAPTURE_FLAG_CONTINUOUS = 1
CAPTURE_FLAG_IMMEDIATELY = 2


#noinspection PyUnusedLocal
def output(msg, level=LOGNOTICE):
    """Write a string to XBMC's log file and the debug window.

    msg: string - text to output.
    level: integer - log level to ouput at.

    Note:
        Text is written to the log for the following conditions:
            XBMC loglevel == -1 (NONE, nothing at all is logged)
            XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)
            XBMC loglevel == 1 (DEBUG, shows all)
        See pydocs for valid values for level.

    Example:
        xbmc.output(msg='This is a test string.', level=xbmc.LOGDEBUG)
    """
    pass

#noinspection PyUnusedLocal
def log(msg, level=LOGNOTICE):
    """Write a string to XBMC's log file.

    msg: string - text to output.
    level: integer - log level to ouput at.

    Note:
        Text is written to the log for the following conditions.
            XBMC loglevel == -1 (NONE, nothing at all is logged)
            XBMC loglevel == 0 (NORMAL, shows LOGNOTICE, LOGERROR, LOGSEVERE and LOGFATAL)
            XBMC loglevel == 1 (DEBUG, shows all)
        See pydocs for valid values for level.

    Example:
        xbmc.log(msg='This is a test string.', level=xbmc.LOGDEBUG)
    """
    pass

def shutdown():
    """Shutdown the xbox."""
    pass

def dashboard():
    """Boot to dashboard as set in My Pograms/General."""
    pass

def restart():
    """Reboot the xbox."""
    pass

#noinspection PyUnusedLocal
def executescript(script):
    """Execute a python script.

    script: string - script filename to execute.

    Example:
        xbmc.executescript('special://home/scripts/update.py')
    """
    pass

#noinspection PyUnusedLocal
def executebuiltin(function):
    """Execute a built in XBMC function.

    function: string - builtin function to execute.

    List of functions: http://wiki.xbmc.org/?title=List_of_Built_In_Functions

    Example:
        xbmc.executebuiltin('XBMC.RunXBE(c:\\\\avalaunch.xbe)')
    """
    pass

#noinspection PyUnusedLocal
def executehttpapi(httpcommand):
    """Execute an HTTP API command.

    httpcommand: string - http command to execute.

    List of commands: http://wiki.xbmc.org/?title=WebServerHTTP-API#The_Commands

    Example:
        response = xbmc.executehttpapi('TakeScreenShot(special://temp/test.jpg,0,false,200,-1,90)')
    """
    return str

#noinspection PyUnusedLocal
def executeJSONRPC(jsonrpccommand):
    """Execute an JSONRPC command.

    jsonrpccommand: string - jsonrpc command to execute.

    List of commands: http://wiki.xbmc.org/index.php?title=JSON_RPC#XBMC_API

    Example:
        response = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "JSONRPC.Introspect", "id": 1 }')
    """
    return str

#noinspection PyUnusedLocal
def sleep(time):
    """Sleeps for 'time' msec.

    time: integer - number of msec to sleep.

    Note:
        This is useful if you have for example a Player class that is waiting for onPlayBackEnded() calls.

    Raises:
        TypeError: If time is not an integer.

    Example:
        xbmc.sleep(2000) # sleeps for 2 seconds
    """
    pass

#noinspection PyUnusedLocal
def getLocalizedString(id):
    """Returns a localized 'unicode string'.

    id: integer - id# for string you want to localize.

    Note:
        See strings.xml in \language\{yourlanguage}\ for which id you need for a string.

    Example:
        locstr = xbmc.getLocalizedString(6)
    """
    return unicode

def getSkinDir():
    """Returns the active skin directory as a string.

    Note:
        This is not the full path like 'special://home/addons/MediaCenter', but only 'MediaCenter'.
    """
    return str

def getLanguage():
    """Returns the active language as a string."""
    return str

def getIPAddress():
    """Returns the current ip address as a string."""
    return str

def getDVDState():
    """Returns the dvd state as an integer.

    Return values are:
         1: xbmc.DRIVE_NOT_READY
        16: xbmc.TRAY_OPEN
        64: xbmc.TRAY_CLOSED_NO_MEDIA
        96: xbmc.TRAY_CLOSED_MEDIA_PRESENT
    """
    return int

def getFreeMem():
    """Returns the amount of free memory in MB as an integer."""
    return int

#noinspection PyUnusedLocal
def getInfoLabel(infotag):
    """Returns an InfoLabel as a string.

    infotag: string - infoTag for value you want returned.

    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels

    Example:
        label = xbmc.getInfoLabel('Weather.Conditions')
    """
    return str

#noinspection PyUnusedLocal
def getInfoImage(infotag):
    """Returns a filename including path to the InfoImage's thumbnail as a string.

    infotag: string - infotag for value you want returned.

    List of InfoTags - http://wiki.xbmc.org/?title=InfoLabels

    Example:
        filename = xbmc.getInfoImage('Weather.Conditions')
    """
    return str

#noinspection PyUnusedLocal
def playSFX(filename):
    """Plays a wav file by filename.

    filename: string - filename of the wav file to play.

    Example:
        xbmc.playSFX('special://xbmc/scripts/dingdong.wav')
    """
    pass

#noinspection PyUnusedLocal
def enableNavSounds(yesNo):
    """Enables/Disables nav sounds.

    yesNo: integer - enable (True) or disable (False) nav sounds

    Example:
        xbmc.enableNavSounds(True)
    """
    pass

#noinspection PyUnusedLocal
def getCondVisibility(condition):
    """Returns True (1) or False (0) as a bool.

    condition: string - condition to check.

    List of Conditions - http://wiki.xbmc.org/?title=List_of_Boolean_Conditions

    Note:
        You can combine two (or more) of the above settings by using "+" as an AND operator,
        "|" as an OR operator, "!" as a NOT operator, and "[" and "]" to bracket expressions.

    Example:
        visible = xbmc.getCondVisibility('[Control.IsVisible(41) + !Control.IsVisible(12)]')
    """
    return bool

def getGlobalIdleTime():
    """Returns the elapsed idle time in seconds as an integer."""
    return int

#noinspection PyUnusedLocal
def getCacheThumbName(path):
    """Returns a thumb cache filename.

    path: string or unicode - path to file

    Example:
        thumb = xbmc.getCacheThumbName('f:\\videos\\movie.avi')
    """
    return str

#noinspection PyUnusedLocal
def makeLegalFilename(filename, fatX=True):
    """Returns a legal filename or path as a string.

    filename: string or unicode - filename/path to make legal
    fatX: bool - True=Xbox file system

    Note:
        If fatX is true you should pass a full path. If fatX is false only pass the basename of the path.

    Example:
        filename = xbmc.makeLegalFilename('F:\\Trailers\\Ice Age: The Meltdown.avi')
    """
    return str

#noinspection PyUnusedLocal
def translatePath(path):
    """Returns the translated path.

    path: string or unicode - Path to format

    Note:
        Only useful if you are coding for both Linux and Windows/Xbox.
        e.g. Converts 'special://masterprofile/script_data' -> '/home/user/XBMC/UserData/script_data'
        on Linux. Would return 'special://masterprofile/script_data' on the Xbox.

    Example:
        fpath = xbmc.translatePath('special://masterprofile/script_data')
    """
    return str

#noinspection PyUnusedLocal
def getCleanMovieTitle(path, usefoldername=False):
    """Returns a clean movie title and year string if available.

    path: string or unicode - String to clean
    "usefoldername: bool - use folder names

    Example:
        title, year = xbmc.getCleanMovieTitle('/path/to/moviefolder/test.avi', True)
    """
    return str

#noinspection PyUnusedLocal
def validatePath(path):
    """Returns the validated path.

    path: string or unicode - Path to format

    Note:
        Only useful if you are coding for both Linux and Windows/Xbox for fixing slash problems.
        e.g. Corrects 'Z://something' -> 'Z:\\something'

    Example:
        fpath = xbmc.validatePath(somepath)
    """
    return str

#noinspection PyUnusedLocal
def getRegion(id):
    """Returns your regions setting as a string for the specified id.

    id: string - id of setting to return

    Note:
        Choices are (dateshort, datelong, time, meridiem, tempunit, speedunit)

    Example:
        date_long_format = xbmc.getRegion('datelong')
    """
    return str

#noinspection PyUnusedLocal
def getSupportedMedia(media):
    """Returns the supported file types for the specific media as a string.

    media: string - media type

    Note:
        Media type can be (video, music, picture).

        The return value is a pipe separated string of filetypes (eg. '.mov|.avi').

    Example:
        mTypes = xbmc.getSupportedMedia('video')
    """
    return str

#noinspection PyUnusedLocal
def skinHasImage(image):
    """Returns True if the image file exists in the skin.

    image: string - image filename

    Note:
        If the media resides in a subfolder include it. (eg. home-myfiles\\home-myfiles2.png)

    Example:
        exists = xbmc.skinHasImage('ButtonFocusedTexture.png')
    """
    return bool

#noinspection PyUnusedLocal
def subHashAndFileSize(file):
    """Returns tuple with subtitle hash and size.

    file: string - file to calculate hash and size for

    Example:
        size,hash = xbmc.subHashAndFileSize(file)
    """
    return tuple
