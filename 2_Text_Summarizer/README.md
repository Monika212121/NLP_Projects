# Project : End to End Text-Summarizer with Deployment


# Description : 
It takes text of any length and summarizes the text to the desired limit of words, without loosing it's meaning and context.


# Workflow:
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src/config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py


# Stages in this project:

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation
6. Prediction

# Tools and frameworks used:
1. HuggingFace
2. FastAPI


# Setup steps:

1.) Create a file named "template.py" and write all the filenames we need to create for this project.
 
2.) Run the file using command `python template.py`. We can see all the files along with its directories are created.

3.) Create a conda environment using the command `conda create -p textSum python=3.10`.

4.) Install all the dependencies using commands `pip install -r requirements.txt`. This process can be slow in local system.

- If you have GPU, install Pytorch which can speed up the process, if not torch will use your system's CPU, which will be slower.


# Developing steps:

5.) While completing every stage mentioned above, check the pipeline using command `python main.py`.


# Inference steps:

6.) After completing all the stages, complete the "app.py" file and run this file using command `python app.py`.

7.) The server will run and a link will appear on the terminal.

8.) Open a browser and type `localhost:8080` and a FastAPI UI will be opened.

9.) A Ui will appear, first click on train and then predict. 

- If the artifacts folder is created once while training, then no need to train again and again, just predict.


### Important Note: If you have GPU in your system, make these changes:

a. In `main.py` file, uncomment line 55 and 56.
b. In `config/configuration.py` file, in line 86, write `config = self.config.model_evaluation` instead of `config = self.config.model_evaluation2` so it will take the trained model and tokenier, not the manually placed one.
