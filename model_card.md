# Model Card
Classification Model
## Model Details
Created by Aaron Fowler, 2024, v1.
## Intended Use
Used to classify what an individual makes annually based on multiple factors.
The model will evaluate if the individual makes under $50k a year or if the individual makes $50k or more a year.
## Training Data
census.csv provided by Udacity, training data split (80% of the data for training and 20% of the data for testing).
## Evaluation Data
census.csv provided by Udacity, training data split (80% of the data for training and 20% of the data for testing).
## Metrics
This is a RandomForestClassifier model with default parameters. The metrics used are Precision, Recall, and F1(fbeta).
The results on the last run are as follows:
Precision: 0.7310
Recall: 0.6101
F1: 0.6651
## Ethical Considerations
This model should only be used for description purposes only. The model contains features such as sex, age, race etc. which should not be used when determining things such as credit worthiness or other similar uses.
## Caveats and Recommendations
The model uses default parameters. For more accurate metrics hyperparameters can be used.
