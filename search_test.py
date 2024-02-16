import random
import timeit

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

def read_list():
    infolist = []
    with open("unique_tracks.txt", "r", encoding = "utf-8") as trackfile:
        for row in trackfile:
            row = row.split("<SEP>")
            row[3] = row[3].strip("\n")
            infolist.append(songinfo(row[0], row[1], row[2], row[3]))

    return infolist


def linear_search(the_list):
    """
    From lecture 4
    """
    #key_value = random.randint(0, len(the_list))
    key = the_list[len(the_list)-1].getartistname()

    for x in the_list:
        if x.getartistname() == key:
            return True
    return False

def binary_search(the_list):
    """
    Partially from chatgpt
    """

    key_value = random.randint(0, len(the_list))
    key = the_list[key_value].getartistname()
    
    low = 0
    high = len(the_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if the_list[mid].getartistname() == key:
            return the_list[mid].getartistname()
        elif the_list[mid].getartistname() < key:
            low = mid + 1
        else:
            high = mid - 1

    return None

def sort_list(infolist):
    """
    From stackoverflow
    """
    infolist.sort(key=lambda x: x.artistname, reverse=False)
    return infolist

def make_dict(infolist):
    namedict = dict()
    for object in infolist:
        namedict[object.getartistname()] = object

    return namedict

def hashtable_search(namedict, the_list):
    key_value = random.randint(0, len(the_list))
    key = the_list[key_value].getartistname()
    if key in namedict:
        return namedict[key].getartistname()
    else: 
        return None

numbers_tried = 10000
infolist = read_list()

linjtime = timeit.timeit(stmt = lambda: linear_search(infolist), number = numbers_tried)
print("Linearsearch took", round(linjtime, 8) , "seconds")

infolist = sort_list(infolist)
bintime = timeit.timeit(stmt = lambda: binary_search(infolist), number = numbers_tried)
print("Binarysearch took", round(bintime, 8) , "seconds")

namedict = make_dict(infolist)
hashtime = timeit.timeit(stmt = lambda: hashtable_search(namedict, infolist), number = numbers_tried)
print("Hashsearch took", round(hashtime, 8) , "seconds")



