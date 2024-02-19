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
    
class HeapNode:
    """
    From lecture 8
    """
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return "{0}:{1}".format(self.data, self.priority)

class Heap:
    """
    From lecture 8 but edited to be minheap
    """
    def __init__(self):
        self.maxsize = 32
        self.tab = (self.maxsize + 1) * [None]
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):     
        return self.size == self.maxsize

    def insert(self, data, priority):
        if not self.isFull():
            self.size += 1
            self.tab[self.size] = HeapNode(data, priority)
            i = self.size
            while i > 1 and self.tab[i // 2].priority > self.tab[i].priority:
                self.tab[i // 2], self.tab[i] = self.tab[i], self.tab[i // 2]
                i = i // 2

    def delMin(self):
        if not self.isEmpty():
            data = self.tab[1]
            self.tab[1] = self.tab[self.size]
            self.size -= 1
            i = 1
            while (2 * i) <= self.size:
                mini = self.minindex(i)
                if self.tab[i].priority > self.tab[mini].priority:
                    self.tab[i], self.tab[mini] = self.tab[mini], self.tab[i]
                i = mini
            return data.data
        else:
            return None

    def minindex(self, i):
        if (2 * i) + 1 > self.size:
            return 2 * i
        if self.tab[2 * i].priority < self.tab[(2 * i) + 1].priority:
            return 2 * i
        else:
            return (2 * i) + 1

def read_list():
    infolist = []
    with open("unique_tracks.txt", "r", encoding = "utf-8") as trackfile:
        for row in trackfile:
            row = row.split("<SEP>")
            row[3] = row[3].strip("\n")
            infolist.append(songinfo(row[0], row[1], row[2], row[3]))

    return infolist

def sort_songs_selection_sort(data):
    """
    From lecture 9
    """
    n = len(data)
    for i in range(n-1):
        minst = i
        for j in range(i+1,n):
            if data[j].getsongname() < data[minst].getsongname():
                minst = j
        data[minst],data[i] = data[i], data[minst]

infolist = read_list()
infolist = infolist[0:10]

#print("Before sorting:")
#for song in infolist:
    #print(song.getsongname())

sort_songs_selection_sort(infolist)

#print("\nAfter sorting:")
#for song in infolist:
   # print(song.getsongname())


infolist = read_list()
infolist = infolist[0:100000]
sortedlist = []

def heapsort(infolist):
    heap = Heap()               
    for info in infolist:
        heap.insert(info, info.getsongname())
    while not heap.isEmpty():
        sortedlist.append(heap.delMin())
    return sortedlist

#sortedlist = heapsort(infolist)
#for object in sortedlist:
    #print(object.getsongname())

selection_sort_time = timeit.timeit(stmt = lambda: sort_songs_selection_sort(infolist), number = 1)
print("Selectionsort took", round(selection_sort_time, 8) , "seconds")

heapsort_time = timeit.timeit(stmt = lambda: heapsort(infolist), number = 1)
print("Heapsort took", round(heapsort_time, 8) , "seconds")


"""
For n = 1000
Selectionsort took 0.07856275 seconds
Heapsort took 0.00027679 seconds

For n = 10000
Selectionsort took 8.0347415 seconds
Heapsort took 0.00322208 seconds

For n = 100000
Selectionsort took 975.50067467 seconds
Heapsort took 0.03396679 seconds
"""