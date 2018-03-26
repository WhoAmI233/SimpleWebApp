from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import sys
sys.path.append('../')
import Common.SqlServer as mssql

def get_text_from_target(request):
    sqlDBConnect = mssql.ODBCMS('{SQL SERVER}', r'192.168.1.254', 'test',
                             'qiuguochao', 'qiuguochao')
    sql = "select 1"
    try:
        sqlDBConnect.ExecQuery(sql)
    except:
        print("db connect error.")

    return render(
        request,
        'index.html',
        {'get_text_from_target': request.GET.get('get_text_from_target', sql)}
    )


