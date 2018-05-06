# Django的单元测试类 django.test.TestCase 从 unittest.TestCase 继承而来

from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User #测试登录动作
from sign.models import Event   #测试发布会管理
from sign.models import Guest   #测试嘉宾管理


# Create your tests here.

class ModelTest(TestCase):
    '''Django的简单测试， P100'''


    # 执行setUp时，不会真正向数据表插入数据
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2017-12-21 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='allen', phone='11123', email='allen@mail.com', sign=False)
    
    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='11123')
        self.assertEqual(result.realname, 'allen')
        self.assertFalse(result.sign)


'''P100
Django专门提供了“test”命令来运行测试
python manage.py test

运行sign应用下的所有测试用例:
python manage.py test sign

运行sign应用下的 tests.py 测试文件：
python manage.py test sign.tests

运行sign 应用下 tests.py 测试文件 的 ModelTest 测试类：
python manage.py test sign.tests.ModelTest

运行sign 应用下 tests.py 测试文件 的 ModelTest 测试类 下面的 test_event_models 测试方法（用例）：
python manage.py test sign.tests.ModelTest.test_event_models

还可以使用 -p （或 --pattern ）参数模糊匹配测试文件, 匹配以“test”开头， 以“.py”结尾的测试文件，星号“*”匹配任意字符
python manage.py test -p test*.py

'''


"""P104
# P104 客户端测试，进入Django shell模式测试， python manage.py shell
from django.test.utils import setup_test_environment
# setup_test_environment用于测试前初始化测试环境
setup_test_environment()
from django.test import Client
c = Client()
response = c.get('/index/')
# 打印http返回状态码 200
response.status_code
"""

class IndexPageTest(TestCase):
    '''测试index登录首页  P105'''

    def test_index_page_renders_index_template(self):
        ''' 测试 index 视图 '''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    '''测试 登录 动作 P105'''

    def setUp(self):                                     # 初始化，调用User.objects.create_user创建登录用户数据
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_admin(self):
        '''测试添加的用户数据是否正确'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@mail.com')    # 注意这里书中有误，user表里的字段是email而不是mail，否则会报错

    def test_login_action_username_password_null(self):
        '''测试用户名密码为空'''
        test_data = {'username':'', 'password': ''}
        response = self.client.post('/login_action/', data=test_data)    # 通过post()方法请求'/login_aciton/'路径测试登录功能
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)   # assertIn()方法断言返回的HTML页面中是否包含指定的提示字符串

    def test_login_action_username_password_error(self):
        '''测试用户名密码错误'''
        test_data = {'username':'abc', 'password':'123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        '''测试登录成功'''
        test_data = {'username':'admin', 'password':'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)    # 这里为什么断言的是302，是因为登录成功后，通过HttpResponseRedirect()跳转到了'/event_manage/'路径，这是一个重定向


class EventManageTest(TestCase):
    ''' 发布会管理 P107 '''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name="xiaomi5", limit=2000, address="beijing", status=1, start_time="2017-12-12 12:30:00")
        self.login_user = {'username':'admin', "password":"admin123456"}
    
    def test_event_manage_success(self):
        '''测试发布会：xiaomi5 '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_event_manage_search(self):
        ''' 测试发布会搜索  '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {"name":"xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)


class GuestManageTest(TestCase):
    """测试嘉宾管理 P108"""

    def setUp(self):
        '''还是使用setUp初始化一些测试数据'''
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2017-08-10 12:30:00')
        Guest.objects.create(realname='alen', phone=18611001100, email='alen@mail.com', sign=0, event_id=1)
        self.login_user = {'username':'admin', 'password':'admin123456'}

    def test_event_manage_success(self):
        '''测试嘉宾信息：alen'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'18611001100', response.content)

    def test_guest_manage_search_success(self):
        '''测试嘉宾搜索功能'''
        response = self.client.post('/login_action/', data=self.login_user)
        # 这里就是坑了，我们根据书中描述一步一步来得话，我们在views.py里定义的搜索功能是根据名字来搜索的，而不是根据手机号，下面应该修改为('/search_realname/', {'realname':'alen'})
        response = self.client.post('/search_phone/', {'phone':'18611001100'})
        # response = self.client.post('/search_realname/', {'realname':'alen'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'18611001100', response.content)

class SignIndexActionTest(TestCase):
    """测试发布会签到 P109"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=2000, address='shenzhen', status=1, start_time='2017-6-10 12:30:00')
        Guest.objects.create(realname="alen", phone=18611001100, email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone=18611011101, email='una@mail.com', sign=1, event_id=2)
        self.login_user = {'username':'admin', 'password':'admin123456'}

    def test_event_models(self):
        '''测试添加的发布会数据'''
        result1 = Event.objects.get(name='xiaomi5')
        self.assertEqual(result1.address, 'beijing')
        self.assertTrue(result1.status)
        result2 = Event.objects.get(name='oneplus4')
        self.assertEqual(result2.address, 'shenzhen')
        self.assertTrue(result2.status)

    def test_guest_models(self):
        '''测试添加的嘉宾数据'''
        result = Guest.objects.get(realname='alen')
        self.assertEqual(result.phone, '18611001100')
        self.assertEqual(result.event_id, 1)
        self.assertFalse(result.sign)

    def test_sign_index_action_phone_null(self):
        '''测试手机号为空'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {"phone":""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        '''测试手机号或发布会id错误'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/2/', {"phone":"18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_sign_index_action_user_sign_has(self):
        '''测试嘉宾已签到'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/2/', {"phone":"18611011101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_sign_index_action_sign_success(self):
        '''测试嘉宾签到成功'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {"phone":"18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)