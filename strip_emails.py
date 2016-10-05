#!/usr/bin/python


def strip_emails():
	text = open('original_text.txt')
	new_text=open('Stanford_CS_Masters.txt', 'w')
	for line in text:
		item = line.split(",")
		name = item[0]
		new_text.write(name + '\n')

if __name__ == '__main__':
	strip_emails()
