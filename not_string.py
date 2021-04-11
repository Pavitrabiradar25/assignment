def notstring(str):
	if len(str)>=3 and str[:3] =='not':
		return str
	else:
		return 'not'+str

if __name__ == '__main__':
	print(notstring('candy'))
	print(notstring('x'))
	print(notstring('notbad'))

