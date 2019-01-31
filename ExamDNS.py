# exam dns
import GetRecord as GR
import csv
import datetime
import subprocess

x = []
a = GR.TestData()

count_failed = 0
count_succeed = 0
now = datetime.datetime.now()
nowstr = "{0:%Y%m%d%H%M}".format(now)

x = GR.ReadTestData("Testdata.csv")
#filename = input("nslookup結果ファイル名を入力してください。")
#filename2 = input("正誤判定結果ファイル名を入力してください。")
#examdata.nserver="dns102-1.jp1.ecl.ntt.com"
filename = "NslookupResult" + nowstr + ".txt"
filename2 = "JudgeResult" + nowstr + ".txt"
for examdata in x:
    examdata.nserver="8.8.8.8"
    GR.DefineTestData(examdata)
    GR.GetRecord(examdata.type,examdata.record,examdata.nserver,filename)
    GR.GetRecord(examdata.type,examdata.record,examdata.nserver,"tmpfile")
    a,b = GR.CheckValue(examdata.value,"tmpfile")
    count_succeed += a
    count_failed += b
    GR.ClearResultData("tmpfile")

with open(filename2,"w") as f:
    print(subprocess.check_output(["date"]),file=f)
    print("ーーーーーーーーーー\n試験結果サマリ\n成功回数/試行回数="+str(count_succeed)+"/"+str(count_failed+count_succeed)+"\nーーーーーーーーーー", file=f)
