import sys, os
import time

from PIL import Image
import numpy

def getTxt(imagePath, txtPath):
    img_count = 1
    while img_count <= len(os.listdir(imagePath)):
        imageFile = imagePath + str(img_count) + '.png'
        txtFile = txtPath + str(img_count) + '.txt'
        image2txt(imageFile, txtFile)
        #print('Loading： ' + str(img_count) + '%')
        img_count += 1

def play(txtPath):
    print("Start playing")
    txt_count = 1
    while txt_count <= len(os.listdir(txtPath)):
        """"os.system('type ' + txtPath + str(txt_count) + '.txt')"""""

        os.system('type ' + txtPath + str(txt_count) + '.txt')
        time.sleep(1.0/40)
        txt_count += 1
        os.system('cls')


def image2txt(inputFile, outputFile):
    im = Image.open(inputFile).convert('L')
    charWidth = 100
    im = im.resize((charWidth, charWidth // 2))
    target_width, target_height = im.size
    data = numpy.array(im)[:target_height, :target_width]
    f = open(outputFile, 'w',encoding='utf-8')
    for row in data:
        for pixel in row:
            if pixel > 127:
                f.write('1')
            else:
                f.write(' ')
        f.write('\n')
    f.close()

if __name__ == '__main__':
    txt_dir_path = 'D:/python_fun/txt/'
    img_dir_path = 'D:/python_fun/images/'
    display_path = r'D:\\python_fun\\txt\\'
    #getTxt(img_dir_path, txt_dir_path)
    play(display_path)
