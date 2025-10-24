
# Libraries 

1. Sentencepiece

- SentencePiece is a language-independent subword tokenizer and detokenizer for NLP, designed to work directly with raw text data. 

- It breaks text into smaller units called "subwords," which are then used by neural networks, making it useful for tasks like neural machine translation and for handling languages that lack clear word boundaries, such as Japanese.


2. SacreBLEU

- SacreBLEU is a Python library designed for computing the BLEU (Bilingual Evaluation Understudy) score, a widely used metric for evaluating the quality of machine translation.

- It is particularly known for providing hassle-free computation of shareable, comparable, and reproducible BLEU scores.

- Here, to calculate evaluation matrix for Text Summarization task, we need `Sacrebleu` library, to calculate the accuracy score `rouge score`.


3. In `setup.py`, we are reading `README.md` file because  

- If we want to publish this project as a package in `pyPy`, then we need to read `README.md` file in the pyPy site, to display it, in the front as a package description. 

- Here, we are not publishing in `pyPy` but we will be using this as a local package. 


4. Use of setuptools.setup() 

- This function will look for the constructor file `__init__.py` in every folder and will install it as my local package.