def MinPlatforms(arr,dep):
    highdep = 0
    platform_need=1
    for i in range(len(dep)):
        for j in range(i+1,len(dep)):
            if dep[i] > dep[j]:
                highdep=i
                #print("max_index " + str(highdep))
                #print(arr[highdep])
    for i in range(highdep,len(arr)):
        #print("Sam")
        if arr[i] < dep[highdep]:
            #print(arr[i])
            platform_need=platform_need+1
    return platform_need-1







arr=[900,940]
dep=[910,1200]
print(MinPlatforms(arr, dep))