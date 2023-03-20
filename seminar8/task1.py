"""
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Пример того, что должно получиться:
Изготовитель системы,Название ОС,Код продукта,Тип системы
1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based
2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based
3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based
Обязательно проверьте, что у вас получается примерно то же самое.
ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv


def get_data(*file_name):
    main_data = [["Изготовитель ОС", "Название ОС", "Код продукта", "Тип системы"]]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in file_name:
        with open(file) as f:
            line = f.readline()
            while line:
                line_split = line.split(':')
                if line_split[0] == "Изготовитель ОС":
                    os_prod_list.append(" ".join(line_split[1].split()))
                elif line_split[0] == "Название ОС":
                    os_name_list.append(" ".join(line_split[1].split()))
                elif line_split[0] == "Код продукта":
                    os_code_list.append(" ".join(line_split[1].split()))
                elif line_split[0] == "Тип системы":
                    os_type_list.append(" ".join(line_split[1].split()))
                line = f.readline()
    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)
    with open('main_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(main_data)
    return main_data


def write_to_csv(csv_file):
    data_from_file = get_data('info_1.txt', 'info_2.txt', 'info_3.txt')
    with open(csv_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        result = []
        for i in range(len(data_from_file[1])):
            result_line = list()
            result_line.append(str(i + 1))
            result_line.append(str(data_from_file[1][i]))
            result_line.append(str(data_from_file[2][i]))
            result_line.append(str(data_from_file[3][i]))
            result_line.append(str(data_from_file[4][i]))
            result.append(result_line)
        writer.writerows(result)


write_to_csv('data_report.csv')
