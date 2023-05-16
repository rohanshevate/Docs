# Function to reverse a string
# by converting string to list
# then reversed it and again convert it to string
def Areversed(string):
	string = list(string)
	string.reverse()
	return "".join(string)

s = "Geeksforgeeks"

print("The original string is : ", s)

print("The reversed string(using reversed) is : ", Areversed(s))

# This code is contributed by Susobhan AKhuli
