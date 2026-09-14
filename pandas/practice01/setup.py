import pandas as pd

CATS = ["gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
        "PaperlessBilling", "PaymentMethod", "Churn"]

ADDONS = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
          "TechSupport", "StreamingTV", "StreamingMovies"]


def load(path="telco.csv"):
    df = (
        pd.read_csv(
            path,
            dtype={c: "category" for c in CATS} | {"tenure": "int16", "SeniorCitizen": "int8"},
            na_values=[" "],                 # the 11 blank TotalCharges
        )
        .assign(
            TotalCharges=lambda d: pd.to_numeric(d.TotalCharges),
            churned=lambda d: d.Churn.eq("Yes"),
        )
        .set_index("customerID")             # the natural primary key
    )
    return df
