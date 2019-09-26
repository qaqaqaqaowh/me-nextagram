from flask import flash

def flash_messages(iterable, *args):
	for i in iterable:
		flash(i, *args)