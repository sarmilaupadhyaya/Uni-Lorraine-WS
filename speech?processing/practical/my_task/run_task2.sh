#!/bin/sh

source newenv/bin/activate
python3 my_task/generation.py td_corpus_digits/ man,woman,boy,girl 1digit,3digits,5digits 35 results/task2/
#calculate wer and confidence interval


