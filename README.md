# python_final_project: Just Tap The Black Tile 

## code 執行
執行「只踩黑塊兒.py」

## 遊戲結構
* **MainMenu**
  * 編曲介面
    * 編輯介面
    * Export功能
    * Import功能
  * 遊戲主體

## 檔案介紹
> 每個檔.py案都是module，各代表一個視窗，全部import進只踩黑塊兒.py

`只踩黑塊兒.py (top entity)`
* 即mianmenu，主要使用PyQt5寫成。按下create可以前往編曲介面、play前往遊戲，按下其他區塊會有隨機的音樂播出。

`images.py`
* 各介面背景圖片的圖檔。

`mainwindow.py `
* 即編曲介面，主要使用PyQt5寫成。

`filename.py `
* 即export功能，主要使用PyQt5寫成。

`import_list.py `
* 即import功能，主要使用PyQt5寫成。

`chord.py, drum.py, piano.py`
* 分別為chord, drum, piano的編輯介面，主要使用PyQt5寫成。

`messagebox.py`
* 各介面的彈出式訊息視窗，主要使用PyQt5寫成。

`game.py`
* 即遊戲主體，主要使用PyGame寫成。

`sound (folder)`
* 遊戲中的音檔們。

`image (folder)`
* 各介面的圖片檔。


