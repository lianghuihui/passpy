# -*- coding:utf-8 -*-

import hashlib, sys, getopt


def md5_passwd(passwd, sitename):
    m = hashlib.md5()
    m.update(passwd)
    m.update(sitename)
    print sitename + ' <===> ' + m.hexdigest()[:12]

if __name__ == '__main__':

    opts, args = getopt.getopt(sys.argv[1:], "hp:s:")

    for op, value in opts:

        if op == "-p":
            passwd = value

        if op == "-s":
            site_name = value

        if op == "-h":
            print "usage: python passpy.py -p yourpasswd -s yoursitename"
            sys.exit()

    md5_passwd(passwd, site_name)
