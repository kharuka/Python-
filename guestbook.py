
# coding: utf-8

# In[1]:

import shelve


# In[2]:

DATA_FILE='guestbook.dat'


# In[ ]:

def save_data(name,comment,create_at):
    """投稿データを保存します
    """
    # shelveモジュールでデータベースファイルを開きます
    database=shelve.open(DATA_FILE)
    # データベースにgreeting_listがなければ、新しくリストを作ります
    if 'greeting_list' not in database:
        greeting_list=[]
    else:
        #データベースからデータを取得します
        greeting_list=database['greeting_list']
    # リストの先頭に投稿データを追加します
    greeting_list.insert(0,{
        'name':name,
        'comment':comment,
        'create_at':create_at
    })
    # データベースを更新します
    database['greeting_list']=greeting_list
    # データベースファイルを閉じます
    database.close()
    
def load_data():
    """投稿されたデータを返します
    """
    # shelveモジュールでデータベースをファイルを開きます。
    database=shelve.open(DATA_FILE)
    # greeting_listを返します。データがなければ空のリストを返します
    greeting_list=database.get('greeting_list',[])
    database.close()
    return greeting_list

