#!/usr/bin/python

from os import environ, path
from sys import stdout

from pocketsphinx import *
from sphinxbase import *

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm',  'ps_data/model/en-us')
config.set_string('-lm',   'ps_data/lm/turtle.lm.bin')
config.set_string('-dict', 'ps_data/lex/digits.dict')
decoder = Decoder(config)
digit_jsf = "ps_data/jsgf/digits.gram"

def inference(path_raw, rulename="digitloop"):
    """
    parameters:
    rule: either digitloop or 1digit or 2digit or 3digit
    """

     
    # Switch to JSGF grammar
    jsgf = Jsgf(digit_jsf)
    rule = jsgf.get_rule('digits.'+ rulename)
    fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
    fsg.writefile(rulename+'.fsg')

    decoder.set_fsg(rulename, fsg)
    decoder.set_search(rulename)
    decoder.start_utt()
    stream = open(path_raw, 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
    decoder.end_utt()
    try:
        print ('Decoding with "digit" grammar:', decoder.hyp().hypstr)
    except:
        return ""
    return decoder.hyp().hypstr

