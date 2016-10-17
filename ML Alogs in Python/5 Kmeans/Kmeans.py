## Running instruction : python Kmeans.py <datasetname> <value of k>

import sys, math, random

class Point:

    def __init__(self, coords, reference=None):
        self.coords = coords
        self.n = len(coords)
        self.reference = reference

    def __repr__(self):
        return str(self.coords)

class Cluster:

    def __init__(self, points):

        if len(points) == 0: raise Exception("ILLEGAL: EMPTY CLUSTER")
        self.points = points
        self.n = points[0].n

        for p in points:
            if p.n != self.n: raise Exception("ILLEGAL: MULTISPACE CLUSTER")

        self.centroid = self.calculateCentroid()

    def __repr__(self):
        return str(self.points)

    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        return getDistance(old_centroid, self.centroid)

    def calculateCentroid(self):
        centroid_coords = []
        # For each coordinate:
        for i in range(self.n):

            centroid_coords.append(0.0)
            for p in self.points:
                centroid_coords[i] = centroid_coords[i]+p.coords[i]
            centroid_coords[i] = centroid_coords[i]/len(self.points)

        return Point(centroid_coords)

def kmeans(points, k, cutoff):

    initial = random.sample(points, k)
    clusters = []
    for p in initial: clusters.append(Cluster([p]))

    while True:

        lists = []
        for c in clusters: lists.append([])

        for p in points:
            smallest_distance = getDistance(p, clusters[0].centroid)
            index = 0
            for i in range(len(clusters[1:])):
                distance = getDistance(p, clusters[i+1].centroid)
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i+1
            lists[index].append(p)

        biggest_shift = 0.0
        for i in range(len(clusters)):
            shift = clusters[i].update(lists[i])
            biggest_shift = max(biggest_shift, shift)
        if biggest_shift < cutoff: break
    return clusters

def getDistance(a, b):

    if a.n != b.n: raise Exception("ILLEGAL: NON-COMPARABLE POINTS")
    ret = 0.0
    for i in range(a.n):
        ret = ret+pow((a.coords[i]-b.coords[i]), 2)
    return math.sqrt(ret)

def main(args):
    # Read File
    datafile = sys.argv[1]
    f = open(datafile)
    points = []
    i = 0
    l = f.readline()

    while (l != ''):
        a = l.split()
        coords = []
        for j in range(0, len(a), 1):
            coords.append(float(a[j]))
        points.append(Point(coords))
        l = f.readline()

    k = sys.argv[2]
    cutoff = 0.5

    clusters = kmeans(points, int(k), cutoff)
    print ("\nPOINTS:")
    for p in points: print ("P:", p)
    print ("\nCLUSTERS:")
    for c in clusters: print ("C:", c)
    
if __name__ == "__main__": main(sys.argv)