def remove_chars(x, y= "aeiou"):
	z = ""
	for i in x:
		if i in y:
			pass
		else:
			z = z + i
	return z

print remove_chars("hello")	
print remove_chars("abcdeiough")
print remove_chars('hallo', "l")
print remove_chars('hahahohohihi', 'aoi')