import os
import random
import sys
import datetime

numNeeded = int(input('How many recipes do you want generated? '))
numLeftover = int(input('How many recipes are left over from last week? '))
numNeeded -= numLeftover
leftOver = []
for i in range(0, numLeftover):
	tempPick = input('Leftover recipe %d: ' %(i+1))
	leftOver.append(tempPick)

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
randList = [] #leave this here or there is an error when trying to print later
if numNeeded > 0:
	check = 'n'
	while check == 'n':
		validChoices = [choice[0] for choice in parsedData if int(choice[1]) < 1]
		randRecipe = 0
		for i in range(0, numNeeded):
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
			parsedData[j][1] = 2


newPrintList = open("printMe", "w")
#print the 5 things we chose to eat
newPrintList.write("This is the %d dinner choices: \n" %(numNeeded + numLeftover))
for i in range(0,len(leftOver)):
	newPrintList.write("%s\n" %leftOver[i])

for i in range(0,len(randList)):
	newPrintList.write("%s\n" %randList[i])

if len(ingredientList) > 0:
	newPrintList.write("***********************\nThese are the ingredients:\n")
	for i in range(0,len(ingredientList)):
		newPrintList.write("______%d" %ingredientQuantity[i])
		newPrintList.write(" %s" %ingredientList[i])


	
newLog = open("recipes/logFile", "w")
for i in range(0,len(parsedData)):
	if int(parsedData[i][1]) > 0:
		parsedData[i][1] = int(parsedData[i][1]) - 1
	newLog.write("%s %s\n" %(parsedData[i][0], parsedData[i][1]))


newPrintList.write("**********************\nThese are the regular weekly items we need:\n")
weeklyList = ["mayo","milk","cheese","bread","eggs","ketchup","lettuce","carrots","cereal", 
"butter", "creamy peanut butter", "cruncy PB", "tuna", "chris ranch", "taz ranch", 
"jelly", "chili", "ramen", "chips", "lunchmeat", "mustard", "ice cream"]
for i in weeklyList:
	newPrintList.write("______%s\n" %i)
	
