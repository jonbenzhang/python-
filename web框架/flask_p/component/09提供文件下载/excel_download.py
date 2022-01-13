import xlsxwriter
from flask_old import send_file, send_from_directory
import io


def table_to_excel_main(catalog_ids: str):
    file = io.BytesIO()
    f = xlsxwriter.Workbook(file)
    # 此处进行对xlsx文件的操作
    # 必须要进行关闭,否则不会写入到o.BytesIO()中
    f.close()
    # 重置游标位置,因为xlsxwriter已经把游标写到最后位置，所以需要重置游标位置
    # 否则就会造成file.read()为空
    file.seek(0)
    return send_file(file,
                     # 下边两个为修改文件名
                     as_attachment=True,
                     attachment_filename="标准数据.xlsx")
