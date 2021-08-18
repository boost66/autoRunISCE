#!/usr/bin/env python3
#适用于isce2.3版本生成的run_files文件的自动运行,2.5需要自行修改下编号
import os
import time
start_time = time.time()
print('读取文件')
fileList=os.listdir('./run_files')
for i in range(0,len(fileList)):
	for file in fileList:
          
		if i<9:   
			if file[:6] =='run_{}_'.format(i+1):
				print('*******处理文件:{}********'.format(file))
				run_file=open('./run_files/{}'.format(file))
				for line in run_file:
					print('**运行命令:{}**'.format(line))
					os.system(line)
		else:
			if file[:6] =='run_{}'.format(i+1):
				print('*******处理文件:{}********'.format(file))
				run_file=open('./run_files/{}'.format(file))
				for line in run_file:
					print('**运行命令:{}**'.format(line))
					os.system(line)
m, s = divmod(time.time()-start_time, 60)
print('使用时间: {:02.0f} mins {:02.1f} secs\n'.format(m, s))
print('*********完成处理********')
