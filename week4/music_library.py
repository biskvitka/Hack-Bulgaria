class Song:
    def __init__(self, title, artist, album, lenght):
        self.title = title
        self.artist = artist
        self.album = album
        self.lenght = lenght

    def  get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def get_lenght(self):
        return self.lenght

    def __str__(self):
        return "{}-{} from {}-{}".format(self.get_artist(),self.get_title(),self.get_album(),self.get_lenght())

    def __eq__(self, other):
        return (self.get_artist() == other.get_artist() and self.get_title() ==other.get_title())

    def __hash__(self):
        return hash(self.__str__())

    def lenght(self):
        seconds= 0
        if len(self.get_lenght())<5:
            for part in (self.get_lenght()).split(':'):
                seconds= seconds*60 + int(part)
                return seconds

        l = (self.get_lenght()).split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])





def getSec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

print(getSec('1:23:45'))
print(getSec('0:04:15'))
print(getSec('0:00:25'))



