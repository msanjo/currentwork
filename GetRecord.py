# 外部DNSの試験自動化プログラム
import subprocess
import csv
#　テストデータをインスタンス化
class TestData:
    def __init__(self):
        self.type = ""
        self.record = ""
        self.value = []
        self.nserver = ""
#　特定のレコード情報を取得する。テストを実行して、ファイルに結果を書き込む
#　引数として、type、レコード、DNS指定ができること。
def GetRecord(type,record,nserver,filename):
    result = subprocess.check_output(["nslookup","-type="+type,record,nserver])
    result = str(result)
    #　改行文字・タブなどを有効化する
    #result = result.replace('\n','\n--------\n')
    result = result.replace('\\n','\n')
    result = result.replace('\\t','\t')
    file1 = open(filename,"a")
    print(subprocess.check_output(["date"]),file=file1)
    file1.write(result)
    file1.close()

# 結果ファイルの内容を消去する
def ClearResultData(file):
    file2 = open(file,"w")
    file2.write("")
    file2.close()

#　期待した値がファイル内にあるか確認する
def CheckValue(value,file):
    count_succeed = 0
    count_failed = 0
    for line in value:
        file3 = open(file,"r")
        int_bit = 0
        print("-------- Check Result -------")
        for str in file3:
            if line in str:
                print("The value:"+ line +" is OK!")
                int_bit = 1
                count_succeed += 1
            else:
                print("・")
        file3.close()
        if int_bit == 0:
            print("!!!!Warning!!!! The value:"+ line +" is not found..")
            count_failed += 1
    return count_succeed,count_failed

def DefineTestData(data):
    print("-------- TestData -------- ")
    print("Record : "+ data.record)
    print("Record Type : "+ data.type)
    int = 1
    for v in data.value:
        print("Expected Value"+ str(int) +" : "+ v)
        int += 1
    print("Exam NameServer : "+ data.nserver)

def ReadTestData(file):
    data = []
    a = TestData()
    with open(file, 'r') as file:
        reader = csv.reader(file)
        # ヘッダ行は特別扱い
        header = next(reader)
        for row in reader:
            a.type = row[0]
            a.record = row[1]
            a.value = row
            a.value.pop(0)
            a.value.pop(0)
            data.append(a)
            a = TestData()
    return data
