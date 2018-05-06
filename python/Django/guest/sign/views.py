# Django的视图文件，控制向前端页面显示的内容

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# 从sign应用中导入models中的Event类
from sign.models import Event
from sign.models import Guest
# 导入嘉宾管理分页器
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 若查询对象不存在，则抛出http404异常
from django.shortcuts import get_object_or_404
# 获取数据表对象列表的方法，该方法会返回查询数据结果列表，如果没有查询到指定数据就返回404错误页面；
from django.shortcuts import get_list_or_404


# Create your views here.
# def index(request):
#     return HttpResponse("Hello Django!")


def index(request):
    return render(request,"index.html")

'''
# V1.0登陆动作 P41
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') #此处对应表单的form中的input的 name属性
        password = request.POST.get('password', '')
        if username == 'admin' and  password == 'admin123':
            return HttpResponse('login success!')   #通过HTttpResponse类返回字符串
        else :
            return render(request,'index.html', {'error':'username or password error!'})    #返回错误提示的字典{Key:Value}，在index里面添加{error}显示的位置
'''


'''
# V2.0登陆动作 P43
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') #此处对应表单的form中的input的name属性
        password = request.POST.get('password', '')
        if username == 'admin' and  password == 'admin123':
            return  HttpResponseRedirect('/event_manage/')  #对路径重定向，成功登陆之后重新指向 /event_manage/ 页面
        else:
            return render(request,'index.html', {'error':'username or password error!'})  
    else  render(request,'index.html', {'error':'username or password error!'})
# V2.0发布会管理 
def event_manage(request):
    return render(request,"event_manage.html")
'''


'''# V3.0登陆动作 P45
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') #此处对应表单的form中的input的name属性
        password = request.POST.get('password', '')
        if username == 'admin' and  password == 'admin123':
            # return HttpResponse('login success!')     #V1.0
            # return  HttpResponseRedirect('/event_manage/')    #v2.0
            response = HttpResponseRedirect('/event_manage/')    #对路径重定向，成功登陆之后重新指向 /event_manage/ 页面
            response.set_cookie('user', username, 3600)     #添加浏览器cookie,3600的cookie保存时间
            return  response
        else :
            return render(request,'index.html', {'error':'username or password error!'})
# V3.0发布会管理 
def event_manage(request):
    username = request.COOKIES.get('user', '')  #读取浏览器cookie
    return render(request,"event_manage.html", {"user": username})
'''


'''
# V4.0登陆动作 P47
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') #此处对应表单的form中的input的name属性
        password = request.POST.get('password', '')
        if username == 'admin' and  password == 'admin123':
            # return HttpResponse('login success!')     V1.V3.0
            # return  HttpResponseRedirect('/event_manage/')    V2.0
            response = HttpResponseRedirect('/event_manage/')   # V3.0 V4.0
            # response.set_cookie('user', username, 3600)   # V3.0 添加浏览器cookie,3600的cookie保存时间
            request.session['user'] = username  # v4.0 将session信息记录到浏览器
            return  response
        else :
            return render(request,'index.html', {'error':'username or password error!'})
# V4.0发布会管理
def event_manage(request):
    # username = request.COOKIES.get('user', '')  # V3.0读取浏览器cookie
    username =  request.session.get('user','')    # V4.0读取浏览器session   
    return render(request,"event_manage.html", {"user": username})
'''

'''
# V5.0登陆动作 P50
#引用Django认证登陆动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # 此处对应表单的form中的input的name属性
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user) #登陆
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
# V5.0发布会管理
@login_required #需要import后使用，限制某个视图才能登录
def event_manage(request):
    # username = request.COOKIES.get('user', '')    # V3.0读取浏览器cookie
    username =  request.session.get('user','')      # V4.0读取浏览器session   
    return render(request,"event_manage.html", {"user": username})
'''

# V6.0登陆动作 P50
#引用Django认证登陆动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # 此处对应表单的form中的input的name属性
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user) #登陆
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
# V6.0发布会管理 P74
@login_required #需要import后使用，限制某个视图才能登录 from django.contrib.auth.decorators import login_required
def event_manage(request):
    # 增加发布会列表
    event_list = Event.objects.all()    #sign.models中的event，查询所有发布会对象的数据，通过render（）方法附加在event_manage.html页面返回给客户端
    username =  request.session.get('user','')      # V4.0读取浏览器session   
    return render(request,"event_manage.html", {"user": username,"events":event_list})


# 发布会名称搜索 P79
@login_required
def search_name(request):
    # 读取浏览器Session
    username = request.session.get('user', '')
    # 通过get()方法获取name关键字
    search_name = request.GET.get("name", "")
    # 在Event中匹配name字段
    event_list = Event.objects.filter(name__contains=search_name)
    # 将匹配到的发布会列表注意这里是列表不是对象，返回给客户端
    # render方法接收第三个参数是后台返回给浏览器的数据，它是一个字典。
    # user，events 是你自定义的指针名字，会被对应的html文件应用（即event_manage）
    return render(request, "event_manage.html", {"user": username,"events":event_list})

'''
# 创建guest_manage视图函数 P82
# V1.0嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html",{"user":username,"guests":guest_list})
# V1.0嘉宾手机号搜索 P83
@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    return render(request, "guest_manage.html", {"user": username, "guests":guest_list})
'''

