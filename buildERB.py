import re
import os

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

print ('Beginning ERB build')

baseDir = os.getcwd ()

sourceDir = os.path.join (baseDir, 'source', 'includes')

re_include = re.compile (r".*includes/(.*)")
re_mdName = re.compile (r"_(.*)\.md")

indexList = []

for root, dirs, files in os.walk (sourceDir):
	if (len (files) > 0):
		fileList = sorted_alphanumeric (files)

		shallowRootMatch = re_include.match (root)
		if (shallowRootMatch):
			shallowRoot = shallowRootMatch.group (1)
			erb = []

			for file in fileList:
				if (file == '_index.md.erb'):
					continue

				noMdMatch = re_mdName.match (file)
				if (noMdMatch):
					noMd = noMdMatch.group (1)
					partialLoc = os.path.join ('includes', shallowRoot, noMd)
					line = '<%= partial "' + partialLoc + '" %>\r\n'
					erb.append (line)

			if (len (erb) > 0):

				print ('Writing ERB partials for ' + shallowRoot)

				erbName = os.path.join (baseDir, 'source', 'includes', shallowRoot, '_index.md.erb')
				f = open (erbName, 'w')
				f.writelines (erb)
				f.close ()
				includeName = os.path.join (shallowRoot, 'index')
				indexList.append (includeName)

indexList = sorted_alphanumeric (indexList)

indexErb = '''---
title: Driverworks Reference

language_tabs:
  - lua

toc_footers:
  - <a href='https://github.com/lord/slate'>Documentation Powered by Slate</a>

search: true

includes:
'''

print ('Writing main index.html.md.erb')

if (len (indexList) > 0):
	for index in indexList:
		erbLine = '  - ' + index + '\r\n'
		indexErb = indexErb + erbLine

indexErb = indexErb + '\r\n---\r\n'

indexErbName = os.path.join (baseDir, 'source', 'index.html.md.erb')
f = open (indexErbName, 'w')
f.writelines (indexErb)
f.close ()

print ('ERB build complete')
