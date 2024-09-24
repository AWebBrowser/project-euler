## TO-DO
# Create hashmap such that it maps every two consecutive numbers into a coordinate pair.
# RZN: It allows for searching one around the values easier.

from math import prod


def longestProd(hugeNum: str,dim: int, rad: int) -> int:
    arr=[int(hugeNum[i:i+2]) for i in range(len(hugeNum)//2)]
    res:int=0
    i=0
    while i < len(arr):
        try:
            test0=prod( arr[i-n*dim]  for n in range(rad))
            test1=prod( arr[i-n*dim+n]for n in range(rad))
            test2=prod( arr[i+n]      for n in range(rad))
            test3=prod( arr[i+n*dim+n]for n in range(rad))
            test4=prod( arr[i+n*dim]  for n in range(rad))
            test5=prod( arr[i-n*dim+n]for n in range(rad))
            test6=prod( arr[i-n]      for n in range(rad))
            test7=prod( arr[i-n*dim-n]for n in range(rad))
            test=max(test0,test1,test2,test3,test4,test5,test6,test7)
            #print(test)
            if test > res:
                res=test
        except IndexError:
            print("skip")
    print(i)
    i+=1
    return res

print(longestProd("08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748",20,4))
