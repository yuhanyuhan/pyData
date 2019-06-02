import pytest
from index import df, excelname
from refactor_test import subtitle_length, subtitle_unique_length, subtitle_list

def test1():
    a = subtitle_list
    dupes = [x for n, x in enumerate(a) if x in a[:n]]
    assert (subtitle_length == subtitle_unique_length) == True

#Testing whether the excelname variable contains the text"csv"
def test2():
    text = "csv"
    assert text in excelname

#Checking that the dataframe is not empty
def test3():
    assert df is not df.empty