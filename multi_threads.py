# Script Name    : multi_threads.py
# Author         : Riley Young
# Creat Time     : 25 November 2016
# Release Version: 1.0
# Description    : multiple threads, executing linux commands using python ssh
#
#-*- coding: utf-8 -*-  
#!/usr/bin/python   
import paramiko  
import threading  
import os

def ssh2(ip,username,passwd,cmd):  
    try:  
        ssh = paramiko.SSHClient()  
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(ip,22,username,passwd,timeout=5)  
        for m in cmd:  
            stdin, stdout, stderr = ssh.exec_command(m)    
            out = stdout.readlines()  
            for o in out:  
                print o,  
        print '%s\tOK\n'%(ip)  
        ssh.close()  
    except :  
        print '%s\tError\n'%(ip) 

#def enter():

if __name__=='__main__':  
    cmd = ['cal','echo hello!','os.chdir(r'/root/test') ','ls']  
    username = "root" 
    passwd = "password123"  
    threads = []
    print "Begin......" 
    for i in range(1,254):  
        ip = '192.168.142.'+str(i)  
        a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))   
        a.start() 
