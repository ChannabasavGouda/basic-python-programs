def is_palindrome(string):
	return string == string[::-1]

string = "malayalam"
if is_palindrome(string):
	print("Yes")
else:
	print("No")
