import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import inference, train_model, save_model, load_model

# Create sample data for testing
data = pd.DataFrame({
    "feature_1": np.random.randint(2, size=10),
    "feature_2": np.random.randint(2, size=10),
    "feature_3": np.random.randint(3, size=10),
    "feature_4": np.random.randint(3, size=10),
    "target": np.random.randint(2, size=10)
})

features = [
    "feature_1",
    "feature_2",
    "feature_3",
    "feature_4"
]

train, test = train_test_split( data, test_size=0.2)
X_train, y_train, encoder, lb = process_data(
    train,
    features,
    "target",
    training=True)

X_test, y_test, _, _ = process_data(
    test,
    features,
    "target",
    training=False,
    encoder=encoder,
    lb=lb,
)

model = train_model(X_train, y_train)

def test_inference():
    """
    Test if inference function returns ndarray
    """
    preds = inference(model, X_test)
    assert isinstance(preds, np.ndarray)

def test_train_model():
    """
    Test if train_model function returns RandomForestClassifier instance
    """
    assert isinstance(model, RandomForestClassifier)

def test_load_model():
    """
    Test if loading model returns saved instance type
    """
    project_path = os.getcwd()
    model_path = os.path.join(project_path, "test.pkl")
    save_model(model, model_path)
    loaded_model = load_model(model_path)
    assert isinstance(loaded_model, RandomForestClassifier)
    if os.path.isfile(model_path): os.remove(model_path)
