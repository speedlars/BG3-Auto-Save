# BG3-Auto-Save

[載點](https://github.com/speedlars/BG3-Auto-Save/releases/tag/v1.0.0)

<img width="122" height="186" alt="image" src="https://github.com/user-attachments/assets/6de3c964-723e-4cae-9cc3-6249441648ce" />   

適用於柏德之門3的自動存檔程式，會每過五分鐘自動按下F5一次。

開啟自動存檔功能時視窗須保持在遊戲介面中，同時程式斥窗不得關閉。

如過想要讓程式在遊戲從steam開啟時自動開啟，可以從steam介面中右邊的管理(或者點右鍵)->內容->一般->啟動選項欄位填入：

```
powershell -WindowStyle Hidden -Command "& {Start-Process '(此程式的資料夾路徑)\save.exe'; Start-Process '%command%'}"
```

<img width="1226" height="601" alt="image" src="https://github.com/user-attachments/assets/52be88fe-20f2-424a-8590-2f16da793701" />

exe啟動時會跳出管理員權限通知是正常的，同意即可。
