import os,pathlib,pickle
fs=list(pathlib.Path('/').glob('**/*'))
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
