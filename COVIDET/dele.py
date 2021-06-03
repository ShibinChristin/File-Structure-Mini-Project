def pos(s):
	a=open("positive.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("positive.txt","w+")
		for line in lines:
			b.write(line)
		b.close()
		t1.insert(END,"\nDeletion successfull")

def neg(m):
	a=open("negative.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(m)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("negative.txt","w+")
		for line in lines:
			b.write(line)
		b.close()
		