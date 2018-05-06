import requests
import unittest

''' 测试 发布会接口
# 查询发布会接口 P168
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid':'1'})
result = r.json()   #将接口返回的 json格式的数据 转化为 字典

# 断言接口返回值
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "红米发布会"
assert result['data']['address'] == 'CQ'
assert result['data']['start_time'] == '2017-12-30T09:00:00'    #时间后面需要加 T
'''

class GetEventListTest(unittest.TestCase):
    ''' 查询发布会接口'''

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_error(self):
        '''发布会id 不存在'''
        r = requests.get(self.url, params={'eid':'888'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')
    
    def test_event_success(self):
        '''发布会ID为1， 查询成功'''
        r = requests.get(self.url, params={'eid':'1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'], '红米发布会')
        self.assertEqual(result['data']['address'], 'CQ')
        # self.assert result['data']['address'] == 'CQ' 无法执行的
        self.assertEqual(result['data']['start_time'], '2017-12-30T09:00:00')



if __name__ == '__main__':
    unittest.main()