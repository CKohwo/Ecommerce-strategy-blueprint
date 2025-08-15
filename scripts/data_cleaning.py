import pandas as pd
from pathlib import Path


#Making sure the dataframe is logically correct, actual price must be greater or equal to discounted price
def price_check(df, issues):
    invalid_rows = df[df["discounted_price"] > df["actual_price"]]
    if not invalid_rows.empty:
        issues["invalid_price"] = invalid_rows
    return issues    


def ratings_check(df, issues):

#Checking for logical error in the ratings, rating must not exceed 5      
    invalid_ratings = df[df["rating"] > 5]
    if not invalid_ratings.empty:
        issues["ratings_above_5"] = invalid_ratings

#Checking for logical error in the ratings, rating must not be lower than 0       
    invalid_neg_ratings = df[df["rating"] < 0]
    if not invalid_neg_ratings.empty:
        issues["ratnigs_below_0"] = invalid_neg_ratings
    return issues    
         
  
      

# checking for unrealistic discount(>90%) in the dataframe      
def check_discount(df, issues):
    unrealistic_discount = df[df["discount_percentage_num"] > 90]
    if not unrealistic_discount.empty:
        issues["unrealstics_dis"] = unrealistic_discount 
    return issues    


#Checking for duplicates within the dataframe
def check_duplicates(df, issues):
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        issues["duplicates"] = duplicates 
    return issues           



def data_cleaning(df, export_path = None ):
     
    issues = {}
    issues = price_check(df, issues)
    issues = ratings_check(df, issues)
    issues = check_discount(df, issues)
    issues = check_duplicates(df, issues)
     
    if export_path:
        for name, data in issues.items():
            data.to_csv(f"{export_path}_{name}.csv", index=False)

    return issues