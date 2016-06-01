from os import listdir
from os.path import join

DIR="./Berliner_Parlamentsprotokolle/"

for fname in listdir(DIR):
	with open(join(DIR, fname)) as f:
		content = f.read()
	out = content.replace('KLEINER', '<').replace('GRÖSSER', '>')
	with open(join(DIR, fname), 'w') as f:
		f.write(out)
	print('done with', fname)
print('Finished')
