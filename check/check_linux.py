# encoding:utf-8

import check.checklog as checklog
from utils.tools import mysql_exec,now,clear_table,archive_table
from check.linux_stat import LinuxStat
from utils.linux_base import LinuxBase

from __future__ import print_function
import sys
import libvirt
import time
from xml.etree import ElementTree

def getDomainMemUsed(dom_mem_stats):
    free_mem = float(dom_mem_stats['actual']) / 1024.0
    total_mem = float(dom_mem_stats['available']) / 1024.0
    used_mem = total_mem - free_mem
    print('     Memory:' + str(round(used_mem, 1)) + 'M(' + str(
        round((used_mem / total_mem) * 100.0, 1)) + '%) ' + 'of' + str(round(total_mem, 1)) + 'M')


def getDomainCPUInfo(dom):
    # get time of cpu and real time
    ti = dict()
    ti['t'] = time.time()
    dominfo = dom.info()
    ti['ct'] = dominfo[4]
    # print('CPU:')
    # for a in dominfo:
    #    print(str(a),end=' ')
    # for k in ti:
    #    print(k)
    return ti


def getDomainCPUUsed(dom):
    tl = getDomainCPUInfo(dom)
    time.sleep(0.5)
    t = getDomainCPUInfo(dom)
    cpu_diff = (t['ct'] - tl['ct']) / 100000.0
    real_diff = 109.0 * (t['t'] - tl['t'])
    CPUUsed = 1.0 * cpu_diff / real_diff
    print('     CPU:' + str(round(CPUUsed, 1)) + '%')


def getDomainNetork(dom):
    print(dom.XMLDesc())
    tree = ElementTree.fromstring(dom.XMLDesc())
    # print(1)
    ifaces = tree.findall('devices/interface/target')
    # ifs = AD.interfaceStats('vnet0')
    for i in ifaces:
        iface = i.get('dev')
        tl = time.time()
        ifaceinfo = dom.interfaceStats(iface)
        rx_bl = ifaceinfo[0]
        tx_bl = ifaceinfo[4]
        # print(str(iface)+'ifo'+str(ifaceinfo))
        time.sleep(1)
        t = time.time()
        ifaceinfo = dom.interfaceStats(iface)
        rx_b = ifaceinfo[0]
        tx_b = ifaceinfo[4]
        # print(str(iface)+'ifo'+str(ifaceinfo))
        rx_v = (rx_b - rx_bl) / (t - tl) * 1.0
        tx_v = (tx_b - tx_bl) / (t - tl) * 1.0
        print('     Down:' + str(round(rx_v, 1)) + 'b/s    Up:' + str(round(tx_v, 1)) + 'b/s')
        print('     Total received: ' + str(round((ifaceinfo[0] / 1024.0), 1)) + 'KiB   Total Sent: ' + str(
            round((ifaceinfo[4] / 1024.0), 1)) + 'KiB')


def getDomainDisk(dom):
    tree = ElementTree.fromstring(dom.XMLDesc())
    devices = tree.findall('devices/disk/target')
    # ifs = AD.interfaceStats('vnet0')
    for d in devices:
        device = d.get('dev')
        tl = time.time()
        # devstat = dom.blockStats(device)
        devst = dom.blockStatsFlags(device, 0)
        rd_bl = devst['rd_total_times']
        wr_bl = devst['wr_total_times']
        time.sleep(1)
        t = time.time()
        # devstat = dom.blockStats(device)
        devst = dom.blockStatsFlags(device, 0)
        # for d in devstat:
        #   print(d)
        rd_b = devst['rd_total_times']
        wr_b = devst['wr_total_times']
        rd_v = (rd_b - rd_bl) / (t - tl)
        wr_v = (wr_b - wr_bl) / (t - tl)

        devinfo = dom.blockInfo(device, 0)
        # for d in devinfo:
        #    print(d)
        print('     Disk Read: ' + str(round(rd_v, 1)) + 'b/s    Write:' + str(round(wr_v, 1)) + 'b/s')
        print('     Disk Total: ' + str(round((devinfo[0] / 1024.0) / 1024.0 / 1024.0, 1)) + 'GB   Used: ' + str(
            round(((devinfo[2] / 1024.0) / 1024.0) / 1024.0, 1)) + 'GB')
