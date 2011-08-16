#!/usr/bin/env python 
# encoding: utf-8
"""
StrGenerator.py
Created on 2011-06-16.
version 0.2
Everytime you run this script, it generates different %strfiles% for you.

"""

import os
import shutil
import random
import string
import codecs
from optparse import OptionParser

# 65535 = (82 + 3) * 771
# 3 cause chinese charactor needs 3 bytes in utf-8
strcount = 82 
runtimes = 771 
# how many 65535 strings file what you need
strfiles = 5 
# Chinese article file name
# If you would change or words, please follow the format
chinese_fname = 'article.txt'

gdirname    = 'RandomStrBank'
strdirname  = 'withoutCh' 
chdirname   = 'withCh' 

# Get Chinese words from article.txt
def getChineseChar(filename):
    """
    Choice 1 chinese words from chines article.

    """
    f = file(filename)
    content = f.read()
    de_content = content.decode('utf-8')
    f.close()
    return ''.join(random.sample(de_content.strip().split('\n'), 1))
        
# Combine Chinese words and generate files. 
def generateStrWithCh(num, chinese_words):
    char_set = string.digits + string.letters + string.punctuation 
    return ''.join(random.sample(char_set, num)) + chinese_words

# Generate string files. 
def generateStr(num):
    char_set = string.digits + string.letters + string.punctuation 
    return ''.join(random.sample(char_set, num))

  
if __name__ == '__main__':

    change_ptn_help = '''
                   usage:
                   -c --Generate length 65535 strings with Chinese word.
                   -s --Generate length 65535 strings without Chinese word.
                   '''
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage)

    parser.add_option('-c',
                   '--chinese',
                   action='store_true',
                   dest='chinese',
                   help='generate length 65535 strings with Chinese word.')
    parser.add_option('-s',
                   '--nochinese',
                   action='store_true',
                   dest='nochinese',
                   help='generate length 65535 strings without Chinese word.')
    (options, args) = parser.parse_args()

    if not os.path.isdir(gdirname):
            os.mkdir(gdirname)
    if options.chinese:
        # Check the previos generation exist or not.
        if not os.path.isdir(gdirname+'/'+chdirname):
            os.mkdir(gdirname+'/'+chdirname)
        else:
            shutil.rmtree(gdirname+'/'+chdirname)
            os.mkdir(gdirname+'/'+chdirname)
        
        # Start to generate files
        for i in range(strfiles):
            strfile = codecs.open(gdirname+'/'+chdirname+'/%s.txt' % i, 'w', 'utf-8')
            for j in range(runtimes):
                strfile.write(generateStrWithCh(strcount, getChineseChar(chinese_fname)))
            strfile.close()

    elif options.nochinese:
        # Check the previos generation exist or not. 
        if not os.path.isdir(gdirname+'/'+strdirname):
            os.mkdir(gdirname+'/'+strdirname)
        else:
            shutil.rmtree(gdirname+'/'+strdirname)
            os.mkdir(gdirname+'/'+strdirname)
        
        # Start to generate files
        for i in range(strfiles):
            strfile = codecs.open(gdirname+'/'+strdirname+'/%s.txt' % i, 'w', 'utf-8')
            for j in range(runtimes):
                strfile.write(generateStr(strcount+3))
            strfile.close()

    else:
       print 'Error! Please refer help(-h).'





