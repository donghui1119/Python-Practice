# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:15:20 2020

@author: DonghuiSong
"""


list8=['1.just do it','2.anything is possible','3.program changes the world','4.impossible is nothing']
list9=['4.addidas','2.lining','3.fishc','1.naike']
list10=[name+':' +slogan[2:] for slogan in list8 for name in list9 if slogan[0]==name[0]]