# 创建guest_manage视图函数 P85
# V2.0嘉宾管理,添加分页器
@login_required
def guest_manage(request):
    username = request.session.get('user','')
    # guest_list = Guest.objects.all()  #会报错UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list
    guest_list = Guest.objects.get_queryset().order_by('id')
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page 不是整数，取第一页面
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page 不在范围内，取最后页面
        contacts = paginator.page(Paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username,"guests":contacts})

# V2.0嘉宾手机号搜索 P83
@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    # guest_list = Guest.objects.filter(phone__contains=search_phone)    #会报错UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list
    guest_list = Guest.objects.get_queryset().order_by('id').filter(phone__contains=search_phone)
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page 不是整数，取第一页面
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page 不在范围内，取最后页面
        contacts = paginator.page(Paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username,"guests":contacts, "search_phone": search_phone})

'''
# V1.0签到页面 P89
@login_required
def sign_index(request, eid):
    username = request.session.get('user', '')    # 增加用户身份信息
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {"user": username, "event": event})

# V1.0签到动作 P91
@login_requiredV1.0
def sign_index_action(request, eid):
    username = request.session.get('user', '')    # 增加用户身份信息
    event = get_object_or_404(Event, id=eid)                   # 还是利用get_object_or_404()方法通过eid获取对应发布会，没有就报404异常
    phone = request.POST.get('phone', '')                      # 利用request的POST请求获取用户输入的手机号
    print (phone)
    # 根据用户输入的手机号查询在Guest表中的记录
    # 如果用户输入的手机号在Guest表不存在，则提示用户“phone error.”              
    result = Guest.objects.filter(phone=phone)   
    if not result:                                             
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})

    # 通过用户输入的手机号和对应的发布会id查找Guest表，则说明手机号与发布会不匹配，提示用户“event id or phone error.”
    result = Guest.objects.filter(phone=phone, event_id=eid)   
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})

    # 通过用户输入的手机号和发布会id获取数据对象
    # 从数据对象中获取sign字段的值，如果为真（1），则说明嘉宾已经签到过了，提示用户“user has sign in.” 
    result = Guest.objects.get(phone=phone, event_id=eid)   
    if result.sign:                                         
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has sign in.'})
     # 否则，说明嘉宾未签到，修改签到状态为1并提示用户“sign in success”，同时显示嘉宾的姓名和手机号
    else:                                                  
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'user': username, 'event': event, 'hint': 'sign in success!', 'guest': result})
'''

# V2.0签到页面，显示签到嘉宾数
@login_required
def sign_index(request, eid):
    username = request.session.get('user', '')    # 增加用户身份信息
    event = get_object_or_404(Event, id=eid)
    # guest_list = len(get_list_or_404(Guest, event_id=eid))
    # guest_sign = len(get_list_or_404(Guest, event_id=eid, sign=1))
    guest_list = len(Guest.objects.filter(event_id=eid))
    guest_sign = len(Guest.objects.filter(event_id=eid, sign=1))
    return render(request, 'sign_index.html', {"user": username, "event": event, 'guest_list': guest_list, 'guest_sign': guest_sign})

# V2.0签到动作 P91
@login_required
def sign_index_action(request, eid):
    username = request.session.get('user', '')    # 增加用户身份信息
    event = get_object_or_404(Event, id=eid)                   # 还是利用get_object_or_404()方法通过eid获取对应发布会，没有就报404异常
    # guest_list = len(get_list_or_404(Guest, event_id=eid))
    # guest_sign = len(get_list_or_404(Guest, event_id=eid, sign=1))
    guest_list = len(Guest.objects.filter(event_id=eid))
    guest_sign = len(Guest.objects.filter(event_id=eid, sign=1))
    phone = request.POST.get('phone', '')                      # 利用request的POST请求获取用户输入的手机号
    print (phone)
    # 根据用户输入的手机号查询在Guest表中的记录
    # 如果用户输入的手机号在Guest表不存在，则提示用户“phone error.”              
    result = Guest.objects.filter(phone=phone)   
    if not result:                                             
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.', 'guest_list': guest_list, 'guest_sign': guest_sign})

    # 通过用户输入的手机号和对应的发布会id查找Guest表，则说明手机号与发布会不匹配，提示用户“event id or phone error.”
    result = Guest.objects.filter(phone=phone, event_id=eid)   
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.', 'guest_list': guest_list, 'guest_sign': guest_sign})

    # 通过用户输入的手机号和发布会id获取数据对象
    # 从数据对象中获取sign字段的值，如果为真（1），则说明嘉宾已经签到过了，提示用户“user has sign in.” 
    result = Guest.objects.get(phone=phone, event_id=eid)   
    if result.sign:                                         
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has sign in.', 'guest_list': guest_list, 'guest_sign': guest_sign})
     # 否则，说明嘉宾未签到，修改签到状态为1并提示用户“sign in success”，同时显示嘉宾的姓名和手机号
    else:                                                  
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'user': username, 'event': event, 'hint': 'sign in success!', 'guest': result, 'guest_list': guest_list, 'guest_sign': guest_sign})


# V1.0退出登陆 P94
@login_required
def logout(request):
    # 退出登录
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response




