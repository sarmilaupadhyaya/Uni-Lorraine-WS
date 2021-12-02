#!/bin/sh

source newenv/bin/activate
python3 my_task/generation.py td_corpus_digits/ man ngram,1digit,3digits,5digits,digitloop 35 results/task1/
#calculate wer and confidence interval


