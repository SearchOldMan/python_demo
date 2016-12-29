import pickle

some_dict = {'name':'zhangsan','age':12,'sex':'girl'}

pickle_file_name = open('some_dict.pkl','w')
pickle.dump(some_dict,pickle_file_name)
pickle_file_name.close()


read_pickle_file = open('some_dict.pkl','r')
new_dict = pickle.load(read_pickle_file)

print new_dict