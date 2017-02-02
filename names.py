import csv
import login

def main():
	emailsToSave = []
	with open('names.csv') as csvFile:
		reader = csv.reader(csvFile, delimiter = ',')
		for row in reader:
			validEmails = []
			firstName = row[0]
			middleName = row[1]
			lastName = row[2]
			domain = row[3]
			generatedEmails = generateEmails(firstName, middleName, lastName, domain)
			validEmails = login.testEmails(generatedEmails)
			emailsToSave.extend(validEmails)
	writeToFile(emailsToSave)


'''
Generate possible email permutations that might be valid given the domain
'''
def generateEmails(firstName, middleName, lastName, domain):

	#Found at https://github.com/SudhanshuC/EmailPermute-Rapportive, a more comprehensive permutations list
	firstInitial=firstName[0]
	lastInitial=lastName[0]
	if len(middleName):
	 middleInitial=middleName[0]
	else:
	 middleInitial="" 
	
	
	emailsWithMiddleInitial =[
		firstInitial+middleInitial+lastName+'@'+domain,
		firstInitial+middleInitial+'.'+lastName+'@'+domain,
		firstName+middleInitial+lastName+'@'+domain,
		firstName+'.'+middleInitial+'.'+lastName+'@'+domain,
		firstInitial+middleInitial+'-'+lastName+'@'+domain,
		firstName+'-'+middleInitial+'-'+lastName+'@'+domain,
		firstInitial+middleInitial+'_'+lastName+'@'+domain,
		firstName+'_'+middleInitial+'_'+lastName+'@'+domain
	]

	emailswithMiddleName =[
		firstName+middleName+lastName+'@'+domain,
		firstName+'.'+middleName+'.'+lastName+'@'+domain,
		firstName+'-'+middleName+'-'+lastName+'@'+domain,
		firstName+'_'+middleName+'_'+lastName+'@'+domain
	]

	emails=[
	firstName+'@'+domain,
	lastName+'@'+domain,
	firstName+lastName+'@'+domain,
	firstName+'.'+lastName+'@'+domain,
	firstInitial+lastName+'@'+domain,
	firstInitial+'.'+lastName+'@'+domain,
	firstName+lastInitial+'@'+domain,
	firstName+'.'+lastInitial+'@'+domain,
	firstInitial+lastInitial+'@'+domain,
	firstInitial+'.'+lastInitial+'@'+domain,
	lastName+firstName+'@'+domain,
	lastName+'.'+firstName+'@'+domain,
	lastName+firstInitial+'@'+domain,
	lastName+'.'+firstInitial+'@'+domain,
	lastInitial+firstName+'@'+domain,
	lastInitial+'.'+firstName+'@'+domain,
	lastInitial+firstInitial+'@'+domain,
	lastInitial+'.'+firstInitial+'@'+domain,
	firstName+'-'+lastName+'@'+domain,
	firstInitial+'-'+lastName+'@'+domain,
	firstName+'-'+lastInitial+'@'+domain,
	firstInitial+'-'+lastInitial+'@'+domain,
	lastName+'-'+firstName+'@'+domain,
	lastName+'-'+firstInitial+'@'+domain,
	lastInitial+'-'+firstName+'@'+domain,
	lastInitial+'-'+firstInitial+'@'+domain,
	firstName+'_'+lastName+'@'+domain,
	firstInitial+'_'+lastName+'@'+domain,
	firstName+'_'+lastInitial+'@'+domain,
	firstInitial+'_'+lastInitial+'@'+domain,
	lastName+'_'+firstName+'@'+domain,
	lastName+'_'+firstInitial+'@'+domain,
	lastInitial+'_'+firstName+'@'+domain,
	lastInitial+'_'+firstInitial+'@'+domain	
	]

	if len(middleName):
		emails.append(emailswithMiddleName)
		emails.append(emailsWithMiddleInitial)

	return emails



'''
Write emails to file line by line
'''
def writeToFile(validEmails):
	with open('validEmails') as writer:
		for email in validEmails:
			writer.write(email)
			writer.write("\n")


main()



