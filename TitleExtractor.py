__author__ = 'shengyinwu'

from bs4 import BeautifulSoup
import urllib2
import node

url_string = "http://sports.163.com/13/0912/08/98IDS0Q000051C89.html"
tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'b', 'p']

def extract_title(url):
    page = urllib2.urlopen(url_string)
    if not page:
     print "Error down page" + url_string
    else:
        soup = BeautifulSoup(page, 'lxml')

        # get head title, this title is noisy
        head_title = soup.find('title').string

        # append h1 ~ h6 p a
        node_list = []
        for tag in tags:
            all_content = soup.find_all(tag)
            for content in all_content:
                if type(content) == None:
                    continue
                tmp = content.string
                if tmp == None:
                    continue
                else:
                    nod = node.node(tmp.rstrip('\n').lstrip('\n').rstrip(' ').lstrip(' '))
                    node_list.append(nod)

        for nod in node_list:
            nod.calculate_LCS(head_title)
            nod.calculate_pureness(head_title)
            nod.calculate_prefix_ratio()
        node_list.sort(key=lambda x: x.lcs_length, reverse=True)

        nod = node_list[0]
        if float(nod.pureness) > 0.5 and float(nod.prefix_ratio) == 0:
            return nod.lcs
        else:
            return head_title

if __name__ == "__main__":
    url_string = "http://sports.163.com/13/0912/08/98IDS0Q000051C89.html"
    print "Extracted title is: " +  extract_title(url_string)
    url_string = "http://www.5eplay.com/group/cs/topic/5642"
    print "Extracted title is: " +  extract_title(url_string)
    url_string = "http://business.sohu.com/20130912/n386445665.shtml"
    print "Extracted title is: " +  extract_title(url_string)
    url_string = "http://jandan.net/2013/09/12/3nes.html"
    print "Extracted title is: " +  extract_title(url_string)
