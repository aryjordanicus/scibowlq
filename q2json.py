import os

r=open('allq.txt', 'r')
lines = r.readlines()
r.close()

is_q = False
q = ""
subj = ""
ans = ""

objs = []
bios = []

for line in lines:

	ls = line.split()

	if len(ls)>0:

		if ls[0] == "ANSWER:": 
			ans = line.replace("ANSWER: ", "")
			obj = {"subj": subj.replace("\n", ""), "q": q.replace("\n", "").strip(), "ans": ans.replace("\n", "").strip()}
			objs.append(obj)
			subj = ""
			q = ""
			ans = ""
			is_q = False

		if is_q:
			try:
				if subj=="": 
					subj = ls[1]
					q+=line[line.find(ls[1])+len(ls[1]):]
				else: q+=line
			except IndexError: 1==1

		if ls[0] in ["TOSS-UP", "BONUS"]:
			typ = ls[0]
			is_q = True
'''
subjs=[["BIOLOGY", "Biology"], 
["Physics", "PHYSICS"],
["Chemistry", "CHEMISTRY"],
["Math", "MATH"],
["Astronomy", "ASTRONOMY"],
["General", "GENERAL"],
["Earth", "EARTH"]]

num = 0

bio = open('earth.txt', 'w')

for obj in objs:
	if obj['subj'] in ["Earth", "EARTH"]:
		bio.write(str(num)+'\n')
		bio.write(obj['q']+2*'\n')
		bio.write("ANSWER: " + obj['ans']+2*'\n')
		num+=1

bio.close()
'''

for obj in objs:
	if obj['subj']=="BIOLOGY":
		bios.append({'q': obj['q'], 'ans': obj['ans']})

os.system('clear')

index = int(input(">> "))

for i in range(index, len(bios)-1):
	os.system('clear')
	print(i)
	print(bios[i]['q'])
	try: input("")
	except SyntaxError: pass
	os.system('clear')
	print(bios[i]['q']+'\n')
	print(bios[i]['ans'])
	try: input("")
	except SyntaxError: pass

