#!/usr/bin/python

import pickle

file = open("etc/banner.p", "rb")
p = pickle.load(file)
print(p)
file.close()

results = [int(v) for lst in p for k, v in p.items()]