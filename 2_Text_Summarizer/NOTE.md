
# Important notes

### 1.) Sentencepiece

- SentencePiece is a language-independent subword tokenizer and detokenizer for NLP, designed to work directly with raw text data. 

- It breaks text into smaller units called "subwords," which are then used by neural networks, making it useful for tasks like neural machine translation and for handling languages that lack clear word boundaries, such as Japanese.


### 2.) SacreBLEU

- SacreBLEU is a Python library designed for computing the BLEU (Bilingual Evaluation Understudy) score, a widely used metric for evaluating the quality of machine translation.

- It is particularly known for providing hassle-free computation of shareable, comparable, and reproducible BLEU scores.

- Here, to calculate evaluation matrix for Text Summarization task, we need `Sacrebleu` library, to calculate the accuracy score `rouge score`.


### 3.) In `setup.py`, we are reading `README.md` file because  

- If we want to publish this project as a package in `pyPy`, then we need to read `README.md` file in the pyPy site, to display it, in the front as a package description. 

- Here, we are not publishing in `pyPy` but we will be using this as a local package. 


### 4.) Use of setuptools.setup() 

- This function will look for the constructor file `__init__.py` in every folder and will install it as my local package.


### 5.) Use of `config.yaml` file.

- We are mentioning the location of artifacts folder, the source of data URL(github) and also the data unzip dir name. 

- If we want to change any file name, we can change from this file, there is no need to manually go the file and change its name.  


### 6.) Use of Data validation

- It will create a `status.txt` file and "data_validation" part will check whether the data in artifacts folder are in given order or not, mentioned in the ALL_REQUIRED_FILES list.

- If the 3 folders(train, test, validation) are available, then status.txt = true, if not then false. 

- Reason: Before providing data to our model during training, if there is anything wrong with the dat, it will throw error. We do Data validation to avoid this error. So, we need to verify that our data is in correct format or not before give it to the model training.


### 7. Why in config.yaml, model_evaluation2 is used instead of model_evaluation

- I don't have GPU on my system, so I cannot train such a heavy model on my system.

- I trained the same code with same data using Google Colab, using GPU instead.

- I downloaded the 2 things 'pegasus-model' files and 'tokenizer' files and kept them in `model_trainer_artifacts` folder.


### 8. Why I am skipping training pipeline

- I cannot train such a heavy model on my system (see point 7).

- So, as training is not completed, the files will not be created for the model and tokenizer inside the `artifacts/model_trainer` folder.

-  During evaluation, when we are about to read these files, it will throw error.

- So, to avoid the error and breking of the entire pipeline, I am keeping my manually dowloaded model and tokenizer in another location and reading them from those files.