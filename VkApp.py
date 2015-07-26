#!/usr/local/bin/python3
# coding: UTF-8

from words import *
import vk
import sys
import urllib
from urllib.request import urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random
import time
from datetime import timedelta
from datetime import datetime
from threading import Timer,Thread,Event
import webbrowser
import wget
import os
import cgi
import cgitb
import wsgiref.handlers
import json
import wikipedia
from itertools import islice

# cgitb.enable()

# print('Content-type: text/html')
# print()

# User and app info
vkapi = vk.API( access_token = '12190cdc5c7c2de92e1f892153e6ec3af558d98afc124f1a2534fae400ec277f8807264ff980f4c403de4')
other = [-72580409, -61330688]
person = [179349317]
app_id = 4967352

supercitat = []
end = 0

# VK groups info for reading

public = { 'items' : [
						{	'name' : 'techtroit', 
							'id' : -69107269 	},
						{	'name' : 'mnmlsm', 
							'id' : -80982654	},
						{	'name' : 'sklr', 
							'id' : -45327998	},
						{	'name' : 'IMAGE',
							'id' : 	-54179178	},				
						{	'name' : 'SKYFALL',	
							'id' : -39669294	}
					]
		}
citat = { 'items' : [
						{	'name' : 'cfb',	
							'id' : -31164499	}
					]
		}
images = { 'items' : [
						{	'name' : 'VILLAN',
							'id': -46773594		}
					

					]
		}
# List text sources 		

pub = list(i['id'] for i in public['items'] if i['name']=='techtroit')


mypost = '''Привет. Одиноко? Грустно? Скучно? Нужен собеседник понимающий? - Забудь эти проблемы! Я их решу за тебя. Всего за 100$ в час. Без интима. Предоплата - 20$, без возврата. \n\nP.S. Детям не беспокоить без родителей.'''


class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)
      self.count = 0
   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

# Main Programm Classes and Functions

