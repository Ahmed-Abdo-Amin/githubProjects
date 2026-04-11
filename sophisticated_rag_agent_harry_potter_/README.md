# 📚 Autonomous Retrieval & QA Agent

A modular, production-ready pipeline for answering complex questions from structured book data, including:

- Book chunks
- Chapter summaries
- Book quotes

The system is capable of planning, breaking down tasks, retrieving relevant content, and producing grounded answers.

---

## Requirements

- **Python 3.12.12 or later**  
- Install Python using **Miniconda**  

### Install Miniconda

1. Download and install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).  

2. Create a new environment using the following command:

```bash
$ conda create -n myenv312 python=3.12.12
```
3. Activate the environment:

```bash
$ conda activate myenv312
```

### (Optional) Setup you command line interface for better readability

```bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

##  Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```
Set your environment variables in the .env file. Like OPENAI_API_KEY value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```


