f = open("guests.txt", "w")

for i in range(1, 3001):
    str_i = str(i)
    realname = "rose" + str_i
    phone = xxxx + i
    email = "rose" + str_i +"@mail.com"
    sql = 'INSERT INTO sign_guest(realname, phone, email, sign, event_id) VALUES (" '+realname+' ", '+str(phone)+', "'+email+'", 0 ,1);'

    f.write(sql)
    f.write("\n")


f.close()
