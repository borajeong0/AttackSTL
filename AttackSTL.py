from dataload import *
from get_bb import *
from get_log import *

from torch.utils.data import DataLoader, Dataset
from easydict import EasyDict as edict
import torch
import torch.nn.functional as F
import random


def real(n, target, device, dataset):
    filename = '{}_real_{}'.format(target, n)
    
    bb = blackbox(target=target).to(device)
    th = threshold(target=target)
    
    txt = 'Target: {},   Threshold: {}\n'.format(target, th)
    print(txt)
    logging(txt, filename)


    successes=0
    query=0
    for i in range(500):
        r = random.randint(1, 400000)
        x1 = dataset.__getitem__(r)[0].unsqueeze(0).to(device)
            
        k1 = torch.randint(0, high=2, size=(1, 100), device=device)
        k1_norm = F.normalize(k1.to(torch.float))     
        target_f = bb(x1, k1_norm)

        s=1
        z=0
        while s > th and z < 5:
            z+=1
            x2 = dataset.__getitem__(r + z*1000)[0].unsqueeze(0).to(device)
            k2 = torch.rand(1,100, device=device)
            k2_norm = F.normalize(k2)     
            random_f = bb(x2, k2_norm)

            s = score(random_f, target_f)
            key_s = score(k1_norm, k2_norm)
            txt = '[n={}, i={}, z={}]\nStart...   score: {:.4f},   key score: {:.4f}'.format(n, i+1, z, s, key_s)
            print(txt)
            logging(txt, filename)

            if s <= th:
                successes += 1    
                query+=1
                txt = 'Success!   score: {:.4f},   key score: {:.4f}   [Query: 1, Mean of Query: {}, Success rate: {}]\n'.format(
                        s, key_s, float(query)/(i+1), (float(successes)*100)/(i+1))
                print(txt)
                logging(txt, filename)
                continue

            for q in range(999):
                noise = torch.randn(1, 100, device=device) * 0.01*n
                k2_new = k2+noise
                k2_new_norm = F.normalize(k2_new) 
                random_f = bb(x2, k2_new_norm)
                s_new = score(random_f, target_f)

                if s_new <= s:
                    k2 = k2_new
                    s = s_new  

                if s <= th:
                    successes += 1    
                    query+=(q+2)
                    key_s = score(k2_norm, k2_new_norm)
                    txt = 'Success!   score: {:.4f},   key score: {:.4f}   [Query: {}, Mean of Query: {}, Success rate: {}]\n'.format(
                        s, key_s, q+2, float(query)/(i+1), (float(successes)*100)/(i+1))
                    print(txt)
                    logging(txt, filename)
                    break

            if s > th:
                query+=999
                txt = 'Failed...  score: {:.4f},   [Success rate: {}]\n'.format(s, (float(successes)*100)/(i+1))
                print(txt)
                logging(txt, filename)
                
def binary(n, target, device, dataset):    
    filename = '{}_binary{}'.format(target, n)
    
    bb = blackbox(target=target).to(device)
    th = threshold(target=target)
    
    txt = 'Target: {},   Threshold: {}\n'.format(target, th)
    print(txt)
    logging(txt, filename)


    successes=0
    query=0
    for i in range(500):
        r = random.randint(1, 400000)
        x1 = dataset.__getitem__(r)[0].unsqueeze(0).to(device)
            
        k1 = torch.randint(0, high=2, size=(1, 100), device=device)
        k1_norm = F.normalize(k1.to(torch.float))     
        target_f = bb(x1, k1_norm)

        s=1
        z=0
        while s > th and z < 5:
            z+=1
            x2 = dataset.__getitem__(r + z*1000)[0].unsqueeze(0).to(device)
            k2 = torch.randint(0, high=2, size=(1, 100), device=device)
            k2_norm = F.normalize(k2.to(torch.float))     
            random_f = bb(x2, k2_norm)

            s = score(random_f, target_f)
            key_s = score(k1_norm, k2_norm)
            txt = '[n={}, i={}, z={}]\nStart...   score: {:.4f},   key score: {:.4f}'.format(n, i+1, z, s, key_s)
            print(txt)
            logging(txt, filename)

            if s <= th:
                successes += 1    
                query+=1
                txt = 'Success!   score: {:.4f},   key score: {:.4f}   [Query: 1, Mean of Query: {}, Success rate: {}]\n'.format(
                        s, key_s, float(query)/(i+1), (float(successes)*100)/(i+1))
                print(txt)
                logging(txt, filename)
                continue

            for q in range(999):
                k2_perm = ((torch.randperm(100, device=device)-99+n)>0).to(torch.long)
                k2_new = (k2^k2_perm)
                k2_new_norm = F.normalize(k2_new.to(torch.float))  
                random_f = bb(x2, k2_new_norm)
                s_new = score(random_f, target_f)

                if s_new <= s:
                    k2 = k2_new
                    s = s_new  

                if s <= th:
                    successes += 1    
                    query+=(q+2)
                    key_s = score(k2_norm, k2_new_norm)
                    txt = 'Success!   score: {:.4f},   key score: {:.4f}   [Query: {}, Mean of Query: {}, Success rate: {}]\n'.format(
                        s, key_s, q+2, float(query)/(i+1), (float(successes)*100)/(i+1))
                    print(txt)
                    logging(txt, filename)
                    break

            if s > th:
                query+=999
                txt = 'Failed...  score: {:.4f},   [Success rate: {}]\n'.format(s, (float(successes)*100)/(i+1))
                print(txt)
                logging(txt, filename)
                

                