#!/bin/usr/python
class Person:               #Person Class
	def __init__(self):
		self.score = 0
		self.level = 1
		self.life = 3

	def scoreboard(self):
		return self.score

	def levelreached(self):
		return self.level

	def livesleft(self):
		return self.life
