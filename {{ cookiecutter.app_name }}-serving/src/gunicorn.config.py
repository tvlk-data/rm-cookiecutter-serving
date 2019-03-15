import multiprocessing

bind = ':80'

workers = 4 if multiprocessing.cpu_count() * 2 + 1 > 4 else multiprocessing.cpu_count() * 2 + 1
threads = 4 if multiprocessing.cpu_count() * 2 + 1 > 4 else multiprocessing.cpu_count() * 2 + 1
reload = True

timeout = 600