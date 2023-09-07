#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import argparse
parser = argparse.ArgumentParser(description='两亲本纯和渐渗系杂合位点')
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
    intro=x_split[10].split(':')[0]
    intro=intro.replace('|','/')
    ak=x_split[9].split(':')[0]
    ak=ak.replace('|','/')
    ae=x_split[11].split(':')[0]
    ae=ae.replace('|','/')
    if (ak=="0/0" or ak=="1/1")  and  (ae=="1/1" or ae=="0/0") and ak!=ae:
        print('\t'.join(x_split))
fh.close()
