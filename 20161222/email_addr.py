#coding=utf-8
#from : lisi <asde>
import re,fileinput

regx = re.compile('from : (.*) <.*?>$')

for line in fileinput.input():
    m = regx.match(line)
    print m
