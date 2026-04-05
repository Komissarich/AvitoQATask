import pytest
from endpoints.create_obj import CreateObj
from endpoints.get_stat import GetStat
from endpoints.get_obj import GetObj
from endpoints.del_obj import DeleteObj
from endpoints.get_all_objs import GetAllObjects
from tests.test_data.payloads import *


def test_get_obj(obj_id):
    get_object = GetObj()
    get_object.get_obj(obj_id)
    get_object.check_200()
    get_object.check_obj(obj_id, fixture_payload)


def test_get_all_objects(seller_id, many_obj_ids):
    get_all_object = GetAllObjects()
    get_all_object.get_all_objects(seller_id)
    get_all_object.check_200()
    get_all_object.check_all_objs(many_obj_ids, get_all_from_seller_payload)


def test_delete_obj():
    create_obj = CreateObj()
    create_obj.create_obj(payload=fixture_payload)
    create_obj.check_200()
    id = create_obj.response_json['status'].split()[3]
    delete_object = DeleteObj()
    delete_object.del_obj(id)
    delete_object.check_200()


def test_get_stat_v1(obj_id):
    get_stat_object = GetStat()
    get_stat_object.get_stat_v1(obj_id)
    get_stat_object.check_200()
    get_stat_object.check_stat(fixture_payload)


def test_get_stat_v2(obj_id):
    get_stat_object = GetStat()
    get_stat_object.get_stat_v2(obj_id)
    get_stat_object.check_200()
    get_stat_object.check_stat(fixture_payload)
