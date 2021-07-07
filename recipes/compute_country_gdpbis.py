# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
country_gdp = dataiku.Dataset("country_gdp")
country_gdp_df = country_gdp.get_dataframe()

import debugpy
# 5678 is the default attach port in the VS Code debug configurations. Unless a host and port are specified, host defaults to 127.0.0.1
debugpy.listen(5678)
debugpy.wait_for_client()
print("test")
debugpy.breakpoint()
print("second")
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

country_gdpbis_df = country_gdp_df # For this sample code, simply copy input to output

# Write recipe outputs
country_gdpbis = dataiku.Dataset("country_gdpbis")
country_gdpbis.write_with_schema(country_gdpbis_df)