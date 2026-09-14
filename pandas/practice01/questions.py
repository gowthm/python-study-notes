import pandas as pd
from setup import load, ADDONS

pd.set_option("display.width", 100)
df = load()

def q(n, text, expr):
    print(f"\n{'='*72}\nQ{n}. {text}\n{'-'*72}")
    print(expr)


q(1, "Which contract type has the highest churn rate?",
   df.groupby("Contract", observed=True).churned.mean().sort_values(ascending=False))

q(2, "Which 5 payment-method x internet-service pairs churn most?",
   df.groupby(["PaymentMethod", "InternetService"], observed=True)
     .churned.agg(["mean", "size"]).nlargest(5, "mean"))

q(3, "Median monthly charge by internet service, split by churn?",
   df.pivot_table(index="InternetService", columns="Churn",
                  values="MonthlyCharges", aggfunc="median", observed=True))

q(4, "What share of month-to-month fibre customers without tech support churned?",
   df.loc[df.Contract.eq("Month-to-month")
          & df.InternetService.eq("Fiber optic")
          & df.TechSupport.eq("No"), "churned"].mean())

q(5, "How does churn rate move across tenure quintiles?",
   df.groupby(pd.qcut(df.tenure, 5), observed=True)
     .agg(churn_rate=("churned", "mean"), customers=("churned", "size")))

q(6, "Who are the 5 highest-lifetime-value customers that we lost?",
   df.loc[df.churned].nlargest(5, "TotalCharges")[["tenure", "MonthlyCharges", "TotalCharges", "Contract"]])

q(7, "Which add-on service shows the biggest churn gap between having it and not?",
   df[ADDONS].apply(lambda s: df.churned[s.eq("No")].mean() - df.churned[s.eq("Yes")].mean())
             .sort_values(ascending=False).rename("churn_gap"))

q(8, "Are senior citizens over-represented among churners?",
   pd.crosstab(df.SeniorCitizen, df.Churn, normalize="index"))

q(9, "What share of monthly recurring revenue walked out the door, by contract?",
   df.groupby("Contract", observed=True)
     .apply(lambda g: g.loc[g.churned, "MonthlyCharges"].sum() / g.MonthlyCharges.sum(),
            include_groups=False))

q(10, "Does stacking on more add-ons reduce churn?",
    df.groupby(df[ADDONS].eq("Yes").sum(axis=1).rename("n_addons"), observed=True)
      .agg(churn_rate=("churned", "mean"),
           median_bill=("MonthlyCharges", "median"),
           customers=("churned", "size")))
