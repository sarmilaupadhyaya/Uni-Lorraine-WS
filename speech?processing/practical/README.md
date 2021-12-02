Speech modeling and automatic speech recognition
Lexicons and language models for ASR using pocketsphinx experiments –


# Outline

1. [Directory Structure](#directory-structure)
2. [Introduction](#introduction)
3. [Installation](#installation)
4. [Dataset](#dataset)
5. [Execution](#execution)
5. [Results](#results)
6. [Licence](#licence)


## Directory structure

```
.
├── my_task   ## the main program I added for 4 tasks
│   ├── decoder_jsgf.py   #modified asr model with jsgf grammar
│   ├── decoder_ngram.py   #modified asr model with ngram
│   ├── generation.py       #main file that takes parameters and run different task. this is called by bash files 
│   ├── run_task1.sh    # bash file to run task number 1
│   ├── run_task2.sh
│   ├── run_task3.sh
│   ├── run_task4.sh
│   ├── run_wer_task1.sh   #bash file that after getting prediction calculate wer for task 1
│   ├── run_wer_task2.sh
│   ├── run_wer_task3.sh
│   ├── run_wer_task4.sh
│   ├── task1_wer.py    #simple python script to plot wer and its confidence interval
│   ├── task2_wer.py
│   ├── task3_wer.py
│   └── task4_wer.py
├── ps_data  #provided in the lab. I only added lexical dictionary called digits.dict
│   ├── exemple
│   │   └── goforward.raw
│   ├── jsgf
│   │   ├── digits.gram
│   │   └── goforward.gram
│   ├── lex
│   │   ├── cmudict-en-us.dict
│   │   ├── digits.dict  # added by me
│   │   ├── script_to_get_lex.py
│   │   └── turtle.dic
│   ├── lm
│   │   ├── en-us.lm.bin
│   │   └── turtle.lm.bin
│   ├── model
│   │   └── en-us
│   │       ├── feat.params
│   │       ├── mdef
│   │       ├── means
│   │       ├── noisedict
│   │       ├── README
│   │       ├── sendump
│   │       ├── transition_matrices
│   │       └── variances
│   └── test-digits
│       ├── SNR05dB_man_seq1digit_001.raw
│       ├── SNR05dB_man_seq1digit_001.ref
│       ├── SNR05dB_man_seq1digit_002.raw
│       └── SNR05dB_man_seq1digit_002.ref
├── ps_exemples
│   ├── 1
│   ├── decoder_jsgf.py
│   ├── decoder_ngram.py
│   ├── decoder_utt_jsgf.py
│   └── decoder_utt_ngram.py
├── README.md
├── results   # results for prediction and plot of wer and confidence interval
│   ├── figures
│   ├── task1
│   │   ├── pred_35man1digit
│   │   ├── pred_35man3digits
│   │   ├── pred_35man5digits
│   │   ├── pred_35mandigitloop
│   │   ├── pred_35manngram
│   │   ├── ref_35man1digit
│   │   ├── ref_35man3digits
│   │   ├── ref_35man5digits
│   │   ├── ref_35mandigitloop
│   │   └── ref_35manngram
│   ├── task2
│   │   ├── pred_35boy1digit
│   │   ├── pred_35boy3digits
│   │   ├── pred_35boy5digits
│   │   ├── pred_35girl1digit
│   │   ├── pred_35girl3digits
│   │   ├── pred_35girl5digits
│   │   ├── pred_35man1digit
│   │   ├── pred_35man3digits
│   │   ├── pred_35man5digits
│   │   ├── pred_35woman1digit
│   │   ├── pred_35woman3digits
│   │   ├── pred_35woman5digits
│   │   ├── ref_35boy1digit
│   │   ├── ref_35boy3digits
│   │   ├── ref_35boy5digits
│   │   ├── ref_35girl1digit
│   │   ├── ref_35girl3digits
│   │   ├── ref_35girl5digits
│   │   ├── ref_35man1digit
│   │   ├── ref_35man3digits
│   │   ├── ref_35man5digits
│   │   ├── ref_35woman1digit
│   │   ├── ref_35woman3digits
│   │   └── ref_35woman5digits
│   ├── task3
│   │   ├── pred_35man1digit
│   │   ├── pred_35man3digits
│   │   ├── pred_35man5digits
│   │   ├── pred_35mandigitloop
│   │   ├── pred_35manngram
│   │   ├── pred_35woman1digit
│   │   ├── pred_35woman3digits
│   │   ├── pred_35woman5digits
│   │   ├── pred_35womandigitloop
│   │   ├── pred_35womanngram
│   │   ├── ref_35man1digit
│   │   ├── ref_35man3digits
│   │   ├── ref_35man5digits
│   │   ├── ref_35mandigitloop
│   │   ├── ref_35manngram
│   │   ├── ref_35woman1digit
│   │   ├── ref_35woman3digits
│   │   ├── ref_35woman5digits
│   │   ├── ref_35womandigitloop
│   │   └── ref_35womanngram
│   └── task4
│       ├── pred_05man1digit
│       ├── pred_05man3digits
│       ├── pred_05man5digits
│       ├── pred_15man1digit
│       ├── pred_15man3digits
│       ├── pred_15man5digits
│       ├── pred_25man1digit
│       ├── pred_25man3digits
│       ├── pred_25man5digits
│       ├── pred_35man1digit
│       ├── pred_35man3digits
│       ├── pred_35man5digits
│       ├── ref_05man1digit
│       ├── ref_05man3digits
│       ├── ref_05man5digits
│       ├── ref_15man1digit
│       ├── ref_15man3digits
│       ├── ref_15man5digits
│       ├── ref_25man1digit
│       ├── ref_25man3digits
│       ├── ref_25man5digits
│       ├── ref_35man1digit
│       ├── ref_35man3digits
│       └── ref_35man5digits
├── TD-Sphinx-2019-Additional_Information.pdf
├── TD-Sphinx-2019-SetUp.pdf
├── toto.hyp
├── toto.ref
└── tree.txt

16 directories, 125 files
```
    


## Introduction

This task was carried out under supervision of Paul Margon with the main objective of implementing the provided Encoder and Decoder models for automatic speech recognition. The task consists of implementation of a model for a digits corpus and
analysing the performance of the ASR system with respect to different language models, length of digits, speaker groups and
signal-to-noise ratio (SNR). Furthermore, in this report fluctuations in results between speakers and noise level are analysed.

## Installation

view the requirements.txt file and install the packages.

<!-- ### Requirements -->
Pre-requisites:

    python==3.7.5

On Windows you will also need [Git for Windows](https://gitforwindows.org/).

---
_Optional_: to install a specific version of Python:

#### Ubuntu:

    pyenv install 3.7.5

(To install ```pyenv```, follow [this tutorial](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation), and then [this one](https://www.laac.dev/blog/setting-up-modern-python-development-environment-ubuntu-20/))
<!--     sudo apt-install python3.7 -->


#### Mac:

    brew install python@3.7


#### Windows:
Download Python 3.7.5 for Windows [here](https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe), run it and follow the instructions.
    
---
### 1. Clone the repository

    git clone [link]

_Optional_: use the package manager [pip](https://pip.pypa.io/en/stable/) to install a vitual environment.

    bash
    pip install virtualenv
    
    
    
#### 2. Navigate to the folder with the cloned git repository

#### 3. Create Virtual Environment

    virtualenv <name of env> --python /usr/bin/python[version] or <path to your python if its not the mentioned one>
    
Conda:

    conda create --name <name of your env> python=3.7

#### 4. Activate Virtual Environment

    source name_of_env/bin/activate
On Windows:

    name_of_env\Scripts\activate
Conda:

    conda activate <name of your env>

(To leave the virtual environment, simply run: ```deactivate``` (with virtualenv) or ```conda deactivate``` (with Conda))

---

### 5. Install Requirements

    pip install -r requirements.txt
        
Conda:

    conda install pip
    pip install -r requirements.txt


---

_Optional_: If you're on Mac.  

***Note: if you are on mac, then first install wget using brew***  

    brew install wget

---

## Execution

Step 1: According to task, I have different files. You can run the task1, task2, task3 and 4 with:

```
bash my_task/run_task1.sh
bash my_task/run_task2.sh
bash my_task/run_task3.sh
bash my_task/run_task4.sh
```

Step 2: getting wer using for each type of prediction using bash file

- For task 1

```
bash my_task/run_task1.sh -lm <language model, either ngram, 1digit, 3digits or 5digits>

Usage : Script -lm <language model>
```

- For task 2

```
bash my_task/run_task2.sh -m <agegroup, man, woman, girl or boy> -lm <language model digitloop, 1digit, 3digits, 5digits>

Usage : Script -m <age group> -lm <language model>
```

- For Task 3

```
bash my_task/run_task3.sh -m <agegroup, man, woman, girl or boy> -lm <language model 1digit, 3digits, 5digits or digitloops>

Usage : Script -m <age group> -lm <language model>
```

- For Task 4

```
bash my_task/run_task4.sh -n <SNR value either 05, 15,25, 35> -lm <language model 1digit, 3digits, 5digits or digitloops>

Usage : Script -n <noise ratio> -lm <language model>
```
---

## Dataset
I used td_corpus, a digit corpus provided in the lab
Besides, I created a lexical dictionary of digits which is available in ps_data/lex/digits.dict

---

## Results
Tabular form of wer and confidence interval is below.
- Task 1: WER for man digit corpus with 35 db SNR
Language Model | #ngram | #1 digit | #3 digits | #5 digits | #digitloop 
--- | --- | --- | --- |--- |---
WER | 12.3  |10.5  |15  |11.3  |23.6

- Task 2: Different age group data with 35 db SNR for 1 digit corpus
Language Model | #Man | #Woman  | #Girl | #boy 
--- | --- | --- | --- |--- |---
WER | 10.5  |10.5  | 24  | 17.5

Different age group data with 35 db SNR for 3 digits corpus
Language Model | #Man | #Woman  | #Girl | #boy 
--- | --- | --- | --- |--- |---
WER | 15   |10   | 22.6   | 20

Different age group data with 35 db SNR for 5 digits corpus
Language Model | #Man | #Woman  | #Girl | #boy
--- | --- | --- | --- |--- |---
WER |  11.31   |7.8   |26.8   |18 

- Task 3 WER for Man and Woman corpus with 35 db SNR for different digits grammar
Language Model | #Man-1digit   |#Man-3Digit   |#Man-5Digit   |#Woman-1digit   |#Woman-3Digit   |#Woman-5Digit 
--- | --- | --- | --- |--- |---
WER | 10.5   | 15   | 11.2   | 10.5   | 10   | 7.8

- Task 4: WER for man with different SNR for 1 digit corpus
Language Model | #SNR35   | #SNR25   | #SNR15   | #SNR05 
--- | --- | --- | --- |--- |---
WER | 10.5   |11.5   | 18   | 94.697

WER for man with different SNR for 3 digits corpus
Language Model | #SNR35   | #SNR25   | #SNR15   | #SNR05 
--- | --- | --- | --- |--- |---
WER | 15   |16.6   |19.67   |93.237

WER for man with different SNR for 5 digits corpus
Language Model | #SNR35   | #SNR25   | #SNR15   | #SNR05 
--- | --- | --- | --- |--- |---
WER |  11.3   |11.4   |16.97   |76.27
## Licence
[MIT](https://choosealicense.com/licenses/mit/)

