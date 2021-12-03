#!/bin/bash
usage ()
{
  echo 'Usage : Script -lm <language model>'
  exit
}
echo $#
if [ "$#" -ne 2 ]
then
  usage
fi
pred_file="results/task1/pred_35man$2"
ref_file="results/task1/ref_35man$2"

wer -i ${pred_file} ${ref_file}
