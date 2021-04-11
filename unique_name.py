
def unique_name(names1,names2):
	l1 = names1+names2
	s = sorted(list(set(l1)))
	return ' '.join(s)


if __name__ == '__main__':
	names1 = ["Avva","Emma","Olivia"]
	names2 = ["Olivia","Sophia","Emma"]
	print(unique_name(names1,names2))

