import pytest
import uniplot.parse
import uniplot.analysis

TEST_UNIPROT = "./resources/uniprot_sprot_small.xml.gz"

def test_hello_world():
    """Tests if the file works"""
    assert True

def test_average():
    """Tests the average length function"""
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222222
