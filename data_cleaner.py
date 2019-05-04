import pandas as pd
import numpy as np

# Read in data into a dataframe
data = pd.read_csv('data.csv')

# Display top of dataframe
data.head()

# see column data types and non-missing values
# data.info()
# but incorrect storing of some columns as String object (instead of int/float)

# replace all instances of Not Available with numpy not a number
# replace is case sensitive!!
data = data.replace({'Not Available': np.nan})

# Iterate through columns
for col in list(data.columns):

    # Select columns that should be numeric.
    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in
            col or 'therms' in col or 'gal' in col or 'Score' in col):

        # Convert the data type to float
        data[col] = data[col].astype(float)

# see column data types and non-missing values
# data.info() #still works
print(data.describe())


def missing_values_table(df):
    # total missing values
    mis_val = df.isnull().sum()

    # percentage of missing values
    mis_val_percent = 100 * mis_val / len(df)

    # make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(columns = {0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
           "There are " + str(mis_val_table_ren_columns.shape[0]) + " columns that have missing values.")

    #return the dataframe with missing information
    return mis_val_table_ren_columns


print(missing_values_table(data))

# Get columns with more than 50% of values missing
missing_df = missing_values_table(data);
missing_columns = list(missing_df[missing_df['% of Total Values']>50].index)
print('\nWe will remove %d columns.' % len(missing_columns))
