import csv
import login

def main():
	with open('names.csv') as csvfile:
		validEmails = []
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			firstName = row[0]
			middleName = row[1]
			lastName = row[2]
			domain = row[3]
			generatedEmails = generateEmails(firstName, middleName, lastName, domain)
			validEmails = login.testEmails(generatedEmails)
			for i in validEmails:
				print(i)

def generateEmails(firstName, middleName, lastName, domain):
 	emails = []
 	e1 = firstName + "@" + domain 
 	e2 = firstName + lastName + "@" + domain
 	e3 = firstName + "." + lastName + "@" + domain
 	e4 = lastName + "@" + domain
 	e5 = firstName[0] + lastName + "@" + domain
 	e6 = firstName[0] + "." + lastName  + "@" + domain
 	e7 = firstName + lastName[0] + "@" + domain
 	e8 = firstName + "." + lastName[0] + "@" + domain
 	e9 = firstName[0] + lastName[0] + "@" + domain
 	emails.append(e1)
 	emails.append(e2)
 	emails.append(e3)
 	emails.append(e4)
 	emails.append(e5)
 	emails.append(e6)
 	emails.append(e7)
 	emails.append(e8)
 	emails.append(e9)
 	return emails



main()



