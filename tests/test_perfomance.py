import pytest
from endpoints.create_obj import CreateObj
from endpoints.get_stat import GetStat
from endpoints.get_obj import GetObj
from endpoints.del_obj import DeleteObj
from endpoints.get_all_objs import GetAllObjects
from tests.test_data.payloads import *
import time


def test_response_time_get_item(obj_id):
    get_obj = GetObj()
    start = time.time()
    get_obj.get_obj(obj_id)
    elapsed = (time.time() - start) * 1000
    assert elapsed < 500


def test_response_time_create_item():
    create_obj = CreateObj()
    payload = fixture_payload.copy()
    start = time.time()
    create_obj.create_obj(payload)
    elapsed = (time.time() - start) * 1000
    assert elapsed < 1000