#coding=utf-8
import sys,shelve

def store_person(db):
    pid = raw_input('请输入ID:')
    person = {}
    person['name'] = raw_input('enter_name:')
    person['age'] = raw_input('enter_age:')
    db[pid] = person
def look_person(db):
    pid = raw_input('想查看的id:')
    detail = raw_input('你想要查看什么(name or age)?')
    detail = detail.strip().lower()
    print detail.capitalize() + ':',db[pid][detail]
def help():
    print '可以输入以下命令操作：'
    print 'store: set person message'
    print 'look: look person message'
    print '?:quite!'
def commond():
    cmd = raw_input('请输入命令：')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('E:\\database.sql')
    try:
        while 1:
            cmd = commond()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'look':
                look_person(database)
            elif cmd == 'help':
                help()
            else:
                break
    finally:
        database.close()
if __name__ == '__main__':
    main()