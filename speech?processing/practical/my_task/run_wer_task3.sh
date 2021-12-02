#!/bin/bash
usage ()
{
  echo 'Usage : Script -m <age group> -lm <language model>'
  exit
}
echo $#
if [ "$#" -ne 4 ]
then
  usage
fi
pred_file="../results/task3/pred_35$2$4"
ref_file="../results/task3/ref_35$2$4"

wer -i ${pred_file} ${ref_file}
