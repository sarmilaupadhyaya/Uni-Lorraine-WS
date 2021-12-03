#!/bin/bash

usage ()
{
  echo 'Usage : Script -n <noise ratio> -lm <language model>'
  exit
}
echo $#
if [ "$#" -ne 4 ]
then
  usage
fi

pred_file="results/task4/pred_$2man$4"
ref_file="results/task4/ref_$2man$4"

wer -i ${pred_file} ${ref_file}
