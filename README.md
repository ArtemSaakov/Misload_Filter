# Misload_Filter
a tool to quickly narrow down potential bad plots. 

reads an excel file into a pandas dataframe and compares two
specific column values in each series. if the comparison returns false, the series is dropped 
from the dataframe. the new dataframe is rewritten to the original excel file.

this is for my job, hence any strange terminology. 
