#!/usr/bin/env python

import dns.resolver
#ip = dns.resolver.query('baidu.com','A')
mail = dns.resolver.query('baidu.com','MX')

for i in mail:
    print i