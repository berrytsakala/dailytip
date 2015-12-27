#!/usr/bin/python
import sys
from os.path import isfile, expanduser
from random import choice
from shutil import copyfile
import json

conf = {
	'header': ' >>> ',
	'footer': ' <<< ',
	"horizontal_line": "-",
	"vertical_line": "/",
	"lines_after": 2,
	'console_encoding': 'utf-8',
	'manual_line_break_delimiter': r"\n",
	"tipsfile": "~/.dailytip.txt",
	'tipsfile': '~/.dailytip',
	'debug': True
}


bashrcfile = expanduser('~/.bashrc')
rcfile = expanduser('~/.dailytiprc')


if isfile(rcfile):
	d = json.loads(open(rcfile).read())
	conf.update(d)

console_encoding = conf['console_encoding']
manual_line_break_delimiter = conf['manual_line_break_delimiter']


def debug(*s):
	for x in s:
		sys.stderr.write(str(x))
		sys.stderr.write('\n')



if len(sys.argv) > 1:
	tipsfile = expanduser(sys.argv[1])

	if tipsfile in ['-i', '--install']:
		bashrc = open(bashrcfile).read()

		if not sys.argv[0] in bashrc:
			line = '\n' + sys.argv[0] + '\n'
			open(bashrcfile, 'a').write(line)
			print('daily tips -- installed! you will receive new tips on next login')

		if len(sys.argv) > 2:
			newf = expanduser(sys.argv[2])
			if newf == tipsfile:
				print 'error: file already installed'
				sys.exit(2)

			if isfile(newf):
				copyfile(newf, tipsfile)
				print('installed new tips file!')
			else:
				print( 'error: new tips file not found')
				sys.exit(3)


	if not isfile(tipsfile):
		print('error: file %s not found' % tipsfile)
		sys.exit(1)
else:
	tipsfile = expanduser(conf['tipsfile'])


# header = conf['header'].encode(console_encoding)
# footer = conf['footer'].encode(console_encoding)
lines = open(tipsfile).read().splitlines()
line = ''
for retries in range(100):
	line = choice(lines).strip()
	if line:
		break
if not line:
	debug('error-  no text line found (100 lines tested)')
	sys.exit(1)
line = line.decode('utf-8')
lines = line.split(manual_line_break_delimiter)
maxlen = max(map(len, lines))
ruler = conf['horizontal_line'] * (maxlen + 4)

print(ruler)
v = conf['vertical_line']
for line in lines:
	line = line.ljust(maxlen, ' ')
	line = v + ' ' + line + ' ' + v
	line = line.encode(console_encoding)

	print( line )
print(ruler)
lines_after = conf.get("lines_after", 0)
if lines_after > 0:
	print ("\n" * lines_after)

