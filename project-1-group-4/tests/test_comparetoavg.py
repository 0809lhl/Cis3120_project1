# tests/test_comparetoavg.py
from src.comparetoavg import comparetoavg

def test_compare_mixed(capsys):
	"""
	Vertifies output for numbers less than, equal to, and greater than average.
	"""
	comparetoavg(4,5,6,5)
	captured = capsys.readouterr()
	assert '4 is less than the average 5\n' in captured.out
	assert '5 is equal to the average 5\n' in captured.out
	assert '6 is greater than the average 5\n' in captured.out



