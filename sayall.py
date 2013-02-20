#!/usr/bin/python3
#coding: utf-8

# this script downloads words from google speech api and joins in one file
# for audio studing english

import sys
import wget
import os

def makefilename(filename):
    return '.' + os.sep + 'mp3res' + os.sep + filename

def appendfile(outputfile, lastfilename):
    fileobj = open(makefilename(lastfilename) + '.mp3', 'rb')
    filebytes = fileobj.read()
    outputfile.write(filebytes)
    fileobj.close()

onesecond = 'empty10'
# формат файла: одиночные слова без пробелов и других символов
# по одному слову на строку
def loadfile(filename):
    outputfile = open(filename + '.mp3', 'wb')
    appendfile(outputfile, onesecond)
    wordsfile = open(filename,'r')
    for line1 in wordsfile:
        line = line1.replace('\n', '')
        wordlen = len(line)
        print (" " + line)
        wget.download(line, makefilename)
        appendfile(outputfile, onesecond)
        appendfile(outputfile, line)
        appendfile(outputfile, onesecond)
        appendfile(outputfile, line)
        appendfile(outputfile, onesecond)
        for i in range(int(wordlen/2)):
            appendfile(outputfile, onesecond)


# главная функция
if __name__ == '__main__':
    if len(sys.argv) == 2:
        wordsfilename = sys.argv[1]
        print ("loading words from file " + wordsfilename)
        loadfile(wordsfilename)

    else:
        print ('attempt to load translate for test!')
        wget.download('test', makefilename)

