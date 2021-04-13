# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
country_to_geopoint = dataiku.Dataset("country_to_geopoint")
country_to_geopoint_df = country_to_geopoint.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

country_to_geopoint_py_df = country_to_geopoint_df # For this sample code, simply copy input to output


# Write recipe outputs
country_to_geopoint_py = dataiku.Dataset("country_to_geopoint_py")
country_to_geopoint_py.write_with_schema(country_to_geopoint_py_df)