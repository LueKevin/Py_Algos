#Sorting Algos

class sAlgo():
    def insSrt(list):
        for i in range(0,list.length()):
            j = i
            while j and list[j-1] > list[j]:
                list[j], list[j-1] = list[j-1], list[j]
                
