Speech modeling and automatic speech recognition
Lexicons and language models for ASR using pocketsphinx experiments –


# Outline

1. [Directory Structure](#directory-structure)
2. [Introduction](#introduction)
3. [Installation](#installation)
4. [Dataset](#dataset)
5. [Execution](#execution)
5. [Contributing](#contributing)
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

Note: Since, the project has three models as the pipeline running serially, it requires some memory space and RAM. Make sure you have around 3 GB physical disk space, 4 GB RAM and enough space to install the requirements. 

In order to get the model to run, follow these installation instructions.


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
#### 6. You also need to download the spacy model:

    python -m spacy download en_core_web_lg

---

### 7. Initial Downloads

orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.


************************************************************************************************************************************
**_YAY!!_** Installation is done! Now you can jump to the execution part and run the web app.


## Execution
**!!!** Before running the application, make sure to change the ```ROOT_PATH``` variable in the ```.env``` file to the path of your project.

To run the webapp, run the following code, being in the root directory.

    python3 src/views.py

---


## Dataset
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.



### x DATASET


### y Dataset

 Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
