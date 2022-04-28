
def load_data():
    path = './/func//shop.txt'
    file = open(path, 'r')
    content = file.read()
    lst = content.replace(" ",'').split('\n')
    lst = ' '.join(lst).split()
    file.close()
    return lst