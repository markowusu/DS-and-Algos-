# import os 
from datetime import timedelta  
from datetime import datetime
import time 

# with open('Devleap_exam.log','r') as fptr:
#     log_line = fptr.readline().rstrip()
#     print(log_line)
    
keyword_count = 0 
keyword_init_count = 0
keyword_ = ['begin', 'end'] 
begin_trans =0 
end_trans = 0 
time_list = []
trans_id =[]

with open('Devleap_exam.log','r') as fptr:
    for log_line in fptr:
        resulting_log =list(map(str,log_line.rstrip().split()))
        if keyword_[0] in resulting_log:
            begin_trans = resulting_log[1]
            print(str(begin_trans),'start')
        if keyword_[1] in resulting_log:
            end_trans = resulting_log[1]
            trans_id.append(resulting_log[7])
            print(int(str(end_trans[0:2]))-int(str(begin_trans[0:2])))
            hr_diff = int(str(end_trans[0:2]))-int(str(begin_trans[0:2]))
            min_diff=(int(str(end_trans[3:5])) - int(str(begin_trans[3:5])))
            second_diff = (float(str(end_trans[6:]))- float(str(begin_trans[6:])))
            time_list.append(round(float(hr_diff+min_diff+second_diff)*1000))
print(max(time_list),"maximum transaction time")
min_trans = min(time_list)
print(min(time_list),"Minimum transaction time")
print(trans_id[time_list.index(min_trans)],"transcation id for minimum time of transaction")
print(sum(time_list)//len(time_list), "The average time for the transactions")
print("A list of all time values of transaction{}".format(time_list))  



















# with open('Devleap_exam.log','r') as fptr:
#     for log_line in fptr:
#         resulting_log =list(map(str,log_line.rstrip().split()))
#         if keyword_[0] == resulting_log[2]:
#             # print(log_line)
#             keyword_count=keyword_count +1 

# print("The number of errors in the log file is {}".format(keyword_count))        


# with open('Devleap_exam.log','r') as fptr:
#     for log_line in fptr:
#         resulting_log =list(map(str,log_line.rstrip().split()))
#         if keyword_[0] in resulting_log:
#             # print(log_line)
#             keyword_init_count=keyword_init_count +1 

# print("The number of errors in the log file is {}".format(keyword_init_count))   


