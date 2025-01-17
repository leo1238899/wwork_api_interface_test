# @Author : TongTong

import pytest
from wwork_api_interface_test.api.wework import Wework
from wwork_api_interface_test.api.meeting_room import MeetingRoom
from wwork_api_interface_test.common.config import cf

# 初始化会议室对象
meeting = MeetingRoom()

# 获取token值
@pytest.fixture(scope="session")
def token():
    secret = cf.get_key("wwork", "meeting_room_secret")
    token = Wework().get_token(secret)
    return token

# 会议室冒烟测试前后置步骤
@pytest.fixture(scope="session")
def meeting_smoke(token):
    # add的前置步骤
    meeting.delete_meeting_room(token, 1)
    # edit的前置步骤
    meeting.add_meeting_room(token, "tong", 11, None, None, None, None)
    # 删除的前置步骤
    meeting.add_meeting_room(token, "tong1", 12, None, None, None, None)
    yield
    # 后置步骤
    meeting.delete_meeting_room(token, 1)
    meeting.delete_meeting_room(token, 2)
    meeting.delete_meeting_room(token, 3)
    meeting.delete_meeting_room(token, 4)
    meeting.delete_meeting_room(token, 5)
    meeting.delete_meeting_room(token, 6)
    meeting.delete_meeting_room(token, 7)
