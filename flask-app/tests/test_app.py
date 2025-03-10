from app import calculate_race_times, format_time

def test_format_time():
    assert format_time(0) == "0:00"
    assert format_time(1) == "1:00"
    assert format_time(10) == "10:00"
    assert format_time(60) == "1:00:00"
    assert format_time(181) == "3:01:00"
    assert format_time(611) == "10:11:00"

def test_calculate_race_times():
    # pace per km is 5 min
    # TODO: complete the dict with the expected times
    distance_result = { 
        "5K": "25:00",
        "10K": "",
        "Half Marathon": "",
        "Marathon": ""
    }

    assert calculate_race_times(5) == distance_result 