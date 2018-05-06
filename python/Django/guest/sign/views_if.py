# 增加发布会接口 

from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
import time
# from views_if import user_auth


# 添加发布会接口   P130
def add_event(request):
    eid = request.POST.get('eid', '')   #发布会id
    name = request.POST.get('name', '') #发布会标题
    limit = request.POST.get('limit', '')   #限制人数
    status = request.POST.get('status', '') #状态（非必填）
    address = request.POST.get('address', '')   #地址
    start_time = request.POST.get('start_time', '') #发布会时间（格式：2017-12-31 12:00:00）

    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})  #JsonResponse可以将字典转化成JSON格式

    result =Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023, 'message':'event name already exists'})

    if status == '':    #发布会状态不是必填状态，若发布会状态为 空 ，则将状态设置为 1 （true，开启）
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address, status=int(status), start_time=start_time)    #将数据插入Event表
    except ValidationError :
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024, 'message':error})

    return JsonResponse({'status':200, 'message':'add event success'})


# 添加嘉宾接口    P135
def add_guest(request):
    eid = request.POST.get('eid', '')   #关联发布会id
    realname = request.POST.get('realname', '') #姓名
    phone = request.POST.get('phone', '')   #手机号
    email = request.POST.get('email', '')   #邮箱

    if eid == '' or realname == '' or phone == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})

    result = Event.objects.filter(id=eid)   #判断发布会的id 是否存在
    if not result:
        return JsonResponse({'status':10022, 'message':'event id null'})

    result = Event.objects.get(id=eid).status   #关联的发布会状态是否为True（1），并返回相应的状态码和提示信息
    if not result:
        return JsonResponse({'status':10023, 'message':'event status is not available'})

    event_limit = Event.objects.get(id=eid).limit   #发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)    #发布会已添加的嘉宾数

    if len(guest_limit) >= event_limit: 
        return JsonResponse({'status':10024, 'message':'event number is full'})

    event_time = Event.objects.get(id=eid).start_time     # 发布会时间
    timeArray = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time()) #当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)

    if n_time >= e_time:    #判断当前时间 是否大于 发布会 时间， 若已经开始了就不能进行添加 嘉宾
        return JsonResponse({'status':10025, 'message':'event has started'})

    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email, sign=0, event_id=int(eid))   #插入嘉宾数据
    except IntegrityError:
        return JsonResponse({'status':10026, 'message':'the event guest phone number repeat'})  #如果嘉宾phone 已经存在， 则提示信息

    return JsonResponse({'status':200, 'message':'add guest success'})


# 查询发布会接口   P132
def get_event_list(request):
    eid = request.GET.get("eid", "")    #发布会id
    name = request.GET.get("name", "")  #发布会名称

    if eid == '' and name == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})

    if eid != '':   #如果发布会id（eid）不为空，则优先使用发布会id查询，因为id具有唯一性
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
	        # event['eid'] = result.id
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data':event})  #将查询结果以字典形式放到定义的evetn中，并将event作为 接口返回字典中data对应的值

    if name != '':
        datas = []
        results = Event.objects.filter(name__contains=name) #模糊查询，查询数据可能会有多条，返回的数据格式会稍显复杂
        if results:
            for r in results:
                event = {}
                # event['eid'] = r.id
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time  #首先将查询的每一条数据放到一个event字典中
                datas.append(event)                 #再把每个even 字典 放到 datas 数据中
            return JsonResponse({'status':200, 'message':'success', 'data':datas})  #最后将整个datas数组作为接口返回字典中 data 对应的值
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})




# 查询嘉宾接口 P135
def get_guest_list(request):
    eid = request.GET.get("eid", "")       # 关联发布会id
    phone = request.GET.get("phone", "")   # 嘉宾手机号

    if eid == '':
        return JsonResponse({'status':10021,'message':'eid cannot be empty'})

    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone,event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200, 'message':'success', 'data':guest})

# 嘉宾签到接口 P137
def user_sign(request):
    eid =  request.POST.get('eid','')       # 发布会id
    phone =  request.POST.get('phone','')   # 嘉宾手机号

    if eid =='' or phone == '':
        return JsonResponse({'status':10021,'message':'parameter error'})

    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status':10022,'message':'event id null'})

    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status':10023,'message':'event status is not available'})

    event_time = Event.objects.get(id=eid).start_time     # 发布会时间
    timeArray = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time()) #当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)

    if n_time >= e_time:
        return JsonResponse({'status':10024, 'message':'event has started'})

    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status':10025, 'message':'user phone null'})

    result = Guest.objects.filter(event_id=eid, phone=phone)
    if not result:
        return JsonResponse({'status':10026, 'message':'user did not participate in the conference'})

    result = Guest.objects.get(event_id=eid,phone=phone).sign
    if result:
        return JsonResponse({'status':10027,'message':'user has sign in'})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return JsonResponse({'status':200, 'message':'sign success'})