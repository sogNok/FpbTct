# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:03:09 2021

@author: 이충섭
"""

# Chapter 13 organization 2

with open('binfile.bin', 'bw') as f:
    f.write(bytes(range(0, 256)))
    
with open('binfile.bin', 'br+') as f:
    while True:
        pos = int(input('Offset: '))
        f.seek(pos)
        c = f.read(1)
        print(c[0])
        
        retry = input('Change offset[Y/N]: ')
        if retry in {'Y', 'y'}:
            value = int(input('Number between 0~255: '))
            if 0 <= value <= 255:
                f.seek(pos)
                f.write(bytes([value]))
            else:
                print('Invalid value.')
                
        retry = input('One more try[Y/N]: ')
        if retry in {'N', 'n'}:
            break
            