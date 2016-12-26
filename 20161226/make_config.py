from ConfigParser import ConfigParser

config_file = 'configtest.txt'
config = ConfigParser()
config.read(config_file)

print config.get('message','greeting')
radius = input(config.get('message','question'))
print config.get('message','result')+' '
print config.getfloat('number','pi')*radius**2