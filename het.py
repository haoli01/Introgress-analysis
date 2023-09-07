#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import argparse
parser = argparse.ArgumentParser(description='渐渗系杂合位点')
parser.add_argument("input_vcf", type=str, help="need move local vcf file")
args = parser.parse_args()

input_vcf = args.input_vcf

fh = open(input_vcf)
for x in fh:
    # 注释行直接输出
    if x.startswith('#'):
        print(x.strip())
        continue
    x_split = x.strip().split('\t')
    intro=x_split[9].split(':')[0]
    intro=intro.replace('|','/')
    if intro=="0/1" :
        print('\t'.join(x_split))
fh.close()
