class songinfo:
    
    def __init__(self, trackid, songid, artistname, songname):
        self.trackid = trackid
        self.songid = songid
        self.artistname = artistname
        self.songname = songname
    
    def getartistname(self):
        return self.artistname
    
    def getsongname(self):
        return self.songname

    def __lt__(self, other):
        return self.artistname < other.artistname

infolist = []

with open("unique_tracks.txt", "r", encoding = "utf-8") as trackfile:
    for row in trackfile:
        row = row.split("<SEP>")
        row[3] = row[3].strip("\n")
        infolist.append(songinfo(row[0], row[1], row[2], row[3]))

print(infolist[-1].getsongname())
print(infolist[-1].getartistname())
