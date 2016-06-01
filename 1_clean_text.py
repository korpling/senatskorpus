from os import listdir
from os.path import exists
import re

DIR = './text/'
REPL_DIR = './replace_lists/'
CLEAN_DIR = './clean/'

for fname in listdir(DIR):
	replaces = []
	with open(DIR+fname) as f:
		content = f.read()
	if exists(REPL_DIR+fname):
		with open(REPL_DIR+fname) as f_r:
			replaces = f_r.readlines()
	out = ''.join(filter(lambda c: c.isprintable() or c.isspace(), content))
	for repl in replaces:
		out = out.replace(repl, repl.replace('-', ' ' if repl.endswith('-und') else ''))
	out = re.sub('\s+', ' ', out)
	out = out.replace('<', 'KLEINER')
	out = out.replace('>', 'GRÖSSER')
	with open(CLEAN_DIR+fname, 'w') as f:
		f.write(out.strip())
	print('Done with',fname)

print('Done')