class Comb:
	'''Super VK combain making collecting and post any data'''

	def __init__( self ):

		self.max = 'dd'
		self.ok = 'dd'
		self.group_ids = [-57014305, -60409637, -33881737]
		self.group_Ids_ToString = str.join(',', [str(abs(x)) for x in self.group_ids])
		self.groups = json.dumps(vkapi.groups.getById(group_ids=self.group_Ids_ToString),indent=4, sort_keys=True, ensure_ascii=False)
		self.group_names = [i['name'] for i in json.loads(self.groups)]
		self.dict_names_and_ids={};
		for i,x in zip(self.group_names, self.group_ids):
			self.dict_names_and_ids[i]=x
	


	def dateChecker(self):

		# Waiting for the post to give parametrs of group walls and date of current post

		while 1:
			Comb.getWall('self', 'no', person[0], 'text', 1)
			time.sleep(0.8)

	def getWall( self, offset,  ioffset, wall_id, dtype, count = 1, bot='no', sdate='no', likes='no', user_id = 179349317  ):
		'''Get music, image, text data from the wall'''
		rid = []
		text=[]
		ids = []
		i = 0
		new=[]
		step = -50
		date = []
		formattime = '%y-%m-%d %H:%M:%S'
		now = datetime.strptime(datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S'), '%y-%m-%d %H:%M:%S')

		# Looking for Post IDs without offset 
		if offset =='yes' and dtype == 'photo':
			urls = []
			step = -10
			dros = []
			
			while step < 10:
				step+=10
				wall = vkapi.wall.get( owner_id = wall_id, count = count, offset = step)
				dros.append(json.dumps(wall))
				time.sleep(0.6)
			print(json.loads(dros))
				
		if offset == 'no' and dtype == 'photo' :
			urls = []

			wall = vkapi.wall.get( owner_id = wall_id, count = count )
			for i in wall['items']:
				# print(json.dumps(i['attachments']['photo'], sort_keys=True, indent=4,ensure_ascii=False))
				# urls.append(i)
				if 'attachments' in i:
					for a in i['attachments']:
						if 'photo' in a:
							urls.append(a['photo']['photo_604'])

			return urls

			# 			if a['photo']:
			# 				urls.append(a['photo']['photo_604'])
			# return print(urls)

		if offset == 'no' and dtype == 'id':
			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					wall = vkapi.wall.get( owner_id = i['id'], count = count )
					ids.append(wall)

				if likes == 'yes':
					for i in ids:
						for a in i['items']:
							if a['likes']['count'] > 10:
								new.append( str(a['owner_id']) + '_'+  str(a['id']) )
				return ids

			if type(wall_id) == int:

				wall = vkapi.wall.get(owner_id=wall_id, count=count)
				for i in wall['items']:
					ids.append(i['id'])

					return  ids

				if likes == 'yes':
					for i in ids:
						for a in i['items']:
							if a['likes']['count'] > 10:
								new.append( str(a['owner_id']) + '_'+  str(a['id']) )

					return


		# Looking for text in posts without offset

		elif offset == 'no' and dtype == 'text' :

			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					wall = vkapi.wall.get( owner_id = i['id'], count = count )
					ids.append(wall)
				for i in ids:
					for a in i['items']:
						text.append(str(a['text']))
						print(text)

						return 

			elif type(wall_id) == int and bot == 'yes':

				wall = vkapi.wall.get( owner_id = wall_id, count = count )
				text.append(wall)
				for i in text[0]['items']:
					timeToPlus = datetime.strptime(datetime.fromtimestamp(i['date']).strftime('%d.%m.%y %H:%M:%S'), "%d.%m.%y %H:%M:%S")
					plusTime = dd+timedelta(seconds=5)

					if plusTime == now:
						comment1 = vkapi.wall.addComment( owner_id=wall_id, post_id=i['id'], text=random.choice(phrases) )
						post = comment1['comment_id']
						hoo = Comb.getWall('self', 'no', person[0], 'id', 1)
						getcomm = vkapi.wall.getComments( owner_id=wall_id, post_id=hoo[0] )
						if getcomm:
							print(getcomm)



			elif type(wall_id) == int and bot == 'no':
				wall = vkapi.wall.get( owner_id = wall_id, count = count )
				text.append(wall)
				for i in text[0]['items']:
					print(i['text'])



		elif offset == 'yes' and dtype == 'text':
			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					while step < 100:
						step+=50
						wall = vkapi.wall.get( owner_id = i['id'], count = count, offset = step )
						ids.append(wall)
						time.sleep(1)
				for i in ids:
					for a in i['items']:
						text.append(str(a['text']))
						supercitat.append(str(a['text']))
				return text
			if type(wall_id) == int:
				while step < ioffset:
					step+=50
					wall = vkapi.wall.get( owner_id = wall_id, count = count, offset = step )
					ids.append(wall)
					# time.sleep(1)
				for i in ids:
					for a in i['items']:
						if a['from_id']==user_id: 
							print(json.dumps(a['text'], indent=4, sort_keys=True, ensure_ascii=False), '\n')
					# print(j)



	# def getCitat( self ):

	# 	items = Comb.getWall('self', 'yes', citat, 'text', 50)
	# 	return items

	def rePost( self ):
		pids = Comb.getWall('self', 'no', public, 'id', 1)
		lol = []
		for i in pids:
			vkapi.wall.repost( object = 'wall' + str(i))
			time.sleep(1)


	def getTopic():
		
		topic_ids = []
		topics = vkapi.board.getTopics( group_id = 53664217 )

		for i in topics['items']:
			if i['title'] == 'ЧАТ':
				topic_ids.append(i['id'])
		return topic_ids
	

	def getPhoto( self, wall_id, album, count, download='no', path='./', dtype='id', multi='no', wall='no' ):

		pho = []
		
		groupName = vkapi.groups.getById( group_id = abs(wall_id))[0]['name']


		if wall == 'yes':
			photoFromWall = Combain.getWall('no', wall_id, 'photo', count)
			for i in photoFromWall:
				if not os.path.exists(path+groupName):
					os.mkdir(path=path+groupName)

				elif not os.path.exists( path+groupName ):
					os.mkdir( path=path+groupName ) 
				else:	
					wget.download( i, out=path+groupName )
		else:

			if multi == 'no' and type(album)==int:
				photos = vkapi.photos.get( owner_id = wall_id, album_id = album['id'], count = count ,  v=5.34 )	
				for i in photos['items']:
					if i['photo_604']:
						if download == 'yes':
							
						# pho.append(i['photo_604'])
							wget.download(i['photo_604'], out=path)
						if dtype == 'id':
							pho.append(i['id'])
						elif dtype == 'url':
							pho.append(i['photo_604'])
			
				return print(pho)

			elif multi == 'yes' and type(album) == list:
				urls=[]
				step = 0			
				if download == 'yes':
					for i in album:
						if i['count'] >= 1000:

							offs = i['count']-800
							step = step - offs
						else:
							offs = 0
						while step < i['count']:
							step+=offs
							for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], offset=step, v=5.34 )['items']:
								if i['id'] == a['album_id']:
									print(i)
									# if not os.path.exists(path+groupName):
									# 	os.mkdir(path=path+groupName)

									# elif not os.path.exists( path+groupName + '/' +str(i['title'] ) ):
									# 	os.mkdir( path=path+groupName + '/' + str(i['title'])  ) 
									# else:	
									# 	wget.download( a['photo_604'], out=path+groupName+'/'+str(i['title']) )
				if download == 'no':

						for i in album:
							for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], v=5.34 )['items']:
								if i['id'] == a['album_id']:
									if 'photo_604' in a:

										print(json.dumps(a['photo_604'], indent=4, sort_keys=True, ensure_ascii=False))
									else:
										print(json.dumps(a, indent=4, sort_keys=True, ensure_ascii=False))


	def getAlbums(self, public_id, count):
		titles = []
		ids= []
		albums = vkapi.photos.getAlbums( owner_id = public_id, count = count)['items']
		for i in albums:
			# ids.append({"id":i['id'], "title":i['title'], "count":i['size']})
			ids.append(dict(id=i['id'], title=i['title'], count=i['size']))

		# print("TITLE:",i['title'],'\nID: ',i['id'])
		# dids = json.loads(ids)
		return ids


	def copyPhoto( self, owner_id, titleNewAlbum, fromWall ):
		album_id=[]
		photo_id=[]
		albumToCreate = vkapi.photos.createAlbum( group_id=owner_id, title=titleNewAlbum, privacy_view='friends_of_friends_only ', privacy_comment='friends_of_friends_only ', v=5.34 )
		photosToCopy = Comb.getPhoto('self', fromWall, 'wall', 1 )
		albumsToGet = vkapi.photos.getAlbums( owner_id=owner_id, v='5.34' )
		for i in albumsToGet['items']:
			if i['title'] == 'TEST':
				album_id.append(i['id'])

		photosToCopy = Comb.getPhoto('self', fromWall, 'wall', 100 )
		for i in photosToCopy:
			copyPhotos = vkapi.photos.copy(owner_id=fromWall, photo_id=i, v='5.34')
			movePhotos = vkapi.photos.move(owner_id=owner_id, target_album_id=album_id[0], photo_id=copyPhotos, v='5.34')
			time.sleep(0.8)
			print("Copied to " + str(album_id[0]) + '  - ' + str(copyPhotos))
			for i in copyPhotos:
				photo_id.append(i)

			for i in photo_id:
				movePhotos = vkapi.photos.move(owner_id=owner_id, target_album_id=album_id[0], photo_id=i, v='5.34')
			

		
		print(photo_id[0])
		
		# return print(copyPhotos)

	def postTopicComment( self ):
		'''Post comment into topic block of group'''

		topic_id = Comb.getTopic() 
		# vkapi.board.addComment( group_id = 53664217, topic_id = topic_id[0], text = str( random.choice( slist ) ) )

		print(' TOPIC ID: ' + str(topic_id[0]) + '\n\n' + "{:-^50}".format("") +'\n') 
		return


	def postMulti( self, feed, mins):
		
		i=-1
		group = str;
		# print('Computer make post photos now... \nTotal number of posts: ' + str(i+1))
		while 1:
			i+=1
			if i == len(self.groups)-1:
				Comb.postTopicComment('self')
				i=-1
			group = str(self.groups[i])
			ok2 = group[:]
			# group = str(random.choice(groups))
			if type(feed) == list:
				words = random.choice( feed )
				ok = words[:]
			elif type(feed) == str and not 'wiki':
				words = feed
				ok = words
			elif type(feed) == str or 'wiki':
					words=wiki()
					ok=words

			# vkapi.wall.post( owner_id = ok2,  message = ok )
			print(' PUBLIC ID: ' + str(ok2) + '\n\n TEXT: \n\n  ' + str(ok) + '\n\n' + "{:-^50}".format("")+ '\n')

			if end == 1:
				break
			time.sleep(60*mins)

		
	
	def postOne( self ):

		dd = getPhoto( 'self', -73484869, 'wall', 10 )
		i=0
		while i < len( dd ):
			i+=1	
			vkapi.wall.post( owner_id = person[0],  attachments = 'photo179349317_4967352, photo-73484869_' + str( dd[i] ) )
			time.sleep(10)
		# return print(self.groups)	
		# 
	def changeOwnPhoto( self ):
		result = vkapi.photos.getOwnerPhotoUploadServer(owner_id=person[0])
		# webbrowser.open_new_tab(result['upload_url'])
		# save = vkapi.saveOwnerPhoto(server=result['upload_url'])

		print (result)
		return
	def getDialogs(self, delete='no', count=1):
		dialogs = vkapi.messages.getDialogs(count=200)
		ids = [i['message']['user_id'] for i in dialogs['items']]
		for i in ids:
			vkapi.messages.deleteDialog(user_id=i)
			time.sleep(0.6)

	
