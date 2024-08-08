from repartition.re_partition import re_partition

def test_repartition():
    size, read_path, write_path = re_partition('20150125', '/data/movie/extract')
    assert True
