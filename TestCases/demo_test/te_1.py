
import pytest

login_format_data =[{'username': '13691579846', 'password': 'xiaochao1152', 'expected': '帐号或密码错误!'},\
                    {'username': '13691579846', 'password': 'xiaochao115200', 'expected': '帐号或密码错误!'}]

# @pytest.mark.parametrize("a,b,c",login_format_data)
# def test_a(a,b,c):
#     print(a,b,c)
#     print(type(a))

@pytest.mark.parametrize("data",login_format_data)
def test_a(data):
    print(data["username"],data["password"],data["expected"])



if __name__ == '__main__':
    pytest.main(["test_1.py","-s","-q"])