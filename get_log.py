import time
from datetime import datetime

def logging(txt, filename):
    date = datetime.now().strftime('%Y%m%d %H:%M:%S')
    f = open('./log/log_{0}.txt'.format(filename), 'a')
    f.write("[{}] ".format(date) + txt + "\n")
    f.close()    
