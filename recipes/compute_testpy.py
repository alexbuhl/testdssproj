# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
new_customers_joined = dataiku.Dataset("new_customers_joined")
new_customers_joined_df = new_customers_joined.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

testpy_df = new_customers_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
testpy = dataiku.Dataset("testpy")
testpy.write_with_schema(testpy_df)
