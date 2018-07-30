
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import csv

def load_claim(fname):
    df = pd.read_csv('../policy_claim/' + fname)
    ig_column = ['Claim_Number', 'Vehicle_identifier']
    one_hot_column = ["Driver's_Gender", "Driver's_Relationship_with_Insured", 'Marital_Status_of_Driver', 'Cause_of_Loss', 'Accident_area']

    for name in ig_column:
        df = df.drop(name, axis=1)

    for name in one_hot_column:
        tmp = pd.get_dummies(df[name], prefix = name)
        df = df.drop(name, axis=1)
        df = df.join(tmp)

    return df

def multi2one(df):
    new_df = {}
    title = list(df.keys())
    acc_item = ['paid_Expenses_Amount', 'Salvage_or_Subrogation?', 'Deductible']
    for row in range(len(df)):
        if df['Policy_Number'][row] in new_df:
            for item in acc_item:
                new_df[df['Policy_Number'][row]][item] += df[item][row]
        
        else:
            new_df.update({df['Policy_Number'][row]:{}})
            for item in title:
                new_df[df['Policy_Number'][row]].update({item:df[item][row]})
    return new_df, title

def drop_age_miss(df):
    for row in range(len(df)):
        df['DOB_of_Driver'][row] = df['DOB_of_Driver'][row][3:]
        df['DOB_of_Driver'][row] = 2017 - int(df['DOB_of_Driver'][row])
    
    return df

def main():
    fname = 'claim_0702.csv'
    new_fname = 'claim_0702_v2.csv'
    print('one-hot encoding now...')
    df = load_claim(fname)
    print('age counting...')
    df = drop_age_miss(df)
    print('multi-policy to 1...')
    df, title = multi2one(df)
    print('done!')
    
    
    
    with open(new_fname, 'w', newline = '') as fout:
        wr = csv.writer(fout)
        wr.writerow(title)

        for usr in df:
            value = []
            for item in title:
                value.append(df[usr][item])

            wr.writerow(value)
    

if __name__ == '__main__':
    main()


# In[ ]:



