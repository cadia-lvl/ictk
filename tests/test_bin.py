from ictk import bin


def test_file_reading(bin_test_file):
    bin_client = bin.BIN.from_file(bin_test_file)
    assert bin_client.entries == 10
