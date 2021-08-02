import re

def update_counter(count):
    if __name__ == '__update_counter__':
        update_counter()

    with open('../database/datasetcounter.txt', 'r+') as f:
        text = f.read()
        text2 = int(text)+1
        text = re.sub(count, str(text2), text)
        f.seek(0)
        f.write(str(text))
        f.truncate()
    return

def get_and_update_counter():
    if __name__ == '__get_and_update_counter__':
        get_and_update_counter()

    with open('../database/datasetcounter.txt','r') as f:
        count = f.readline()
        update_counter(count)
        return count

def get_counter():
    if __name__ == '__get_counter__':
        get_counter()

    with open('../database/datasetcounter.txt','r') as f:
        count = f.readline()
        return count

# print(get_counter())
