from extract_position import extract_position


def test_extract_position():
    check_error = 'error'
    check_update = 'x:21.432'
    assert extract_position(check_error) == None
    assert extract_position(0) == None
    assert extract_position(check_update) == "21.432"
