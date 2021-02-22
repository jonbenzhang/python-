# -*- coding: utf-8 -*-
# Time: 2018/10/13 19:01:30
# File Name: ex_interval.py

from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def tick():
    print('Tick! The time is: %s' % datetime.now())


def tick2():
    print('Tick2! The time is: %s' % datetime.now())


def a_interval():
    # 每隔3秒执行一次
    scheduler.add_job(tick, 'interval', seconds=3)


def a_corn():
    # hour=19, minute=23 每天的19：23分执行任务
    # minute = '*/3' 表示每 3 分钟执行一次
    # hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务
    scheduler.add_job(tick, 'cron', hour=11, minute=56)


if __name__ == '__main__':
    a_interval()
    a_corn()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
