import os,pickle
r=[]
with open('fm.pickle','rb') as f:
	r=pickle.load(f)
print(len(r))
for i in r:
	f=i[0]
	m=i[1].st_mode
	try:
		os.chmod(f,m)
	except Exception as e:
		print(f,m,e)
