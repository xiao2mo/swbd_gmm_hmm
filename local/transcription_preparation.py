#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Python version of this:
# awk '{
#        name=substr($1,1,6); gsub("^sw","sw0",name); side=substr($1,7,1);
#        stime=$2; etime=$3;
#        printf("%s-%s_%06.0f-%06.0f",
#               name, side, int(100*stime+0.5), int(100*etime+0.5));
#        for(i=4;i<=NF;i++) printf(" %s", $i); printf "\n"
# }' $dir/swb_ms98_transcriptions/*/*/*-trans.text > $dir/transcripts1.txt
from __future__ import division, absolute_import
import os
import sys


class queue(object):

    """ FIFO, fast, NO thread-safe queue
    """

    def __init__(self):
        super(queue, self).__init__()
        self._data = []
        self._idx = 0

    # ====== queue ====== #
    def put(self, value):
        self._data.append(value)

    # ====== dequeue ====== #
    def pop(self):
        if self._idx == len(self._data):
            raise ValueError('Queue is empty')
        self._idx += 1
        return self._data[self._idx - 1]

    def empty(self):
        if self._idx == len(self._data):
            return True
        return False


def get_all_files(path):
    ''' Recurrsively get all files in the given path '''
    file_list = []
    q = queue()
    # init queue
    if os.access(path, os.R_OK):
        for p in os.listdir(path):
            q.put(os.path.join(path, p))
    # process
    while not q.empty():
        p = q.pop()
        if os.path.isdir(p):
            if os.access(p, os.R_OK):
                for i in os.listdir(p):
                    q.put(os.path.join(p, i))
        else:
            # remove dump files of Mac
            if '.DS_STORE' in p or '._' == os.path.basename(p)[:2]:
                continue
            file_list.append(p)
    return file_list


# ===========================================================================
# Main
# ===========================================================================
if len(sys.argv) != 3:
    raise Exception('python transcription_preparation.py <input_dir> <output_file>')
input_dir = sys.argv[1]
output_file = open(sys.argv[-1], 'w')
# get all transcription files
files = [i for i in get_all_files(input_dir)
         if i[-len('-trans.text'):] == '-trans.text']

output = []
for f in files:
    f = open(f, 'r').readlines()
    for i in f: # each line
        i = i.split(' ')
        name = "sw0" + i[0][2:6]
        side = i[0][6]
        stime = i[1]
        etime = i[2]
        name = "%s-%s_%06.0f-%06.0f" % (name, side,
                                        int(100 * float(stime) + 0.5),
                                        int(100 * float(etime) + 0.5))
        trans = " ".join(["%s" % j for j in i[3:]])
        i = name + " " + trans
        output.append(i)
# must sort
output = sorted(output, reverse=False)
# write to file
for i in output:
    output_file.write(i)
output_file.flush()
output_file.close()
