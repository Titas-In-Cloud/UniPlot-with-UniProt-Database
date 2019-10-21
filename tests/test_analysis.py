import pytest
import uniplot.parse
import uniplot.analysis

TEST_UNIPROT = "./resources/uniprot_sprot_small.xml.gz"

def test_hello_world():
    assert True

def test_average():
    assert uniplot.analysis.proteins_average_lenght(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222222
