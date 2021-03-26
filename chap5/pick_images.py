#coding:utf-8

'''
    filename:pick_images.py
        chap:5
    subject:22
    conditions:filenames
    solution:pick up images
'''




filenames = [
        'a.py',
        'b.jpg',
        'c.gif',
        'd.map',
        'e.png',
        'f.jpg',
        'k.txt',
        'f.gif',
        'h.png',
        'm.docx']


#image_types = ['jpg','gif','png']
image_types = ['.jpg','.gif','.png']


def pick_up_images(filenames,image_types):
    #return list(filter(lambda fn:fn.rpartition('.')[2] in image_types,filenames))
    images = []
    for fn in filenames:
        for tp in image_types:
            if fn.endswith(tp):
                images.append(fn)
    return images
        



images = pick_up_images(filenames,image_types)


print('files:',filenames)
print('images in files:',images)


