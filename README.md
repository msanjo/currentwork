# examdns
# ファイル
- モジュール類：GetRecord.py
- 実行ファイル：ExamDNS.py
- テストデータ：Testdata.csv（試験対象）

# 使い方
- 上記のファイルを同一フォルダに格納の上、Pythonのランタイムで実行すること
- Python 3.7.0で動作確認
- テストデータは以下のフォーマットでCSV形式で作成する。  
  行数に特に制限はない
- 出力結果として、以下が出力される  
  *JudgeResultYYYYMMDDhhmm.txt:何件中何件の出力が成功したか。*  
  *成功・・・想定のvalue通りの結果がnslookupで得られること*  
  *NslookupResultYYYYMMDDhhmm.txt:nslookupの結果一覧*  
- また、標準出力も同時にされる

# テストデータ例
---------
>>  record_type,record_data,record_value  
>>  a,record.hogehoge.hoge,1.1.1.1  
---------
