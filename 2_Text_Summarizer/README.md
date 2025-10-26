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


# Tools and frameworks used:


# Setup steps:

1. Create a file named "template.py" and write all the filenames we need to create for this project.
 
2. Run the file using command `python template.py`. We can see all the files along with its directories are created.

3. Create a conda environment using the command `conda create -p textSum python=3.10`.

4. Install all the dependencies using commands `pip install -r requirements.txt`. This process can be slow in local system.

- If you have GPU, install Pytorch which can speed up the process, if not torch will use your system's CPU, which will be slower.
