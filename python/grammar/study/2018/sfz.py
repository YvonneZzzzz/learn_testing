#!/usr/bin/env python
# -*- coding: utf-8 -*-

#name,phoneno,sfz,fa_phone,name_2,ki_phone,name_3,bo_phone
#哇哈哈测试,13381000002,310101198303141056,13381000003,中文名2,13381000004,中文名3,13381000005
#

import random

def main():
	global phone,sfzkt,sfz,ck,kahao
	ct = 10000
	kahao = 9843010202530433
	phone = "13470000000"	#电话号码
	sfzkt = "310283"	#身份证最开头
	sfz = "19860901001"	#身份证结尾，除最后一位
	ck = [1,0,'X',9,8,7,6,5,4,3,2]	#身份证最后一位
	#
	for n in range(0,ct):
		ctn = pho(phone)
		ctn2 = pho(phone)
		ctn3 = pho(phone)
		ctn4 = pho(phone)
		sfz1 = sf(sfz)
		#sfz2 = sf(sfz)
		kh = kaho(kahao)
		#print ctn
		#print(ctn + "," + kh + "," + sfz1)
		name = gen_name()
		name2 = gen_name()
		name3 = gen_name()

		#print(ctn + "," + sfz1 + "," + name)
		print(('%s,%s,%s,%s,%s,%s,%s,%s') % (name,ctn,sfz1,ctn2,name2,ctn3,name3,ctn4))
##
def pho(ph1):
	rt_ph = ph1
	global phone
	phone = str(int(phone) + 1)
	return rt_ph

##
def kaho(kh):
	rt_ph = kh
	global kahao
	kahao = str(int(kahao) + 1)
	while kahao.endswith('2') or kahao.endswith('4') or kahao.endswith('6') or kahao.endswith('99'):
		kahao = str(int(kahao) + 1)
	return str(rt_ph)
	
def sf(mysfz):
	global sfzkt,sfz,ck
	yy = mysfz[0:4]
	mm = mysfz[4:6]
	dd = mysfz[6:8]
	seq = mysfz[8:]
	
	cd = str(sfzkt + mysfz)
	
	tp_idx = (int(cd[0])*7+int(cd[1])*9+int(cd[2])*10+int(cd[3])*5+int(cd[4])*8+int(cd[5])*4+int(cd[6])*2+int(cd[7])*1+int(cd[8])*6+int(cd[9])*3+int(cd[10])*7+int(cd[11])*9+int(cd[12])*10+int(cd[13])*5+int(cd[14])*8+int(cd[15])*4+int(cd[16])*2)%11

	new_sfz = cd + str(ck[tp_idx])
	##
	seq = int(seq)
	dd = int(dd)
	mm = int(mm)
	yy = int(yy)
	seq += 1
	if (seq > 999):
		seq = 1
		dd += 1
	if (dd > 28):
		dd = 1
		mm += 1
	if (mm > 12):
		mm = 1
		yy += 1
	seq = "%03d" % seq
	dd = "%02d" % dd
	mm = "%02d" % mm
	
	sfz = str(yy) + str(mm) + str(dd) + str(seq)
	#print "new sfz info : " +  sfz
	return new_sfz

