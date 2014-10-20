def Count_unique_words(arr):
	if arr == []:
		return 0

	count = 1
	for i in range(0,int(len(arr)-1)):
		if arr[i+1] not in arr[0:i+1]:
			count += 1
	return count

print (Count_unique_words(["apple", "banana", "apple", "pie"]))