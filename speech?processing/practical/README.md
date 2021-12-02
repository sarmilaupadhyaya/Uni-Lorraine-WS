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

├── ps_data   #this structure was provided in the lab. only modification is that a new lex/digits.dict is added
|
├── ps_exemples # contains code snippet to run the asr model using different langauge model
|
├── td_corpus_digits # supposed to contain the digit corpus
|
├── documents 
|   |
│   └── report.pdf #report of the experiment
├── my_task 
|   |
│   ├── run_task1.sh ## running the main task where the prediction is generated based on task
│   ├── run_task2.sh
|   |── run_task3.sh
│   ├── run_task4.sh
│   ├── run_wer_task1.sh ## bash script that inputs the parameters and give out the wer calculated
│   └── run_wer_task2.sh
|   |── run_wer_task3.sh
│   ├── run_wer_task4.sh
│   ├── task1_wer.py ## python script where wer values are manually plotted with there confidence interval
│   └── task2_wer.py
|   ├── task3_wer.py
│   └── task4_wer.py
|   └── generation.py ##main python file which takes the argument and gives out prediction according to parameters
|   ├── decoder_jsgf.py ## model with jsgf grammar
│   └── decoder_ngram.py ## model with ngram model
|   ├── images/ ## plots of wer rate with confidence interval
|
├── README.md 

    


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

