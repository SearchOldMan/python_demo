import dns.resolver

hosts = ['baidu.com','yahoo.com','google.com','microsoft.com','qq.com']

def query(host_list=hosts):
    a_list = []
    for i in host_list:
        ip = dns.resolver.query(i,'A')
        for j in ip:
            a_list.append(str(j))

    return a_list

if __name__ == '__main__':
    print query()

