# Questioning-Answering Using BERT-SQUAD

### Use google BERT to do SQUAD  !

## What is SQUAD?
Stanford Question Answering Dataset (SQUAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

## Requirements
- python3
- pip install -r requirements.txt

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/QA_with_BERT_SQUAD
```

### Step-2: Navigate to the project directory:
```bash
    cd QA_with_BERT_SQUAD
```

### Step 3: Create a conda environment after opening the repository

```bash
    conda create -p env python=3.6 -y
```

```bash
    source activate ./env
```

### Step 4: Install the requirements
```bash
    pip install -r requirements.txt
```

### Step 5: Install the pytorch from the link
```bash
    https://pytorch.org/get-started/locally/
```
```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Step 6: Add the pre-trained model in your project structure. I had trained the model already.
As **pytorch_model.bin** is very large in size(1250 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the model folder in your project structure.

You can download the **pytorch_model.bin** from [here](https://www.dropbox.com/scl/fi/4whv8917xgxc66eef83el/pytorch_model.bin?rlkey=05n3zsek2l6kda5bmwtlprpa7&st=ccs950m5&dl=0)


### Step-7: Run the application:
```bash
    python clientApp.py
```

### Step-8: Prediction application:
```bash
    http://localhost:8000/
```

## Result
- `model` : bert-large-uncased-whole-word-masking 
```json
{"exact_match": 86.91579943235573, "f1": 93.1532499015869}
```
### Pretrained model download from [here](https://www.dropbox.com/s/8jnulb2l4v7ikir/model.zip) unzip and move files to model directory

# Inference
```python
from bert import QA

model = QA('model')

doc = "Victoria has a written constitution enacted in 1975, but based on the 1855 colonial constitution, passed by the United Kingdom Parliament as the Victoria Constitution Act 1855, which establishes the Parliament as the state's law-making body for matters coming under state responsibility. The Victorian Constitution can be amended by the Parliament of Victoria, except for certain 'entrenched' provisions that require either an absolute majority in both houses, a three-fifths majority in both houses, or the approval of the Victorian people in a referendum, depending on the provision."

q = 'When did Victoria enact its constitution?'

answer = model.predict(doc,q)

print(answer['answer'])
# 1975
print(ans.keys())
# dict_keys(['answer', 'start', 'end', 'confidence', 'document']))
```
`model.predict(doc,q)` return `dict`
```json
{
"answer" : "answer text",
"start" : "start index",
"end" : "end index",
"confiednce" : "confidence of answer",
"document" : "tokenzied document , list"
}
```

# Deploy REST-API
BERT QA model deployed as rest api

```bash
python api.py
```
API will be live at `0.0.0.0:8000` endpoint `predict`

### CURL request
```bash
curl -X POST http://0.0.0.0:8000/predict -H 'Content-Type: application/json' -d '{ "document": "Victoria has a written constitution enacted in 1975, but based on the 1855 colonial constitution, passed by the United Kingdom Parliament as the Victoria Constitution Act 1855, which establishes the Parliament as the states law-making body for matters coming under state responsibility. The Victorian Constitution can be amended by the Parliament of Victoria, except for certain 'entrenched' provisions that require either an absolute majority in both houses, a three-fifths majority in both houses, or the approval of the Victorian people in a referendum, depending on the provision.","question":"When did Victoria enact its constitution?" }'
```
#### Output
```json
{
    "result": {
        "answer": "1975",
        "confidence": 0.940746070672879,
        "document": [
            "Victoria",
            "has",
            "a",
            "written",
            "constitution",
            "enacted",
            "in",
            "1975,",
            "but",
            "based",
            "on",
            "the",
            "1855",
            "colonial",
            "constitution,",
            "passed",
            "by",
            "the",
            "United",
            "Kingdom",
            "Parliament",
            "as",
            "the",
            "Victoria",
            "Constitution",
            "Act",
            "1855,",
            "which",
            "establishes",
            "the",
            "Parliament",
            "as",
            "the",
            "states",
            "law-making",
            "body",
            "for",
            "matters",
            "coming",
            "under",
            "state",
            "responsibility.",
            "The",
            "Victorian",
            "Constitution",
            "can",
            "be",
            "amended",
            "by",
            "the",
            "Parliament",
            "of",
            "Victoria,",
            "except",
            "for",
            "certain",
            "entrenched",
            "provisions",
            "that",
            "require",
            "either",
            "an",
            "absolute",
            "majority",
            "in",
            "both",
            "houses,",
            "a",
            "three-fifths",
            "majority",
            "in",
            "both",
            "houses,",
            "or",
            "the",
            "approval",
            "of",
            "the",
            "Victorian",
            "people",
            "in",
            "a",
            "referendum,",
            "depending",
            "on",
            "the",
            "provision."
        ],
        "end": 7,
        "start": 7
    }
}
```
### Postman
![postman output image](/img/postman.png)
