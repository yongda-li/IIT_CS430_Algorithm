def InsertionSort(Arr):
	for j in range(len(Arr)):
		key = Arr[j]
		i = j - 1
		while i >= 0 and Arr[i] > key:
			Arr[i+1] = Arr[i]
			i = i - 1
		Arr[i+1] = key
	return Arr