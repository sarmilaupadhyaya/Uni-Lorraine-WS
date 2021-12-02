#!/usr/bin/python
import os
from os import environ, path


from pocketsphinx import *
from sphinxbase import *


# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm',  'ps_data/model/en-us')
config.set_string('-lm',   'ps_data/lm/en-us.lm.bin')
config.set_string('-dict', 'ps_data/lex/digits.dict')

# Decode streaming data.
decoder = Decoder(config)



def inference(path_raw):
    """
    """
    decoder.start_utt()
    stream = open(path_raw, 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
          decoder.process_raw(buf, False, False)
        else:
            break
    decoder.end_utt()

    hypothesis = decoder.hyp()
    logmath = decoder.get_logmath()

    if hypothesis is not None:
        N_best = []
        for best, i in zip(decoder.nbest(), range(1)):
            print(best.hypstr)
            return best.hypstr


def inference_set(files_directory, seq=None, extension=".raw"):
    """

    """
    filenames_decoded = dict()
    for root, dirs, files in os.walk(files_directory):
        for f in files:
            if f.endswith(".raw"):
                s = os.path.join(root, f)
                result = inference(s)
                filenames_decoded[f] = result
    return filenames_decoded


#filenames_decoded = inference_set("td_corpus_digits/SNR35dB/boy/seq1digit_200_files")

#total = 0
#correct = 0
# get all the ref for the file
#filenames_reference = dict()
#for root, dirs, files in os.walk("td_corpus_digits/SNR35dB/boy/seq1digit_200_files"):
#    for f in files:
#        if f.endswith(".ref"):
#            ref = open(os.path.join(root, f), "r").read().strip()
#            filename = ".".join(f.split(".")[:-1]) + ".raw"
#            result = filenames_decoded[filename]

#            if ref == result:
#                correct += 1
#            total += 1

#import pdb
#pdb.set_trace()