def getDomainOs(dom):
    root = ElementTree.fromstring(dom.XMLDesc())
    print(dom.XMLDesc())
    print(root.tag, ":", root.attrib)
    for child in root:
        print(child.tag, ":", child.attrib)
        for children in child:
            print(children.tag, ":", children.attrib)

if __name__ == "__main__":
    conn = libvirt.open('xen:///') #connect
    if conn == None:
        print('Failed to open connection to xen:///', file=sys.stderr)
        exit(1)
    # try:
    #     dom0 = conn.lookupByName("Domain-0")
    # except:
    #     print ('Failed to find the main domain')
    #     exit(1)
    # print ("Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType()))
    # print (dom0.info())

    AllDomains = conn.listAllDomains(1)
    n = 1;
    for AD in AllDomains:
        print("domain" + str(n) + ': ' + AD.name() + '  ', end='')
        if AD.ID() == -1:
            print('shutdown')
        else:
            print(str(AD.ID()))
            # getDomainMemUsed(AD.memoryStats())
            # getDomainCPUUsed(AD)
            # getDomainNetork(AD)
            # getDomainDisk(AD)
            getDomainOs(AD)
        n = n + 1

    conn.close()
    exit(0)
def check_linux(linux_params):
    conn = libvirt.open('xen:///') #connect
    if conn == None:
        print('Failed to open connection to xen:///', file=sys.stderr)
        exit(1)
    # try:
    #     dom0 = conn.lookupByName("Domain-0")
    # except:
    #     print ('Failed to find the main domain')
    #     exit(1)
    # print ("Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType()))
    # print (dom0.info())
    AllDomains = conn.listAllDomains(1)
    n = 1;
    for AD in AllDomains:
        # print_function("domain" + str(n) + ': ' + AD.name() + '  ', end='')
        if AD.ID() == -1:
            print('shutdown')
            exit(1)
        elif AD.name()==linux_params:
            print(str(AD.ID()))
            # getDomainMemUsed(AD.memoryStats())
            # getDomainCPUUsed(AD)
            # getDomainNetork(AD)
            # getDomainDisk(AD)
            getDomainOs(AD)
        n = n + 1
    conn.close()

