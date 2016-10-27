__author__ = 'raviteja_ganireddy'

import glob
import os
import sys
base_dir="C:\Users\hema_ganireddy\Documents\Visual Studio 2012\Projects\\1000_files"
class posting_list():
    def __init__(self):
        self.base_dir="C:\Users\hema_ganireddy\Documents\Visual Studio 2012\Projects\\1000_files"
        self.list={}


def extract_words(fp1,list1):
    str=[]
    i=0
    fp= os.path.join(list1.base_dir,fp1)
    fp=open(fp,"rb")
    for lines in fp:
        for char in lines:
            if('a'<=char<='z' or 'A'<=char <='Z' or '0'<=char<='9'):
                str.append(char)
            else:
                str="".join(str)
                if(str is not ''):
                    try:
                        list1.list[str][fp1]+=1
                    except Exception :
                        try:
                            k=list1.list[str]
                        except Exception:
                            list1.list[str]={}
                        list1.list[str][fp1]=1
                str=[]


def index_files():
    list1=posting_list()
    files=glob.glob1(list1.base_dir,"*.txt")
    for f in files:
        extract_words(f,list1)
    return list1

    """wf=[w.strip() for w in open(fp)]
        for line in wf:
            list1.parse_line(line)
        break"""

def search(keyword):
    try:
        return list1.list[keyword]
    except Exception:
        return False

def intersect(l1,l2):
    l3=[]
    for x in l1:
        if(x in l2):
            l3.append(x)
    return l3

def union(l1,l2):
    l3=[]
    for x in l1:
        l3.append(x)
    for x in l2:
        if(x not in l3):
            l3.append(x)
    return l3

def href(l):
    str=''
    for x in l:
        str1=base_dir+"\\"+x
        str1="<a href="+'"'+str1+'"'+">"+x+"</a> <br>"
        str=str+str1
    return str

"""if __name__=="__main__":
    index_files()"""

list1=index_files()
