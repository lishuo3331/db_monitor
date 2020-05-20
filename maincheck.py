# encoding:utf-8

from check.check_linux import check_linux

from check.alarm import check_alarm
from utils.tools import clear_table,archive_table,mysql_query
from multiprocessing import Process

if __name__ == '__main__':
    # all minitoring servers
    linux_list = mysql_query('select adname from linux_list')
    # windows_list = mysql_query('select tags,host,sshport,user,password from linux_list where system ="windows"')
    # check_linux
    check_pool = []

    if linux_list:
        for each in linux_list:
            adname = each[0]
            # linux_params = {
            #     'hostname': each[1],
            #     'port': each[2],
            #     'username': each[3],
            #     'password': each[4]
            # }
            linux_check = Process(target=check_linux, args=(adname))
            linux_check.start()
            check_pool.append(linux_check)


    for each in check_pool:
        each.join()

    # 告警
    print('maincheck')
    check_alarm()



