# @Author : TongTong

import pytest
from wwork_api_interface_test.api.member import Member
from wwork_api_interface_test.api.wework import Wework

# 获取token值和联系人对象，但token并没使用配置文件获取
secret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
token = Wework().get_token(secret)
member = Member()

# 冒烟测试的前后置
@pytest.fixture(scope="session")
def test_all_pre_data():
    pre_add_list = [
        ["tongtong1", "tongtong1", "13112661165"],
        ["tongtong2", "tongtong2", "13122661165"],
        ["tongtong3", "tongtong3", "13132661165"],
        ["tong1234"]
    ]
    for i in range(len(pre_add_list)):
        if i <= 2:
            member.add_member(token, pre_add_list[i][0], pre_add_list[i][1], pre_add_list[i][2])
        else:
            member.delete_member(token, pre_add_list[i][0])


# add接口的数据准备
@pytest.fixture(scope="session")
def add():
    member.multi_delete_member(token, ["tong", "tong5"])


# delete接口的数据准备
@pytest.fixture(scope="session")
def delete():
    member.add_member(token, "delete", "delete", "13172222165")


# edit接口的数据准备
@pytest.fixture(scope="session")
def edit():
    member.add_member(token, "edit", "name", "13172669999")


# multi_delete接口的数据准备
@pytest.fixture(scope="session")
def multi_delete():
    member.add_member(token, "delete1", "delete1", "13172669998")
    member.add_member(token, "delete2", "delete2", "13172669997")
    member.add_member(token, "delete3", "delete3", "13172669996")


# get接口的数据准备
@pytest.fixture(scope="session")
def get():
    member.add_member(token, "get", "get", "13172669995")
