# word2vec_use

參考：https://github.com/zake7749/word2vec-tutorial

目標：
將商品名稱進行過濾，並將"類別"加在商品資料當中
ex:洗髮精、洗髮乳，歸類為"洗髮乳"

first：
找出與分類高度相關的其他商品分類
如果列表當中的商品分類在高相關的內容當中，就進行刪除

second：
將斷詞後的商品名稱比對商品分類
若符合就加入為tag
最後以csv格式輸出

使用方式：
使用wiki的資料訓練完模型後，分別執行 first、second
