from facenet_pytorch import InceptionResnetV1
from SecureTL.models import SecureModel, SecureFaceNetwork
from SecureTL.eval import normalised_distance

import os
import torch
from torch import nn
import numpy as nP
import pickle as pk


class blackbox(nn.Module):
    def __init__(self, target='STL_C'):
        super(blackbox, self).__init__()
        pretrained = InceptionResnetV1(pretrained='vggface2')
        network = SecureFaceNetwork(pretrained)
        model = SecureModel(network)
        model.load_state_dict(torch.load('{}.pth'.format(target), map_location='cpu'))
        model.eval()
        self.model = model
        
    def forward(self, x, k):    
        emb = (self.model).get_embedding(x, k)
        return emb
    

def threshold(target='STL_C'):
    with open('{}_results.pk'.format(target), 'rb') as f:
        data = pk.load(f)
        threshold = data[0]['eer'][0]
    return threshold


def score(emb1, emb2):
    emb1 = emb1.detach().cpu().numpy()
    emb2 = emb2.detach().cpu().numpy()
    s = normalised_distance(emb1, emb2)
    return float(s)