def ten(X,Y):
		
	array_2D = []

	for j in range(Y):
		array_1D = []
		
		for i in range(X):
			array_1D.append(i*j)
			
		array_2D.append(array_1D)
	
	return array_2D