#!/usr/bin/env python

import ftplib
import os

class FTPSync(object):
    def __init__(self,host,username,password,ftp_base_dir,local_base_dir,delete=False):
        self.host = host
        self.username = username
        self.password = password
        self.ftp_base_dir = ftp_base_dir
        self.local_base_dir = local_base_dir
        self.delete = delete

        self.conn = ftplib.FTP(host,username,password)
        self.conn.cwd(ftp_base_dir)
        try:
            os.makedirs(local_base_dir)
        except OSError:
            pass
        os.chdir(local_base_dir)

    def get_dirs_files(self):
        dir_res = []
        self.conn.dir('.',dir_res.append)
        files = [f.split(None,8)[-1] for f in dir_res if f.startswith('-')]
        dirs = [f.split(None,8)[-1] for f in dir_res if f.startswith('d')]
        return (files,dirs)

    def walk(self,next_dir):
        print 'Walking to',next_dir
        self.conn.cwd(next_dir)
        try:
            os.mkdir(next_dir)
        except OSError:
            pass
        os.chdir(next_dir)

        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()

        files,dirs = self.get_dirs_files()
        print 'FILES:',files
        print 'DIRS:',dirs
        for f in files:
            print next_dir,':',f
            outf = open(f,'wb')
            try:
                self.conn.retrbinary('RETR %s' % f,outf.write)
            finally:
                outf.close()
            if self.delete:
                print 'Deleting',f
                self.conn.delete(f)

        for d in dirs:
            os.chdir(local_curr_dir)
            self.conn.cwd(ftp_curr_dir)
            self.walk(d)

    def run(self):
        self.walk('.')

if __name__ == '__main__':
    from optparse import OptionParser
    