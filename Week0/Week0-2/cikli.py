def cikli():
    for k in range(0, 3):
        for i in range(0, 3):
            for j in range(0 + 3 * k, 3 + 3 * k):
                print (i, " ", j)


def cikli2():
    for d in range(0, 3):
        for k in range(0, 3):
	        for i in range(0 + 3 * d, 3 + 3 * d):
	            for j in range(0 + 3 * k, 3 + 3 * k):
	                print (i, " ", j)

print ("------------------------------")
cikli2()
