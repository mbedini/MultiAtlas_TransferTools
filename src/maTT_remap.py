__author__ = 'jfaskowitz'

'''
josh faskowitz
Indiana University
Computational Cognitive Neuroscience Lab

Copyright (c) 2018 Josh Faskowitz
See LICENSE file for license
'''

import numpy as np
import nibabel as nib
from sys import argv

def main():

    i_file = str(argv[1])
    o_file = str(argv[2])
    labels_file = str(argv[3])

    i_img = nib.load(i_file)
    i_data = i_img.get_fdata()

    # get labels from first column of LUT table
    labels = [x.split()[0] for x in open(labels_file).readlines()]  
    names = [x.split()[1] for x in open(labels_file).readlines()]  

    # init o_data
    o_data = np.zeros(i_data.shape,dtype=np.int32)

    # print remap to file
    f = open(str(o_file +'_remap.txt'),'w')
    
    # loop over the labs
    for x in range(0,len(labels)):
        print(x)
        w = np.where(i_data == int(labels[x]))
        o_data[w[0],w[1],w[2]] = (x + 1)
        f.write( "{}\t->\t{}\t== {} \n".format(  str(labels[x]), str(x + 1), str(names[x]) ) ) 

    f.close()

    # save output
    o_img = nib.Nifti1Image(o_data, i_img.affine)
    nib.save(o_img, o_file)

if __name__ == '__main__':
    main()
