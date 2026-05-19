# Smart Text Assistant (CLI-Based NLP Project)

## Objective

The objective of this project is to develop a CLI-based Smart Text Assistant that performs basic Natural Language Processing (NLP) tasks such as dictionary lookup, spelling correction, and next-word prediction. The project combines rule-based NLP techniques, trigram language modeling, and frequency-based prediction systems to build an intelligent CLI assistant.

---

## Features

* Dictionary Lookup (Meaning + Synonyms)
* Spelling Correction with user confirmation
* Next Word Prediction
* Trigram-based language model
* Frequency-based fallback prediction
* Text preprocessing pipeline
* CLI-based interaction system

---

## Technologies Used

* Python 3.x
* NLTK (Natural Language Toolkit)
* TextBlob
* wordnet
* wordfreq
* Pickle
* Trigram (N-gram) Language Model
* Rule-based NLP logic

---

## Datasets Used

The project uses public datasets for training and experimentation.

Datasets used:

* WikiText Dataset
* Chatbot Conversations Dataset

These datasets were used to improve sentence prediction, conversational understanding, and next-word suggestion quality.

---

## Text Preprocessing Pipeline

The datasets are cleaned and normalized before training the language model.

### Preprocessing Steps

### Step 1: Text Normalization

* Convert text to lowercase
* Replace special quotation marks
* Remove unnecessary symbols

### Step 2: Noise Removal

* Remove URLs and unwanted characters
* Handle special tokens and formatting symbols
* Normalize whitespace

### Step 3: Sentence Handling and Tokenization

* Convert sentence endings into EOS tokens
* Tokenize cleaned text into words
* Prepare tokens for trigram model training

---

## Workflow

### Step 1: User Input

The user enters a word or sentence through the command-line interface.

### Step 2: Input Processing

The input text is cleaned, normalized, and tokenized using the preprocessing pipeline.

### Step 3: NLP Processing

Based on the input type:

* Single word → Dictionary lookup and spelling correction
* Sentence → Next-word prediction

### Step 4: Prediction System

- Trigram model predicts the next word using statistical word sequence patterns
- Frequency-based fallback suggestions are used if trigram prediction is unavailable

### Step 5: Output Generation

The final suggestions are displayed to the user.

---

## Model Export

The trained trigram language model is exported as a `.pkl` file for reusable inference without retraining.

---

## Sample Outputs

### Input

```text
sarry
```

### Output

```text
Did you mean 'sorry'? (y/n)
```

---

### Input

```text
happy
```

### Output

```text
Meaning: feeling or showing pleasure
Synonyms: glad, joyful, pleased
```

---

### Input

```text
I am feeling
```

### Output

```text
Suggestions: happy, sad, tired, good
```

---

## Conclusion

This project demonstrates a hybrid NLP-based Smart Text Assistant integrating preprocessing pipelines, trigram language modeling, rule-based NLP techniques, and frequency-based prediction systems using public datasets such as WikiText and Chatbot Conversations. The project provides a strong foundation for understanding practical NLP workflows and intelligent text prediction systems.
