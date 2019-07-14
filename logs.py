#!/bin/env python
#coding=utf-8

#name:log_cut_5days.py
#editor:uncle k

import os,time,json
from apscheduler.schedulers.blocking import BlockingScheduler
class logcut():
    def trans_str_to_time(str=None,format='%Y-%m-%d'):	#进行时间字符串
        if str:
            tuple1 = time.strptime(str,format)	#根据指定的格式把一个时间字符串解析为时间元组
            result = time.mktime(tuple1)		#转换成时间戳
            return  int(result)

    def delete(self,logpath):			#截取日志名称中时间的字符串，将符合条件的删除

        for cur_dir,dirs,files in os.walk(logpath):
                print(cur_dir,dirs,files)                   #test
                for file in files:
                        #print(dirs1,files1)
                        str = file.split('-')[-1].split('.')[0]			#截取出字符串
                        print("字符串",str)                #test
                        timedata = logcut.trans_str_to_time(str,'%Y%m%d')
                        print("时间:",timedata)               #test
                        n = 5
                        daytime = int(time.time()) - n*24*60*60		#n天的时间戳
                        print("时间戳：",daytime)           #test
                        if int(timedata) < daytime:
                            print("条件成立")   					#条件判断，删除5天前的日志
                            abs_path = os.path.join(cur_dir,file)
                            print(abs_path)                     #test
                            os.remove(abs_path)
                            for aa,bb,cc in os.walk(logpath):
                                print(aa,bb,cc)                 #tets
                        else:
                            print("条件不成立")                  #test

    def choose(self):
        #存储日志路径的文件的读取
        for cur_dir2,dirs2,files2 in os.walk("/",topdown=True):
            print(cur_dir2, dirs2, files2)      #test
            for sfile in files2:
                namel = "logsname.txt"
                if sfile == namel:
                    txtpath = os.path.join(cur_dir2,sfile)
                    yy = open(txtpath, "r+")
                    logsname = yy.read()  # 文件内容是字典类型
                    print(logsname)             #test
                    loggg = logsname.split(",")
                    for value in loggg:
                        print("路径：" + value)        #test
                        logpath = value
                        self.delete(logpath)
                    break

def job():
    foo = logcut()
    foo.choose()

if __name__ == '__main__':

    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=12, minute=00)
    scheduler.start()

    #job()      #test