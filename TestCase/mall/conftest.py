import pytest

from Common import Request, Assert

@pytest.fixture(scope="session")
def head():
    request = Request.Request()

    assertions = Assert.Assertions()
    login_resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                      json={"username": "admin", "password": "123456"})
    assertions.assert_code(login_resp.status_code, 200)
    login_resp_json = login_resp.json()
    assertions.assert_in_text(login_resp_json['message'], '成功')

    # 提取token
    data_json = login_resp_json['data']
    token = data_json['tokenHead'] + data_json['token']
    print(token)

    # 重新赋值全局变量 head

    head = {'Authorization' : token }
    return head