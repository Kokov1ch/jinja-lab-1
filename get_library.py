from jinja2 import Template
import sqlite3
from library_model import get_publisher
# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.sqlite")
# выбираем записи из таблицы publisher
df_publisher = get_publisher(conn)
# закрываем соединение с базой
conn.close()
# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('/template/library_templ.html')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
 table_1 = "publisher",
 relation_1 = df_publisher,
 len = len
 )
#создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
