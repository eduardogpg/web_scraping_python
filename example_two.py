import urllib
import re

def get_page(final_name = 'test.html'):
	open_file = open(final_name, 'w')
	html_file = urllib.urlopen("http://econpy.pythonanywhere.com/ex/005.html")
	html_file = html_file.read()

	open_file.write( str(html_file) )
	open_file.close()

def get_title(final_name = 'test.html'):
	open_file = open(final_name, 'r')
	regex = '<div title="buyer-name">'
	size_regex = len(regex) # No hasta la segunda 
	
	final_regex = '</div>'
	size_final_regex = len(final_regex)

	for line in open_file.readlines():
		sentence = line.strip('\n')
		if regex in sentence:
		
			initial_pos = sentence.find(regex) 
			initial_pos = initial_pos + size_regex

			final_pos = len(sentence)
			final_pos = final_pos - size_final_regex
			
			print sentence[initial_pos :final_pos]

def get_title_regex():
	html_file = urllib.urlopen("http://econpy.pythonanywhere.com/ex/005.html")
	html_file = html_file.read()

	regex = '<div title="buyer-name">(.+?)</div>'
	titles = re.findall(regex, html_file)
	for title in titles:
		print title

		

if __name__ == '__main__':
	get_title_regex()