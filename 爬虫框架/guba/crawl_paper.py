# -*- coding: utf-8 -*-
import subprocess
import random
import time
from paper.log_config import logger
from scrapy.cmdline import execute
execute('scrapy crawl  eastmoneyguba'.split())
1121
# def func():
#     p = subprocess.run(['scrapy', 'list'], stdout=subprocess.PIPE, encoding='utf8')
#
#     r = p.stdout
#     PART_SIZE = 5
#     names = r.split()
#     random.shuffle(names)
#     for i in range(0, len(names), PART_SIZE):
#         part_names = names[i:i+PART_SIZE]
#         print(part_names)
#         need_wait = []
#         for name in part_names:
#             if name.startswith('sina'):
#                 need_wait.append(name)
#                 continue
#             subprocess.Popen(['scrapy', 'crawl', name])
#             logger.info(f"spider: {name} start")
#             time.sleep(0.5)
#         if need_wait:
#             for name in need_wait:
#                 try:
#                     logger.info(f"spider: {name} start")
#                     subprocess.run(['scrapy', 'crawl', name], timeout=60*5)
#                 except subprocess.TimeoutExpired:
#                     pass
#         # else:
#         #     time.sleep(60*2)
#
#
# def main():
#     # while True:
#         func()
#         # print('one crawl finish, sleep...')
#         # time.sleep(3600*4)
#
#
# if __name__ == "__main__":
#     main()
