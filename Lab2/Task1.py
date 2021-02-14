dictionary={}
file=open('Eng_test.txt', 'r')
#file=open('Rus_test.txt', 'r')
lines=file.readlines()
lines=[line.rstrip() for line in lines]
for line in lines:
    for letter in line:
        if letter.isalpha():
            dictionary[letter.lower()]=dictionary.get(letter.lower(),0)+1
out=sorted(dictionary.items(), key=lambda i: i[1], reverse=True)
for value in out:
    print(value[0], ':', value[1])
file.close()
