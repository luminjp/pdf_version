# pdf_version
PDFファイルのバージョンチェックと1.6以下の場合に1.7に変換するプログラム。

変換後は必ず開いて壊れていないかを確認してください。変換した場合は、オリジナルを保持しファイル名に _1.7 が追加されます。

実行サンプル
```bash
$ python3 pdf_version.py test -v17
Listing PDF files in directory: test

File: ticket_no_w353fe.pdf, Version: 1.5
Re-saved test/ticket_no_w353fe.pdf as test/ticket_no_w353fe_1.7.pdf in PDF 1.7-compatible format.
```

pymupdfをパッケージからインストールします。
```bash
pip3 install pymupdf
```
```バージョン確認
python pdf_version_checker.py <directory_path>
```

``` PDF1.6以下の場合1.7に変換
python pdf_version_checker.py <directory_path> -v17
```
