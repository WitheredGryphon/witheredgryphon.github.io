#!/usr/bin/python

import urllib.request

req = urllib.request.Request("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
resp = urllib.request.urlopen(req)
html = resp.read()
text = html.decode()
word_list = text.split()

for i in range(0, 450):
	if i == 0:
		linked_word_list = word_list
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + linked_word_list[-1]
	print(url)
	linked_req = urllib.request.Request(url)
	linked_resp = urllib.request.urlopen(linked_req)
	linked_html = linked_resp.read()
	linked_text = linked_html.decode()
	prev_number = int(linked_word_list[-1])
	linked_word_list = linked_text.split()
	if (linked_word_list[0] == "Yes."):
		prev_number /= 2
		linked_word_list = str(prev_number)