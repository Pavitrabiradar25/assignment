def make_it_flatten(x):
	y={}
	for key,value in x.items():
		for key1,value1 in value.items():
			y[key+'_'+key1]=value1
		return y

if __name__ == '__main__':
	x={'a':{'b':'c','d':'e'}}
	print(make_it_flatten(x))