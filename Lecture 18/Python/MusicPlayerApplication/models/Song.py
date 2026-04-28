class Song:
    def __init__(self, title: str, artist: str, filePath: str):
        self.__title = title
        self.__artist = artist
        self.__filePath = filePath
    
    def get_title(self):
        return self.__title
    
    def get_artist(self):
        return self.__artist
    
    def get_file_path(self):
        return self.__filePath
    
    

