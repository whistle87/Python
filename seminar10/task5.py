"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

websites = ['youtube.com', 'yandex.ru']
for site in websites:
    ping_site = ['ping', site]
    websites_ping = subprocess.Popen(ping_site, stdout=subprocess.PIPE)
    print(websites_ping.stdout)
    for line in websites_ping.stdout:
        res = chardet.detect(line)
        print(line.decode(res['encoding']))
