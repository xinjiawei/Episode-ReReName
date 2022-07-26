#conding=utf8  
import os 
import re
from loguru import logger

downloadpath = "/volume4/download/2222-incomplete/dl_tmp/bangumi"
warepath = "/volume1/homes/xinjiawei/bangumi/new_bangumi"
renamescript = "/volume4/download/2222-incomplete/dl_tmp/EpisodeReName.py"
renamedelay = 1
badstr = '@|DAV'

logger.debug(f'下载目录: {downloadpath}')
logger.debug(f'本地或挂载的仓库目录: {warepath}')
logger.debug(f'主脚本路径: {renamescript}')
logger.debug(f'重命名延时,防止拥塞,单位为秒: {renamedelay}')
logger.debug(f'跳过的目录关键词,使用|分割: {badstr}')
'''
默认延迟一秒
群晖Download Station 的原因, 排除掉@和DAV的文件夹
'''

g = os.walk(downloadpath)
for path,dir_list,file_list in g:  
    for dir_name in dir_list:
        '''
        logger.debug(f'{os.path.join(path, dir_name)}')
        sudo python3 /volume4/download/2222-incomplete/dl_tmp/rename.py "./杜鹃的婚约/Season 01"
        '''
        matchObj1 = re.match( r'(.*)season(.*?) .*', os.path.join(path, dir_name), re.M|re.I)
        matchObj2 = re.search( badstr, os.path.join(path, dir_name))
        if matchObj2:
            logger.debug(f'get badstr: {badstr} , stop!')
        else:
            if matchObj1:
                logger.debug(f'match: {matchObj1.group()}')
                targetpath = matchObj1.group()
                command05 = 'python3 ' + renamescript + ' --path' + ' \"' + targetpath + "\"" + ' --delay=' + str(renamedelay)
                logger.debug(f'input command: {command05}')
                result01 = os.system(command05)
                logger.debug(f'result: {str(result01)}')
                '''
                '''
                print ("--------------------------over--------------------------")
            else:
                print ("--------------No match keyword 'season' !!------------")
                
print ("--------------------------rename complete--------------------------")
command06 = "cp -r -n " + downloadpath + "/* " + warepath
print (command06)
os.system(command06)
print ("---------------------------copy complete--------------------------")
'''
os.system("chown -R nobody:users " + warepath + "/*")
os.system("chmod -R 777 " + warepath + "/*")
'''
