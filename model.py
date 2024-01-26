from sklearn import datasets
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
diabetes = datasets.load_diabetes(scaled=False)

# Create and train a linear regression model
model = LinearRegression()
model.fit(diabetes.data, diabetes.target)

# Save the model
joblib.dump(model, 'diabetes_model.pkl')

##write code for a flask app







