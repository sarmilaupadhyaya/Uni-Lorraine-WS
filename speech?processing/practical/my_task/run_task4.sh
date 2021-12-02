#!/bin/sh

source newenv/bin/activate
python3 my_task/generation.py td_corpus_digits/ man 1digit,3digits,5digits 35,25,15,05 results/task4/
#calculate wer and confidence interval


