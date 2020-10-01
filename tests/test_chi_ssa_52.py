from datetime import datetime
from os.path import dirname, join

from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.chi_ssa_52 import ChiSsa52Spider

test_response = file_response(
    join(dirname(__file__), "files", "chi_ssa_52.html"),
    url="https://www.51ststreetchicago.com/about.html",
)
spider = ChiSsa52Spider()

freezer = freeze_time("2020-09-14")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


# def test_tests():
#     print("Please write some tests for this spider or at least disable this one.")
#     assert False


"""
Uncomment below
"""


def test_title():
    assert parsed_items[0]["title"] == "SSA # 52 SCHEDULED MEETING DATES 2019"


# def test_description():
#     assert parsed_items[0]["description"] == "EXPECTED DESCRIPTION"


def test_start():
    assert parsed_items[0]["start"] == datetime(2020, 2, 18, 1, 30)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


# def test_time_notes():
#     assert parsed_items[0]["time_notes"] == "EXPECTED TIME NOTES"


# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"


# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"


# def test_location():
#     assert parsed_items[0]["location"] == {
#         "name": "EXPECTED NAME",
#         "address": "EXPECTED ADDRESS"
#     }


# def test_source():
#     assert parsed_items[0]["source"] == "EXPECTED URL"


# def test_links():
#     assert parsed_items[0]["links"] == [{
#       "href": "EXPECTED HREF",
#       "title": "EXPECTED TITLE"
#     }]


# def test_classification():
#     assert parsed_items[0]["classification"] == NOT_CLASSIFIED


# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
