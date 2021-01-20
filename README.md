# python_final_project: Just Tap The Black Tile 

## code 執行
執行「只踩黑塊兒.py」\n
請將解析度調整成1920x1080、windows縮放與版面配置的「變更文字、應用程式與其他項目大小」調整成125%

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
* 即mainmenu，主要使用PyQt5寫成。按下create可以前往編曲介面、play前往遊戲，按下其他區塊會有隨機的音樂播出。

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

## How to Play?
### 編曲(create)
#### edit
每個edit代表一個小節，drum與piano的edit介面中每個選單代表一個八分音符的音，chord的edit介面中的選單代表該小節的和絃
#### preview
試聽目前編曲的成果
#### export
輸出完成的曲子，並輸入檔名，ex:"mysong"，會自動存為一個txt檔
#### import
輸入做到一半曲子的檔名，ex:"mysong.txt"，可以繼續編曲。

### 遊戲(play)
#### 選曲
輸入要玩的曲子的檔名，ex:"mysong.txt"。
#### 遊玩
依照最底層的黑鍵位置按出相對應的按鍵:最左按q、左中按w、右中按e、最右按r，若灰鍵則按空白鍵。目標是快且正確的完成整首音樂。

