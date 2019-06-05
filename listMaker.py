import os
import random
import sys
import datetime

#get current recipes
allRecipes = os.listdir('recipes')

#if log file exits, read it. if not, create it
if os.path.exists('recipes/logFile'):
	logFile = open("recipes/logFile","r+")
	logData = logFile.readlines()
	parsedData  = [line.split() for line in logData]
	for i in allRecipes:
		newRecipe = 0
		for j in range(0,len(parsedData)):
			if i == parsedData[j][0]:
				newRecipe = 1
		if newRecipe == 0 and i != 'logFile':
			logFile.write("%s 0\n" %i)
	logFile.close
	logFile = open("recipes/logFile","r")
else:
	logFile = open("recipes/logFile","w+")
	for i in allRecipes:
		logFile.write("%s 0\n" %i)
	logFile.close
	logFile = open("recipes/logFile","r")


logData = logFile.readlines()
parsedData = [line.split() for line in logData]

check = 'n'
randList = []
while check == 'n':
	validChoices = [choice[0] for choice in parsedData if int(choice[1]) < 3]
	randRecipe = 0
	for i in range(1,4):
		randRecipe = random.randint(0,len(validChoices)-1)
		randList.append(validChoices[randRecipe])
		del validChoices[randRecipe]
	print('These recipes were selected: ')
	for i in randList:
		print(i)
	check = input('Is this list ok? ')
	if check == 'n':
		randList = []

ingredientList = []
ingredientQuantity = []
for i in randList: #i is the current recipe
	ingredientFound = 0
	curFile = open("recipes/" + i)
	tempList = curFile.readlines()
	for j in tempList: #j is the current ingredient
		ingredientFound = 0
		for k in range(0,len(ingredientList)): #k is ingredient from list of ingredients
			if j == ingredientList[k]:
				ingredientFound = 1
				ingredientQuantity[k] += 1
		if ingredientFound != 1:
			ingredientList.append(j)
			ingredientQuantity.append(1)

	for j in range(0,len(parsedData)):
		if i == parsedData[j][0]:
			parsedData[j][1] = 4

newPrintList = open("printMe", "w")
for i in range(0,len(ingredientList)):
	newPrintList.write("%d" %ingredientQuantity[i])
	newPrintList.write(" %s" %ingredientList[i])
	
newLog = open("recipes/logFile", "w")
for i in range(0,len(parsedData)):
	if int(parsedData[i][1]) > 0:
		parsedData[i][1] = int(parsedData[i][1]) - 1
	newLog.write("%s %s\n" %(parsedData[i][0], parsedData[i][1]))



	
