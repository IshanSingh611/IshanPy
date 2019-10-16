#KNN CLASSIFIER
import pandas as pd
import numpy as np
def distance(x,new_age,new_loan):
    return np.sqrt(((x["Age"]-new_age)**2)+((x["Loan"]-new_loan)**2))

def KNNClassifier(new_age,new_loan,threshold_value=3):
    dataset = pd.read_excel("loan_repayment_details.xlsx")
    df = pd.DataFrame(dataset)
    df["Distance"] = df[["Age", "Loan"]].apply(distance, axis=1, args=(new_age, new_loan))
    df.sort_values(by='Distance', ascending=True, inplace=True)
    print(df)
    default_data = df.iloc[:threshold_value, 2:3]
    data = list(default_data["Default"].map({'Y': 1, 'N': 0}))
    one = data.count(1)
    zero = data.count(0)
    return one > zero

new_age,new_loan,threshold_value = [int(i) for i in input("Enter Data: ").split()]
if KNNClassifier(new_age,new_loan,threshold_value):
    print("Person with a given data predicted to be a Loan Defaulter")
else:
    print("Person with a given data predicted NOT to be a Loan Defaulter")