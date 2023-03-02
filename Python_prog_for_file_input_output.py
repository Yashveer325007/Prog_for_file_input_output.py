f=open('poem.txt')
t=f.read()
if 'sheep' in t:
    print("Word Sheep is present in Poem")
else:
    print("Word Sheep is not present in Poem")

f.close()

