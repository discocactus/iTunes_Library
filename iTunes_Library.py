
# coding: utf-8
iTunesで'曲’プレイリストを標準テキスト(UTF-8? 改行コード CR(\r))で書き出し
書き出し時にHDDがマウントされているとなぜかファイルサイズが1.5倍ほどになる、曲の並び順も変わる、なぜ？
# In[ ]:


import pandas as pd


# In[ ]:


# pandas の最大表示列数を設定 (max_rows で表示行数の設定も可能)
pd.set_option('display.max_columns', 30)


# In[ ]:


# 事前にexcelにインポートしたデータを使いたい場合
# it_excel = pd.read_excel('iTunes_Library_191122.xlsx', keep_default_na=False)


# In[ ]:


it_text = pd.read_csv('iTunes_Music_191122.txt'
                      , sep='\t'
                      , usecols=[0, 1, 3, 4] # 名前,アーティスト,アルバム,グループ
                      , keep_default_na=False # 指定しないと空欄がNaNになる?
                      , lineterminator = '\r' # 改行コード CR
                      , encoding='utf-8')


# In[ ]:


# 作業用テーブルの作成
it = it_text.copy()


# In[ ]:


it


# In[ ]:


# 数値は文字列に型変換しておかないとgroupby等ができない?
it['アルバム'] = it['アルバム'].astype(str)


# In[ ]:


# エンコード指定なしで Excel 保存
# 出力後に全セルの書式設定を文字列に変更しておいた方がよいかも?
writer = pd.ExcelWriter('albums.xlsx')
albums.to_excel(writer, index=False)
writer.save()


# In[ ]:


tracks = it.sort_values(['アーティスト', 'アルバム'])


# In[ ]:


tracks


# In[ ]:


# エンコード指定なしで Excel 保存
# 出力後に全セルの書式設定を文字列に変更しておいた方がよいかも?
writer = pd.ExcelWriter('tracks.xlsx')
tracks.to_excel(writer, index=False)
writer.save()


# In[ ]:


albums = it[['アーティスト', 'アルバム', 'グループ']]    .drop_duplicates(['アーティスト', 'アルバム'])    .sort_values(['アーティスト', 'アルバム'])


# In[ ]:


albums


# In[ ]:


# エンコード指定なしで Excel 保存
# 出力後に全セルの書式設定を文字列に変更しておいた方がよいかも?
writer = pd.ExcelWriter('albums.xlsx')
albums.to_excel(writer, index=False)
writer.save()


# In[ ]:


# アーティストごとの楽曲数、アルバム数
it.groupby('アーティスト').nunique()


# In[ ]:


# アルバムごとの楽曲数
it.groupby('アルバム').nunique()


# In[ ]:


# アーティストごとのアルバム数
it.groupby('アーティスト').agg({'アルバム': 'nunique'})

