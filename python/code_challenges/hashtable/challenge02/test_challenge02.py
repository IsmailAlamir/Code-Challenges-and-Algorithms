# Write your test here
import pytest
from challenge02 import *



def test_repeated_word():
  actual = first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
  extcepted = "ASAC"
  assert actual == extcepted

def test_no_repetition():
  actual =first_repeated_word("I am learning programming at ASAC") 
  extcepted = "No Repetition"
  assert actual == extcepted
