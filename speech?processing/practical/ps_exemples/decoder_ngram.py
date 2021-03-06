#!/usr/bin/python

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

print ("Pronunciation for word 'two' is ", decoder.lookup_word("two"))
print ("Pronunciation for word 'one' is ", decoder.lookup_word("one"))

decoder.start_utt()
stream = open('ps_data/test-digits/SNR05dB_man_seq1digit_001.raw', 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()

hypothesis = decoder.hyp()
logmath = decoder.get_logmath()
print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))

print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

# Access N best decodings.
print ('Best 10 hypothesis: ')
for best, i in zip(decoder.nbest(), range(10)):
    print (best.hypstr, best.score)

