import requests, re
import shutil

from bs4 import BeautifulSoup

class FindDuplicate:
    def str_search_in_file(str, fname):
        with open(fname, 'r') as file_obj:
            while 1:
                line = file_obj.readline()
                if line:
                    line = line.strip()
                    if (line.find (str,0) >= 0):
                        print ('found = ',line)
                else:
                    break
 
    def find_same_str_in_2file(file1,file2):
        with open(file1, 'r') as file_obj:
            list1 = file_obj.readlines()
            for line in list1:
                strlist = line.split(' ')
                i=0
                #print 'len=', len(strlist)
                while (i <len(strlist)):
                    #print 'find for',strlist[i].strip() #strlist may have slash \n
                    str_search_in_file(strlist[i].strip(), file2)
                    i += 1
                    
    


#str_search_in_file('lin', 'test.txt')
#find_same_str_in_2file('test.txt', 'map.txt')