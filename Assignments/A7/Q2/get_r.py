import numpy as np

def get_r(K,L,alpha,Z,delta):
	ratio=np.divide(L,K)
	r=(alpha*Z*((ratio)**(1-alpha)))- delta
	return r