import pytest
from endpoints.create_obj import CreateObj
from endpoints.get_stat import GetStat
from endpoints.get_obj import GetObj
from endpoints.del_obj import DeleteObj
from endpoints.get_all_objs import GetAllObjects
from tests.test_data.payloads import *


@pytest.mark.parametrize("payload,status", negative_create_payloads)
def test_create_obj_negative(payload, status):
    create_obj = CreateObj()
    create_obj.create_obj(payload)
    assert create_obj.response.status_code == status


@pytest.mark.parametrize("obj_id,status", negative_get_obj_ids)
def test_get_object_negative(obj_id, status):
    get_obj = GetObj()
    get_obj.get_obj(obj_id)
    assert get_obj.response.status_code == status


@pytest.mark.parametrize("seller_id,status", negative_get_all_obj_ids)
def test_get_all_objects_negative(seller_id, status):
    get_obj = GetAllObjects()
    get_obj.get_all_objects(seller_id)
    assert get_obj.response.status_code == status


@pytest.mark.parametrize("obj_id,status", negative_statistic_ids_v1)
def test_get_statistic_v1_negative(obj_id, status):
    get_stat = GetStat()
    get_stat.get_stat_v1(obj_id)
    assert get_stat.response.status_code == status

@pytest.mark.parametrize("obj_id,status", negative_statistic_ids_v2)
def test_get_statistic_v2_negative(obj_id, status):
    get_stat = GetStat()
    get_stat.get_stat_v2(obj_id)
    assert get_stat.response.status_code == status


@pytest.mark.parametrize("obj_id,status", negative_delete_ids)
def test_delete_item_negative(obj_id, status):
    delete_obj = DeleteObj()
    delete_obj.del_obj(obj_id)
    assert delete_obj.response.status_code == status


