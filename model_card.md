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

## Caveats and Recommendations