#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
import argparse
import gzip
parser = argparse.ArgumentParser(description='渐渗系纯合位点')
parser.add_argument("input_vcf", type=str, help="need move local vcf file")
args = parser.parse_args()
 
input_vcf = args.input_vcf
fh = gzip.open(input_vcf,'rt')
for x in fh:
    if x.startswith('#'):
        print(x.strip())
        continue
    x_split = x.strip().split('\t')
    intro=x_split[9].split(':')[0]
    intro=intro.replace('|','/')
    ae=x_split[11].split(':')[0]
    ae=ae.replace('|','/')
    if intro==ae:
        print('\t'.join(x_split))
fh.close()
