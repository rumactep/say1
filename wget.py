#!/usr/bin/python
#coding: utf-8

import subprocess

def GetCmd(word):
    cmdw = 'wget'
    useragent = ' -U "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5"'
    google = ' "http://translate.google.com/translate_tts?tl=en&q=' + word + '" -O ./"' + word + '.mp3"'
    result = cmdw + useragent + google
    return result

def download(word):
    cmd = GetCmd(word)
    print(cmd)
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    while True:
        s = p.stdout.readline()
        if not s: break
        print s,