def wiki():
	try:
		wikipedia.set_lang('ru')
		# wpage = wikipedia.summary('Билл Клинтон', sentences=5)
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=5)
	except:
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=5)
	return summ


# storage = cgi.FieldStorage()
# action = storage.getvalue('action')
# if action == 'multi':
# 	# dd=[1,2,3]
# 	# # for i in dd:
# 	# while 1:
# 	# 	# print(i)
# 	# 	sys.stdout.write('ok')
# 	# 	sys.stdout.flush()
# 	# 	time.sleep(1)
# 	class MyApplication(object):
# 	    def __call__(self, environ, start_response):
# 	        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
# 	        return self.page()

# 	    def page(self):
# 	        yield '<html><body>'
# 	        for i in range(10):
# 	            yield '<div>%i</div>'%i
# 	            time.sleep(1)

# 	application= MyApplication()
# 	if __name__=='__main__':
# 	    wsgiref.handlers.CGIHandler().run(application)
	# try:
	# 	Combain = Comb()
	# 	Combain.postMulti(slist)
	# 	exit = storage.getvalue('exit')
	# 	if exit == 1:
	# 		end = 1
	# except:
	# 	Combain.postMulti(vselen+psy+mudreci)
if __name__ == "__main__":
	Combain = Comb()
	# aa = Combain.getAlbums(-40485321)
	# # Combain.postOne()
	# Combain.getWall('no', -32149661, 'photo', 20, 'yes') #args (offset, wall_id, dtype, count = 1, bot='no', sdate='no', likes='no')
	# Combain.getWall('yes', -32149661, 'photo', 20) #args (offset, wall_id, dtype, count = 1, bot='no', sdate='no', likes='no')
	# Combain.dateChecker()
	# Combain.getCitat()
	# Combain.getAlbums(-57014305, 1)

	# Combain.getPhoto( -57014305, Combain.getAlbums(-57014305, 2), 1, 'yes', '/Users/hal/', 'id', 'yes', 'no')
	# Combain.getPhoto( -57014305, 'none', 50, 'yes', '/Users/hal/', 'id', 'yes', 'yes')
	# Combain.rePost()
	# Combain.copyPhoto( person[0], 'JOsdfasdfKER', -32149661 )
	# Combain.changeOwnPhoto()
	# Combain.getDialogs()
	

	# print('{:=^80}'.format(" Wellcome to VK API combain ") + '\n\n  Please type kind of action would you like to do with this program.\n\n')

	# actions = ['multi-post', 'download photo', 'copy photo', 'auto reply', 'get text from wall,']

	# elist = [i for i in enumerate(actions, start=1)]
	# for i in elist:
	# 	for a in i:
	# 		print(a)
	# 	# print('%s. %s\n' % (i, actions[i]))
	# 	# print('   %s\n' % (str(i)))


	
	# def actions():
	# 	action = input('Enter action: ')

	# 	if int(action) == 1:
	# 		mins = int(input('Time delay in minutes: '))
	# 		try:
	# 			Combain.postMulti(psy+psy2+mudreci2+mudreci, mins)
	# 		except:
	# 			Combain.postMulti(psy+psy2+mudreci2+mudreci, mins)
	# 	elif int(action) == 5:
	# 		ioffset = int(input('Offset: '))
	# 		from_id = int(input('From_id: '))
	# 		count = int(input('Count: '))
	# 		Combain.getWall('yes', ioffset, -57014305, 'text', count)
	# 	elif int(action) == 2:
	# 		groupId = int(input('group id: '))
	# 		countAlbums = int(input('count albums: '))
	# 		countPhotos = int(input('count photos: '))
	# 		path = input('path to save: ')
	# 		print('Downloading...')
	# 		Combain.getPhoto( groupId, Combain.getAlbums(groupId, countAlbums), 'none', 'yes', path, 'id', 'yes', 'no')

	# actions()

	