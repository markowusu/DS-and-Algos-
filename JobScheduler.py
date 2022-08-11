# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

class Solution:
    def job_scheduler(self,schedule_job,sec):
        print(f'This will be done in {sec} milliseconds')
        time.sleep(sec/1000)
        schedule_job()

if __name__ == '__main__':
    secs = int(input())
    
    def schedule_job():
        print(f'processid : 2343')

    solution = Solution()
    solution.job_scheduler(schedule_job,secs)  
