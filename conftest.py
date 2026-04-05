import pytest
from endpoints.create_obj import CreateObj
from endpoints.del_obj import DeleteObj
from endpoints.get_all_objs import GetAllObjects
from tests.test_data.payloads import *
import time


@pytest.fixture
def obj_id():
    create_obj = CreateObj()
    create_obj.create_obj(payload=fixture_payload)
    create_obj.check_200()
    id = create_obj.response_json['status'].split()[3]
    yield id
    delete_obj = DeleteObj()
    delete_obj.del_obj(id)
    delete_obj.check_200()


@pytest.fixture
def seller_id():
    return DEFAULT_SELLER_ID


@pytest.fixture
def many_obj_ids():
    get_all_object = GetAllObjects()
    get_all_object.get_all_objects(DEFAULT_SELLER_ID)
    delete_obj = DeleteObj()
    for obj in get_all_object.response_json:
        delete_obj.del_obj(obj['id'])
    create_obj = CreateObj()
    ids = []
    for payload in get_all_from_seller_payload:
        create_obj.create_obj(payload=payload)
        create_obj.check_200()
        ids.append(create_obj.response_json['status'].split()[3])
        time.sleep(0.5)
    time.sleep(1)
    yield ids
    
    for id in ids:

        delete_obj.del_obj(id)
        delete_obj.check_200()
