from random import choice
import re
import numpy as np

gc = {'GeForce RTX 3080 Ti 16GB': 17, 'GeForce RTX 3080 Ti для ноутбуков 8GB': 16, 'GeForce RTX 3080 Ti 8GB': 16, 'GeForce RTX 3070 Ti для ноутбуков 8GB': 15, 'GeForce RTX 3070 Ti 8GB': 15, 'GeForce RTX 3070 для ноутбуков 8GB': 15, 'GeForce RTX 3060 для ноутбуков 6GB': 14, 'GeForce RTX 3060 6GB': 14, 'GeForce RTX 3050 для ноутбуков 6GB': 13, 'GeForce RTX 3050 Ti для ноутбуков 4GB': 12, 'GeForce RTX 3050 Ti 4GB': 12, 'GeForce RTX 3050 для ноутбуков 4GB': 12, 'GeForce RTX 3050 4GB': 12, 'Radeon Graphics': 11,'GeForce GTX 1650 4GB': 10, 'GeForce MX450 2ГБ': 9, 'GeForce MX350 2ГБ': 9, 'Intel Iris Xe Graphics': 8, 'Radeon RX Vega 8': 8, 'Radeon': 7, 'Intel UHD Graphics': 6, 'Intel HD Graphics': 5, 'Radeon Vega 3': 4, 'Intel Iris Graphics': 4, 'Intel UHD Graphics 600': 3, 'UHD Graphics 600': 3, 'Intel HD Graphics 5500': 2, 'Intel HD Graphics 500': 1}
dt = {'LTPS': 4, 'TFT': 3, 'IPS': 3, 'IPS-level': 3, 'AHVA': 2, 'TN': 1}
pn = {'Intel': 2, 'AMD': 1}
pc = {'Core i9': 9, 'Core i7': 8, 'Core i5': 7, 'Ryzen 7': 6, 'Ryzen 5': 5, 'Ryzen 3': 4, 'Core i3': 3, 'Pentium': 2, 'Celeron': 1}
os = {'MacOS': 7, 'Windows 11 Pro 64': 6, 'Windows 11 Pro': 6, 'Windows 11 Домашняя 64': 5, 'Windows 11 Домашняя S-режим': 5, 'Windows 11 Домашняя': 5, 'Windows 11': 5, 'Windows 10 Pro': 4, 'Windows 10 Домашняя 64': 3, 'Windows 10 Домашняя': 2, 'Linux': 1, 'FreeDOS': 1, 'DOS': 1, 'не установлена': 0}
proc_dict = {'Intel Core i9': (8, '5 ГГц', '18 МБ'), 'Intel Core i7': (6, '4,7 ГГц', '12 МБ'), 'Intel Core i5': (6, '4,4 ГГц', '12 МБ'), 'Intel Core i3': (4, '4,2 ГГц', '8 МБ'), 'Intel Pentium': (2, '3,5 ГГц', '4 МБ'), 'Intel Celeron': (2, '2,6 ГГц', '2 МБ'), 'AMD Ryzen 7': (8, '4,7 ГГц', '30 МБ'), 'AMD Ryzen 5': (6, '3,7 ГГц', '18 МБ'), 'AMD Ryzen 3': (4, '3,4 ГГц', '12 МБ')}

def string_generator():
    return choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'])

def random_color_string_generator():
    string = '#'
    for _ in range(6):
        string += string_generator()
    if string == '#ffffff':
        random_color_string_generator()
    return string

def get_array(f):
    ntb_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    displ = str(f.disp)
    disp_lst = re.split('[\s"x]', displ)
    disp_lst[0] = disp_lst[0].replace(',', '.')
    ntb_lst[0] = float(disp_lst[0])
    ntb_lst[1] = int(disp_lst[2])
    ntb_lst[2] = int(disp_lst[3])
    ntb_lst[3] = dt[str(f.disp_type)]
    proc = str(f.proc)
    proc_lst = proc.split()
    ntb_lst[4] = pn[proc_lst[0]]
    if len(proc_lst) == 2:
        ntb_lst[5] = pc[proc_lst[1]]
    else:
        ntb_lst[5] = pc[proc_lst[1] + ' ' + proc_lst[2]]
    graph = str(f.gc)
    graph_lst = graph.split()
    if graph_lst[0] == 'Nvidia':
        ntb_lst[6] = gc[graph.replace('Nvidia ', '')]
    if graph_lst[0] == 'AMD':
        ntb_lst[6] = gc[graph.replace('AMD ', '')]
    if graph_lst[0] == 'Intel':
        ntb_lst[6] = gc[graph]
    ramm = str(f.r_a_m)
    ramm_lst = ramm.split()
    ntb_lst[7] = int(ramm_lst[0])
    hd = str(f.hd)
    hd_lst = hd.split()
    if hd_lst[1] == 'ГБ':
        ntb_lst[8] = int(hd_lst[0])
    else:
        ntb_lst[8] = 1024 * int(hd_lst[0])
    ntb_lst[9] = os[str(f.o_s)]
    ntb_lst[10] = int(f.core.cores)
    cache = str(f.cm)
    cache_lst = cache.split()
    ntb_lst[11] = int(cache_lst[0])
    freq = str(f.freq)
    freq_lst = freq.split()
    freq_lst[0] = freq_lst[0].replace(',', '.')
    ntb_lst[12] = float(freq_lst[0])
    ntb_lst = np.array(ntb_lst)
    return ntb_lst