# def check_linux(tags,linux_params):
#     check_time = now()
#     host = linux_params['hostname']
#     port = linux_params['port']
#     # create connection
#     linux_conn, _ = LinuxBase(linux_params).connection()
#     if linux_conn:
#         checklog.logger.info('{}:开始获取Linux主机监控信息' .format(tags))
#         # get linuxstat data
#         linuxstat = LinuxStat(linux_params, linux_conn).get_linux()
#         hostinfo = linuxstat['hostinfo']
#         cpuinfo = linuxstat['cpuinfo']
#         memtotal = linuxstat['Memtotal']
#         ipinfo = linuxstat['ipinfo']
#         load = linuxstat['load']
#         cpustat = linuxstat['cpu']
#         iostat = linuxstat['iostat']
#         memstat = linuxstat['mem']
#         vmstat = linuxstat['vmstat']
#         tcpstat = linuxstat['tcpstat']
#         netstat = linuxstat['net']
#         procstat = linuxstat['proc']
#
#         # total network in/out
#         recv_kbps = round(sum([d['recv'] for d in netstat]),2)
#         send_kbps = round(sum([d['send'] for d in netstat]),2)
#         # total io
#         read_mb = round(sum([d['rd_m_s'] for d in iostat]),2)
#         write_mb = round(sum([d['wr_m_s'] for d in iostat]),2)
#         iops = round(sum([d['io_s'] for d in iostat]),2)
#         # cpu used percent
#         cpu_used = round(100 - cpustat['cpu_idle'], 2)
#         # memory used percent
#         mem_used = round((float(memstat['mem_used_mb']) / (float(memtotal['memtotal']) / 1024)) * 100, 2)
#
#         insert_data_values = {**locals(), **hostinfo, **cpuinfo, **memtotal, **ipinfo, **load, **cpustat, **memstat,
#                               **vmstat, **tcpstat, **procstat}
#
#         insert_data_sql = "insert into linux_stat(tags,host,port,hostname,ipinfo,linux_version,updays,kernel,frame,cpu_mode,cpu_cache,processor,cpu_speed," \
#                           "recv_kbps,send_kbps,load1,load5,load15,cpu_sys,cpu_iowait,cpu_user,cpu_used,memtotal,mem_used,mem_cache,mem_buffer,mem_free,mem_used_mb," \
#                           "swap_used,swap_free,swapin,swapout,pgin,pgout,pgfault,pgmjfault,tcp_close,tcp_timewait,tcp_connected,tcp_syn,tcp_listen,iops,read_mb,write_mb," \
#                           "proc_new,proc_running,proc_block,intr,ctx,softirq,status,check_time) " \
#                           "values ('{tags}','{host}',{port},'{hostname}','{ipinfo}','{linux_version}',{updays},'{kernel}','{frame}','{cpu_mode}','{cpu_cache}','{processor}','{cpu_speed}'," \
#                           "{recv_kbps},{send_kbps},{load1},{load5},{load15},{cpu_sys},{cpu_iowait},{cpu_user},{cpu_used},{memtotal},{mem_used},{mem_cache},{mem_buffer},{mem_free},{mem_used_mb}," \
#                           "{swap_used},{swap_free},{swapin},{swapout},{pgin},{pgout},{pgfault},{pgmjfault},{tcp_close},{tcp_timewait},{tcp_connected},{tcp_syn},{tcp_listen},{iops},{read_mb},{write_mb}," \
#                           "{proc_new},{proc_running},{proc_block},{intr},{ctx},{softirq},0,'{check_time}')"
#
#         clear_table(tags,'linux_stat')
#         insert_sql = insert_data_sql.format(**insert_data_values)
#         mysql_exec(insert_sql)
#         archive_table(tags,'linux_stat')
#
#         # disk free
#         clear_table(tags,'linux_disk')
#         diskfree_list = LinuxStat(linux_params, linux_conn).get_diskfree()
#         for each in diskfree_list:
#             dev, total_size, used_size, free_size, used_percent, mount_point = each
#             used_percent = float(used_percent.replace('%',''))
#             insert_data_sql = '''insert into linux_disk(tags,host,dev,total_size,used_size,free_size,used_percent,mount_point,check_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
#             values = (tags, host, dev, round(float(total_size) / 1024, 2), round(float(used_size) / 1024, 2),
#                       round(float(free_size) / 1024, 2), used_percent, mount_point, now())
#             mysql_exec(insert_data_sql, values)
#         archive_table(tags,'linux_disk')
#
#         # io stat
#         clear_table(tags,'linux_io_stat')
#         for each in iostat:
#             insert_data_sql = "insert into linux_io_stat(tags,host,dev,rd_s,rd_avgkb,rd_m_s,rd_mrg_s,rd_cnc,rd_rt,wr_s,wr_avgkb,wr_m_s,wr_mrg_s,wr_cnc,wr_rt,busy,in_prg,io_s,qtime,stime,check_time)" \
#                               " values ('{tags}','{host}','{dev}',{rd_s},{rd_avgkb},{rd_m_s},{rd_mrg_s},{rd_cnc},{rd_rt},{wr_s},{wr_avgkb},{wr_m_s},{wr_mrg_s},{wr_cnc},{wr_rt},{busy},{in_prg},{io_s},{qtime},{stime},'{check_time}')"
#             insert_data_values = {**locals(), **each}
#             insert_sql = insert_data_sql.format(**insert_data_values)
#             mysql_exec(insert_sql)
#         archive_table(tags,'linux_io_stat')
#     else:
#         error_msg = "{}:linux主机连接失败" .format(tags)
#         checklog.logger.error(error_msg)
#         checklog.logger.info('{}:写入linux_stat采集数据'.format(tags))
#         clear_table(tags,'linux_stat')
#         sql = "insert into linux_stat(tags,host,port,status,check_time) values('{tags}','{host}',{port},1,'{check_time}')"
#         sql = sql.format(**locals())
#         mysql_exec(sql)
#         archive_table(tags,'linux_stat')

if __name__ == '__main__':
    print(now())




