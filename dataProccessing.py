from mpl_toolkits.basemap import Basemap
bm = Basemap()

lan =[]
lon =[]
file1 = open("results.txt", "r+")
coor = file1.readline()

while (coor):
    lonTemp, lanTemp = [ float(x) for x in coor.split()]
   # print(lan)
    coor = file1.readline()
    lanEnd = lanTemp + 0.125
    lonEnd = lonTemp + 0.125
    countSea = 0
    step =0.01
    i = lonTemp - 0.125
    j = lanTemp  - 0.125
    total = 0
    while(i < lonEnd):
        while(j < lanEnd):
            total = total + 1
            if(bm.is_land(j,i) == False):
                countSea = countSea + 1
            j = j+ step
        i = i + step
        total = total +1
    print(countSea, " ", total)
    if(float(countSea)/total < 0.9):
        lon.append(lonTemp)
        lan.append(lanTemp)
    else:
        print(lonTemp," ", lanTemp)


