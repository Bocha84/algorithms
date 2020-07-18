import pytest

import huffman
from test.integration import util


@pytest.mark.parametrize(
    "file, min_length, max_length",
    [("../../../huffman_10_40_input.txt", 4, 9), ("../../../huffman.txt", 9, 19)],
)
def test_code_lengths(file, min_length, max_length):
    array = util.get_array(file)
    weights = {str(k): w for k, w in enumerate(array[1:])}
    code = huffman.code(weights)
    lengths = huffman.lengths(code)
    assert min(lengths) == min_length
    assert max(lengths) == max_length
