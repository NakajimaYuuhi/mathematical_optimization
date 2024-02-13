import datetime

'''
2023/12/1
1701356400
'''

'''
日付→unix
unix or 日付→曜日
'''
#UNIX時間→日付(datetimeオブジェクト)
dt = datetime.datetime.fromtimestamp(86400) #UNIX時間は0
print(dt)

#日付(datetimeオブジェクト)→UNIX時間
dt2 = dt.timestamp() #86400.0未満の値は、OS依存で、返せない
print(dt2)
#dt.weekday()

#日付→UNIX時間
tstr = '2020/9/17 9:00:01'
tdt = datetime.datetime.strptime(tstr, '%Y/%m/%d %H:%M:%S') #文字列コードを解析して、datetimeオブジェクトにする

#d_week = {'Sun':'日','Mon':'月','Tue':'火','Wed':'水','Thu':'木','Fri':'金','Sat':'土'}
d_week = {'Sun':'Sunday','Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday'}
print(type(tdt))
print(tdt)
print(tdt.timestamp())
print(tdt.strftime('%Y年%m月%d日({}) %H時%M分%S秒').format(d_week[tdt.strftime('%a')]))
print(tdt.strftime('%Y/%m/%d %H:%M:%S'))

'''
UNIX時間の作成

文字列取得
00:00:00をくっつける
文字列→datetime→UNIXTIME変換
'''

date = '2023/12/1'

def get_unixtime(month_week_date):    
    month_week_date_time = month_week_date +' 00:00:00'
    datetime_date = datetime.datetime.strptime(month_week_date_time, '%Y/%m/%d %H:%M:%S')
    print(datetime_date)
    unixtime = datetime_date.timestamp()
    return unixtime

def get_datetime(month_week_date):    
    month_week_date_time = month_week_date +' 00:00:00'
    datetime_date = datetime.datetime.strptime(month_week_date_time, '%Y/%m/%d %H:%M:%S')
    return datetime_date



unix_date = get_unixtime(date)
print(unix_date)

'''
曜日を取得

'''
def unixtime_to_strdate(unixtime):
    unixtime_datetime = datetime.datetime.fromtimestamp(unixtime)
    strdate = d_week[unixtime_datetime.strftime('%a')] + unixtime_datetime.strftime(',%m/%d/%Y')
    # Thursday, 5/20/2021
    return(strdate)



str_date = unixtime_to_strdate(unix_date)
print(str_date)

'''
日付リストを作成
'''
def get_datelist(start,end):
    get_unixtime(start)
    start_datetime = get_datetime(start)
    end_datetime = get_datetime(end)
    'datetimeのlistを作成'
    datelist_datetime = []
    while(start_datetime <= end_datetime):
         datelist_datetime.append(int(start_datetime.timestamp()))
         start_datetime += datetime.timedelta(days=1)
    return datelist_datetime    

date1 ='2023/12/05'
date2 = '2024/01/01'
print(get_datelist(date1,date2))

