name = raw_input("Enter file:")
if len(name) < 1 :
	name = "mbox-short.txt"
fhand = open(name)
maildict = {}

for line in fhand:
	if line.startswith("From "):
		lst=line.split()
		mail=lst[1]
		maildict[mail] = maildict.get(mail,0) + 1


greatestmail = None
greatestcount = None

for mail,count in maildict.items():
	if greatestcount is None or count > greatestcount:
		greatestmail = mail
		greatestcount = count

print greatestmail,greatestcount
