# Model Card

## Model Details

	- Developer: Ryan Olsesski
	- Model Date: March 22, 2024
	- Model Version: 1.0.0
	- Model Type: Random Forest Classifier
	- Parameters: 100 Estimators (n_estimators=100)
	- Resource: GitHub Repository: https://github.com/Exeatop/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

## Intended Use

	- Primary Intended Use:
		Place-holder model for pipeline development.
	- Primary Intended Users:
		Those verifying the validity of the pipeline.
	- Out-of-Scope Use Cases:
		Not reccommended for any kind of informed decision making.
		
## Training Data

	- Dataset: "Census Income - UCI Machine Learning Repository"
	- Date: 1994 Census Database
	- Description:
		Categorical and integer dataset with 14 features and 48842 instances intended to be used for machine learning classification tasks.
		

## Evaluation Data

	- Dataset: "Census Income - UCI Machine Learning Repository"
	- Description:
		Subset of Training Data.
	- Ratio:
		20% of data is used for evaluation, and 80% for training.

## Metrics

	- Metrics Used: Precision, Recall, F1 Score
	- Performance:
		- Precision: 74.19%
		- Recall: 63.84%
		- F1 Score: 68.63%

## Ethical Considerations

	- Data:
		No sensitive data is used.
	- Human Life:
		The model is not intended to be used in any informed decision-making.
	- Use Cases:
		The use of the model in any informed decision-making will be influenced by the biases that exist within the dataset and should be avoided.

## Caveats and Recommendations

	- DO NOT USE:
		This model is not for use in decision-making. It exists only for pipeline development.
