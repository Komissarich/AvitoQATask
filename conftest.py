import pytest
from endpoints.create_obj import CreateObj
from endpoints.del_obj import DeleteObj
from tests.test_data.results import *
from tests.test_data.payloads import *



@pytest.fixture
def obj_id():
    create_obj = CreateObj()
    create_obj.create_obj(payload=fixture_payload)
    create_obj.check_200()
    id = create_obj.response_json['status'].split()[3]
    yield id
    delete_obj = DeleteObj()
    delete_obj.del_obj(id=id)
    delete_obj.check_200()


@pytest.fixture
def seller_id():
    return DEFAULT_SELLER_ID


@pytest.fixture
def many_obj_ids():
    create_obj = CreateObj()
    ids = []
    for payload in get_all_from_seller_payload:
        create_obj.create_obj(payload=payload)
        create_obj.check_200()
        ids.append(create_obj.response_json['status'].split()[1])
    yield ids
    delete_obj = DeleteObj()
    for id in ids:
        delete_obj.del_obj(id=id)
        delete_obj.check_200()
