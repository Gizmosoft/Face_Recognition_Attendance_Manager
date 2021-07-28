import re

def update_counter(count):
    with open('datasetcounter.txt', 'r+') as f:
        text = f.read()
        text2 = int(text)+1
        text = re.sub(count, str(text2), text)
        f.seek(0)
        f.write(str(text))
        f.truncate()
    return

def get_counter():
    with open('datasetcounter.txt','r') as f:
        count = f.readline()
        update_counter(count)
        return count

# print(get_counter())
