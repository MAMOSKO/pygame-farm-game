from os import environ
from random import randint

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import pygame.image
from json import loads as jsonLoad

pygame.init()
pygame.mixer.init()


class game:
	def __init__(self):
		self.windowSize=[1280,720]
		#self.window=pygame.display.set_mode((self.windowSize[0],self.windowSize[1]))
		self.window=pygame.display.set_mode((self.windowSize[0],self.windowSize[1]),pygame.FULLSCREEN | pygame.SCALED | pygame.HWSURFACE)
		self.clock=pygame.time.Clock()

		self.MAINLOOP=True

		self.createObjects()
		self.createMap()
		self.crt_inventory()
		self.game()



	def createObjects(self):

		self.font=pygame.font.Font("TfFancy.ttf",32)
		#self.fontsmall=pygame.font.Font("Atari.ttf",14)


		self.name=self.font.render("FATIH",True,(252,15,192))
		self.name_r=self.name.get_rect()
		self.name_r.center=(self.windowSize[0]/2,self.windowSize[1]/2-30)


		self.house=pygame.image.load("assets/Objects_Sliced/farm_house.png").convert_alpha()
		#self.house=pygame.transform.scale(self.house,(self.windowSize[0]/5,self.windowSize[1]/3))
		self.house_r=self.house.get_rect()


		self.chicken_h=pygame.image.load("assets/Objects_Sliced/chicken_house.png").convert_alpha()
		self.chicken_h=pygame.transform.scale(self.chicken_h,(self.windowSize[0]/8,self.windowSize[1]/4))
		self.chicken_h_r=self.chicken_h.get_rect()

		self.house_r.center=(self.windowSize[0]/2,self.windowSize[1]/2)
		self.grasses=[]
		for temp in range(0,77):
			tempIm=pygame.image.load(f"assets/Grasses/Grass{temp}.png").convert_alpha()
			tempIm=pygame.transform.scale(tempIm,(self.windowSize[0]/22,self.windowSize[1]/14))
			self.grasses.append(tempIm)

		self.gis=self.grasses[1].get_size()
		self.grasses_r=[]
		temp_count=0
		for temp in self.grasses:
			temp=self.grasses[temp_count].get_rect()
			self.grasses_r.append(temp)
			temp_count+=1


		self.roads=[]
		for temp in range(0,77):
			tempIm=pygame.image.load(f"assets/Roads/Road_{temp}.png").convert_alpha()
			tempIm=pygame.transform.scale(tempIm,(self.windowSize[0]/22,self.windowSize[1]/14))
			self.roads.append(tempIm)

		self.ris=self.roads[1].get_size()

		self.roads_r=[]
		temp_count=0
		for temp in self.roads:
			temp=self.roads[temp_count].get_rect()
			self.roads_r.append(temp)
			temp_count+=1


		self.bioms=[]
		for temp in range(0,33):
			tempIm=pygame.image.load(f"assets/Biom/biom{temp}.png").convert_alpha()
			tempImSize=tempIm.get_size()


			tempW=tempImSize[0]*2.7
			tempH=tempImSize[1]*2.7
			tempIm=pygame.transform.scale(tempIm,(tempW,tempH))
			self.bioms.append(tempIm)


		self.bioms_r=[]
		temp_count=0
		for temp in self.bioms:
			temp=self.bioms[temp_count].get_rect()
			self.bioms_r.append(temp)
			temp_count+=1




		#Character Normal
		self.character0=pygame.image.load("assets/Character/character0.png").convert_alpha()
		self.character0=pygame.transform.scale(self.character0,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character01=pygame.image.load("assets/Character/character1.png").convert_alpha()
		self.character01=pygame.transform.scale(self.character01,(self.windowSize[0]/11,self.windowSize[1]/7))



		self.character1=pygame.image.load("assets/Character/character4.png").convert_alpha()
		self.character1=pygame.transform.scale(self.character1,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character11=pygame.image.load("assets/Character/character5.png").convert_alpha()
		self.character11=pygame.transform.scale(self.character11,(self.windowSize[0]/11,self.windowSize[1]/7))



		self.character2=pygame.image.load("assets/Character/character12.png").convert_alpha()
		self.character2=pygame.transform.scale(self.character2,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character21=pygame.image.load("assets/Character/character13.png").convert_alpha()
		self.character21=pygame.transform.scale(self.character21,(self.windowSize[0]/11,self.windowSize[1]/7))



		self.character3=pygame.image.load("assets/Character/character8.png").convert_alpha()
		self.character3=pygame.transform.scale(self.character3,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character31=pygame.image.load("assets/Character/character9.png").convert_alpha()
		self.character31=pygame.transform.scale(self.character31,(self.windowSize[0]/11,self.windowSize[1]/7))



		#Character Run
		self.character02=pygame.image.load("assets/Character/character2.png").convert_alpha()
		self.character02=pygame.transform.scale(self.character02,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character03=pygame.image.load("assets/Character/character3.png").convert_alpha()
		self.character03=pygame.transform.scale(self.character03,(self.windowSize[0]/11,self.windowSize[1]/7))


		self.character12=pygame.image.load("assets/Character/character6.png").convert_alpha()
		self.character12=pygame.transform.scale(self.character12,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character13=pygame.image.load("assets/Character/character7.png").convert_alpha()
		self.character13=pygame.transform.scale(self.character13,(self.windowSize[0]/11,self.windowSize[1]/7))


		self.character22=pygame.image.load("assets/Character/character14.png").convert_alpha()
		self.character22=pygame.transform.scale(self.character22,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character23=pygame.image.load("assets/Character/character15.png").convert_alpha()
		self.character23=pygame.transform.scale(self.character23,(self.windowSize[0]/11,self.windowSize[1]/7))


		self.character32=pygame.image.load("assets/Character/character10.png").convert_alpha()
		self.character32=pygame.transform.scale(self.character32,(self.windowSize[0]/11,self.windowSize[1]/7))
		self.character33=pygame.image.load("assets/Character/character11.png").convert_alpha()
		self.character33=pygame.transform.scale(self.character33,(self.windowSize[0]/11,self.windowSize[1]/7))


		self.character_r=self.character0.get_rect()
		self.character_r.center=(self.windowSize[0]/2,self.windowSize[1]/2)
		self.characterAn=0
		self.press=False
		self.now=pygame.time.get_ticks()
		self.animationPart=0
		self.speed=4
		self.animation_speed_normal=750
		self.animation_speed_run=200




		self.chicken_text=self.font.render("YUMURTA TOPLA!    [SPACE]",True,(255,125,0))
		self.chicken_text_r=self.chicken_text.get_rect()
		self.chicken_text_r.center=(self.windowSize[0]/2,self.windowSize[1]/2+300)




		#animals
		self.chicken0=pygame.image.load("assets/Animals/chicken_0.png").convert_alpha()
		self.chicken0=pygame.transform.scale(self.chicken0,(30,30))
		self.chicken0_f=self.flip_image(self.chicken0)

		self.chicken1=pygame.image.load("assets/Animals/chicken_1.png").convert_alpha()
		self.chicken1=pygame.transform.scale(self.chicken1,(30,30))
		self.chicken1_f=self.flip_image(self.chicken1)


		self.chicken_l=[self.chicken0,self.chicken1,self.chicken0_f,self.chicken1_f]


		self.chicken_r=self.chicken0.get_rect()


	def createMap(self):
		mapReadO=open("settings/map.json","r")
		mapRead=mapReadO.read()
		mapReadO.close()
		mapReadD=jsonLoad(mapRead)
		self.mapLeft=0
		self.mapTop=0
		self.map_grass=mapReadD["grasses"]
		self.map_road=mapReadD["roads"]
		self.map_biom=mapReadD["biom"]
		self.map_chicken=mapReadD["chickens"]

	def flip_image(self,image):
		return pygame.transform.flip(image,True,False)



	def crt_inventory(self):
		self.inventory_size=[self.windowSize[0]/3,self.windowSize[1]/10]
		self.inventory_location=[self.windowSize[0]/2-self.inventory_size[0]/2,self.windowSize[1]/25]
	def inventory_f(self):
		pygame.draw.rect(self.window,(19,186,91),(self.inventory_location[0],self.inventory_location[1],self.inventory_size[0],self.inventory_size[1]),0,10)
		pygame.draw.rect(self.window,(200,60,160),(self.inventory_location[0],self.inventory_location[1],self.inventory_size[0],self.inventory_size[1]),4,10)

		inner_x=self.inventory_size[0]-4*2

		pygame.draw.line(self.window,(200,60,160),(self.inventory_location[0]+4+inner_x/4,self.inventory_location[1]),(self.inventory_location[0]+4+inner_x/4,self.inventory_location[1]+self.inventory_size[1]-2),4)
		pygame.draw.line(self.window,(200,60,160),(self.inventory_location[0]+4+inner_x/4*2,self.inventory_location[1]),(self.inventory_location[0]+4+inner_x/4*2,self.inventory_location[1]+self.inventory_size[1]-2),4)
		pygame.draw.line(self.window,(200,60,160),(self.inventory_location[0]+4+inner_x/4*3,self.inventory_location[1]),(self.inventory_location[0]+4+inner_x/4*3,self.inventory_location[1]+self.inventory_size[1]-2),4)
	def controls(self):
		self.keys=pygame.key.get_pressed()

		if self.keys[pygame.K_UP]:
			self.characterAn=1
			self.press=True
			self.mapTop+=self.speed
		elif self.keys[pygame.K_DOWN]:
			self.characterAn=0
			self.press=True
			self.mapTop-=self.speed
		elif self.keys[pygame.K_RIGHT]:
			self.characterAn=2
			self.press=True
			self.mapLeft-=self.speed
		elif self.keys[pygame.K_LEFT]:
			self.characterAn=3
			self.press=True
			self.mapLeft+=self.speed
		else:self.press=False
		if self.keys[pygame.K_r]:self.createMap()
	def changeAnimation(self):
		if self.animationPart==0:self.animationPart=1
		else:self.animationPart=0
		self.now=pygame.time.get_ticks()
	def game(self):
		while self.MAINLOOP:
			self.controls()
			self.window.fill((0,0,0))
			for event in pygame.event.get():
				if event.type==pygame.QUIT:self.MAINLOOP=False


			#Map-Grasses
			for grass in self.map_grass:
				self.window.blit(self.grasses[grass[2]],(0+self.gis[0]*grass[0]+self.mapLeft,0+self.gis[1]*grass[1]+self.mapTop),self.grasses_r[grass[2]])
			#Map-Roads
			for road in self.map_road:
				self.window.blit(self.roads[road[2]],(0+self.ris[0]*road[0]+self.mapLeft,0+self.ris[1]*road[1]+self.mapTop),self.roads_r[road[2]])
			#Map-Biom
			for biom in self.map_biom:
				self.window.blit(self.bioms[biom[2]],(0+self.gis[0]*biom[0]+self.mapLeft,0+self.gis[1]*biom[1]+self.mapTop),self.bioms_r[biom[2]])

			self.house_r.center=(self.windowSize[0]/2+self.mapLeft,self.windowSize[1]/2+self.mapTop-460)
			self.window.blit(self.house,self.house_r)


			self.chicken_h_r.center=(self.windowSize[0]/2+self.mapLeft+250,self.windowSize[1]/2+self.mapTop)
			self.window.blit(self.chicken_h,self.chicken_h_r)


			if self.chicken_h_r.colliderect(self.character_r):
				self.window.blit(self.chicken_text,self.chicken_text_r)

			self.window.blit(self.name,self.name_r)
			self.inventory_f()
			

			#Chickens
			for chicken in self.map_chicken:
				if chicken[2]==0:
					if pygame.time.get_ticks()-chicken[3]>1000:
						chicken[2]=2
						chicken[3]=pygame.time.get_ticks()
				else:
					if pygame.time.get_ticks()-chicken[3]>1000:
						chicken[2]=0
						chicken[3]=pygame.time.get_ticks()


				self.window.blit(self.chicken_l[chicken[2]],(self.windowSize[0]/2+self.mapLeft+chicken[0],self.windowSize[1]/2+self.mapTop+chicken[1]),self.chicken_r)


			#Character
			if self.characterAn==0 and not self.press:
				if self.animationPart==0:self.window.blit(self.character0,self.character_r)
				else:self.window.blit(self.character01,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_normal:self.changeAnimation()
			elif self.characterAn==1 and not self.press:
				if self.animationPart==0:self.window.blit(self.character1,self.character_r)
				else:self.window.blit(self.character11,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_normal:self.changeAnimation()
			elif self.characterAn==2 and not self.press:
				if self.animationPart==0:self.window.blit(self.character2,self.character_r)
				else:self.window.blit(self.character21,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_normal:self.changeAnimation()
			elif self.characterAn==3 and not self.press:
				if self.animationPart==0:self.window.blit(self.character3,self.character_r)
				else:self.window.blit(self.character31,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_normal:self.changeAnimation()



			elif self.characterAn==0 and self.press:
				if self.animationPart==0:self.window.blit(self.character02,self.character_r)
				else:self.window.blit(self.character03,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_run:self.changeAnimation()
			elif self.characterAn==1 and self.press:
				if self.animationPart==0:self.window.blit(self.character12,self.character_r)
				else:self.window.blit(self.character13,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_run:self.changeAnimation()
			elif self.characterAn==2 and self.press:
				if self.animationPart==0:self.window.blit(self.character22,self.character_r)
				else:self.window.blit(self.character23,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_run:self.changeAnimation()
			elif self.characterAn==3 and self.press:
				if self.animationPart==0:self.window.blit(self.character32,self.character_r)
				else:self.window.blit(self.character33,self.character_r)
				if pygame.time.get_ticks()-self.now>self.animation_speed_run:self.changeAnimation()
			#self.grass1=pygame.Rect(0,0,2*self.grassesSizeOne,self.grassesSizeOne)
			#self.window.blit(self.grasses,(0,0),self.grass1)
			pygame.display.update()
			self.clock.tick(60)


game()