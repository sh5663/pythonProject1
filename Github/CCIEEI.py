import os
import random
zhengque = 0 #正确答案次数
cuowu = 0 #错误答案次数
q1 = ("Which feature is supported by EIGRP but is not supported by OSPF?\nA. route filtering\nB. unequal-cost load balancing\nC. route summarization\nD. equal-cost load balancing")
q2 = ("On which protocol or technology is the fabric data plane based in Cisco SD-Access fabric?\nA. VXLAN\nB. LISP\nC. Cisco TrustSec\nD. IS-IS")
q3 = ("Which two mechanisms are available to secure NTP? (Choose two.)\nA.IPsec\nB.IP prefix list - based\nC.encrypted authentication\nD.TACACS - based authentication\nE.IP access list - based")
q4 = ("Which technology provides a secure communication channel for all traffic at Layer 2 of the OSI model?\nA. SSL\nB. Cisco TrustSec\nC. MACsec\nD. IPsec")
q5 = ("Which two methods are used by an AP that is trying to discover a wireless LAN controller? (Choose two.)\nA. Cisco Discovery Protocol neighbor\nB. querying other APsC. DHCP Option 43\nD. broadcasting on the local subnet\nE. DNS lookup CISCO-DNA-PRIMARY.localdomain")
q6 = ('Which IP SLA operation requires the IP SLA responder to be configured on the remote end?\nA. UDP jitter\nB. ICMP jitter\nC. TCP connect\nD. ICMP echo')
que = [q1,q2,q3,q4,q5,q6]
# 题目列表
daan = {q1:'B',q2:' A',q3:'CE',q4:'C',q5:'CD',q6:'A'}
# 对应题目答案字典
for i in range(3):
    timu1 = random.choice(que) #列表中随机选择题目
    print('QUESTION',i+1,timu1)
    que.remove(timu1) #将已经选择过的题目移除放在重复
    shuru = input('输入答案:')
    if shuru.upper() == daan[timu1]: #输入的题目答案和答案字典对比是否正确
        zhengque +=1
        # print('ok')
    else:
        cuowu+=1
        # print('no')
if zhengque >=  2:
    # print('pass')
    result = 'Pass'
else:
    # print('fail')
    result = 'Fail'
inname = input('输入考试文件名称：')
with open(('E:/{}.txt'.format(inname)),'a+') as f:
    f.write('本次考试结果:')
    f.write(result)
    f.close()