def gen_name():
	x = "王陈张李周杨吴黄刘徐朱胡沈潘章程方孙郑金叶汪何马赵林蒋俞姚许丁施高余谢董汤钱卢江蔡宋曹邱罗杜郭戴洪唐袁夏童肖姜傅范顾梅盛吕诸邵陆彭韩倪雷郎梁楼万龚储鲍严葛华应冯项崔魏毛阮邹喻曾邓熊任陶费凌虞裘涂苏翁莫卞史季康管黎孔田单娄宣钟饶鲁廖于韦甘石孟柳祝胥殷舒褚薛白向邬尚竺查谈贾温游谭开伍庄成沙柏郝秦尉麻詹赖裴颜尹巴乐厉谷易段钮骆笪阎缪臧樊操卜丰文水兰包平乔伊有牟邢劳来求沃芮闵欧郏柯贺闻桂耿戚符蓝路阚滕霍上卫干支牛计车左申艾仲刑匡印吉宇安戎毕池纪过佘冷时束花迟邰卓宓宗官庞於明练苗茅郁冒洑相郤郦钦奚席晋晏柴聂宿密屠常鄂惠琚窦简蒿阙穆濮"
	m = "华明芳琴红萍文丽金荣国英珍月云平美海林志玉建伟春玲晓爱秀霞燕根新凤德成敏生民小亚梅强忠军良永飞雪芬莲宝娣斌水兰祥学勇福娟峰菊青桂卫富龙贵娥莉彩兴安慧珠庆旭法艳惠群秋世有佳立家清义丹正宏炳银贤培锋中仁元香长如花才友刚利连东江洪胜君昌俊星光波顺婷一和康吉亮喜琳颖仙发杰鸣勤蓉静传欢兵振维晶辉双方礼松彬淑来涛素莹超木芸武浩道天冬巧先宗泽娜虹能善瑛鑫开加汉全远坤炎树泉珏继高鸿景为叶宇年孝寿苗虎洁益智森琼雅源鹏士山丰乐冰克杏定承绍政倩健锡锦黎耀三阳佩剑姣珊章铭瑞碧翠瑾土少行伯坚阿其奇妹怡炜南品盛菲雄意璐人久大风仲向达启时欣茂钦卿翔九广心代亦存师纪芝李灵纯苏迎秉诚奎娇显祖哲荷基珺琦熙蕾万子火以圣宁兆权竹自观贞妙怀妮育彦恒栋堂婕湘照瑜韵毓豪毅潮力之五从升太引业本田名守扬汝百妍岚男财进凯周宜放旺经雨保信娅庭思钢钧凌圆宽宾笑骏跃斐朝煜增震鹤衡艺尔申尧作园声陆卓孟昉治知祎郁钖修复威柏洲相科晋润航莎铁乾晨望梦涵象逸媛敬腊滨雷蔚磊露乃于女工书公六历日贝仕令北四石再农则吕延聿亨余呈应社芹运依姐姗季岩玥诗厚垚宣宪峥映柱炼茹贻轶容悦梧泰积耕莺谊逢铃梓渊爽绪敦淼琪登程越雁雯雲嵩满筠蓓路旗熊瑶璋聪镕薇赟鹰麟亿川允夫毛功可央幼必旦未由白伊众优伦同囡孙臣至齐吾希张改更灿甫纬芙言轩钊咏姑官宙尚岳征昇昊昕枝枫河玮迪驹亭俐俭冠奕帮挺柳标洋济珉盈省觉选闻娴展恩息晔晟桃真竞舫通钰啓堃婧寅崇晗深焕理甜绮绵绿野铨隆傅博嵘普棋渭焱然琛禄缘萱葆葱裕鼎楚筱解靖魁嘉睿韬影蕊蕴蝶儒樵镛镜霏燮繁巍懿又上巾彐门马内支斗丝主仪占古台史对巨市汀玄甲艾记丞乔争任伍伏关列在圭地多好庄扣执次池汤玎玑祁羊舟许迈位冶初助吴均妞妤孚岑序库形彤我扶抒攸材杜步求汪汶芦芽评谷身邱里际陈京佶侹典刻垂备居幸性房抱招昆昔杭枚泷玠玫现画畅空竺罗苓苔苹表视诞贯轮郑俞俨勉勋咣咸哞城姝娃将峡带度彪待总战持昱柯洼洽炯狮界畏盼眉祚禹统胤胪茗茜茶荟赴赵逊重钜钟闽音候原唐夏峻换效敖晖校桔桢桧殷流浙浦涌烈烨玺珩祯秦秩称粉致舰莞起都铎阅隽颂婉婵孰寄尉屠常庸得惊惜授敛旋曹梁涯淦烽猗猛球琅皎硕移羚辅逵铜领喆堡媚尊弼惑斯晰最棠棣植滋琨琰紫联舒舜葛装谟谦遂遇链靓鲁嫄微愚慈慎数椿楠楷楸楹槐歆殿溢溪滢煌瑀瑰盟碎蒙裘键雾颐龄嫣稳舆蔷蔺蕖蜀蜜蝉裴褔谱霆韶墀嬉慰樑樟樱潜澄澜璇稼稽豫遵醉镇镐霄题颜冀器壁操潞濒璘璞璟禧翰翱赞霖黔壑曙磻魏黛藩馥攀霭麒鑑"
	num = random.randint(1, 2)
	ln = x[random.randint(1, len(x)) - 1]
	ln2 = m[random.randint(1, len(x)) - 1]
	rn = ''
	for n in range(0, num):
		rn += m[random.randint(1, len(m)) - 1]

	return ln + ln2 + rn

if __name__ == '__main__':
    main()