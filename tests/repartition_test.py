from repartition.re_partition import re_partition

def test_repartition():
    size, read_path, write_path = re_partition('20150125', '/data/movie/extract')
    print(size)
    print(read_path)
    print(write_path)

    assert True
