import sys,os,pathlib,pickle
gsp='/'
if len(sys.argv)==2:
	gsp=sys.argv[1]
fs=list(pathlib.Path(gsp).glob('**/*'))
r=[]
for i in fs:
	i=str(i.absolute())
	try:
		r.append([i,os.stat(i)])
	except Exception as e:
		print(i,e)
print('scaned {} files'.format(len(r) )  )
with open('fm.pickle','wb') as f:
	pickle.dump(obj=r,file=f)
