#モジュールのインストール######################################
import selenium
from selenium import webdriver
import time
from time import sleep
import pandas as pd
import datetime
import numpy as np
import sys
import it
import random   #recapture対策のsleep()に入れる秒数に使用

#前準備######################################
from fake_useragent import UserAgent
ua=UserAgent()
user_agent=ua.chrome

cols=['会社名',	'URL',	'データ取得日',
      '2012(口コミ総合評価)',	'2012(待遇面の満足度)',	'2012(社員の士気)',	'2012(風通しの良さ)',	'2012(社員の相互尊重)',	'2012(20代成長環境)',	'2012(人材の長期育成)',	'2012(法令順守意識)',	'2012(人事評価の適正感)',	'2012(有給休暇消化率)',	'2012(残業時間(月間))',
      '2013(口コミ総合評価)',	'2013(待遇面の満足度)',	'2013(社員の士気)',	'2013(風通しの良さ)',	'2013(社員の相互尊重)',	'2013(20代成長環境)',	'2013(人材の長期育成)',	'2013(法令順守意識)',	'2013(人事評価の適正感)',	'2013(有給休暇消化率)',	'2013(残業時間(月間))',
      '2014(口コミ総合評価)',	'2014(待遇面の満足度)',	'2014(社員の士気)',	'2014(風通しの良さ)',	'2014(社員の相互尊重)',	'2014(20代成長環境)',	'2014(人材の長期育成)',	'2014(法令順守意識)',	'2014(人事評価の適正感)',	'2014(有給休暇消化率)',	'2014(残業時間(月間))',
      '2015(口コミ総合評価)',	'2015(待遇面の満足度)',	'2015(社員の士気)',	'2015(風通しの良さ)',	'2015(社員の相互尊重)',	'2015(20代成長環境)',	'2015(人材の長期育成)',	'2015(法令順守意識)',	'2015(人事評価の適正感)',	'2015(有給休暇消化率)',	'2015(残業時間(月間))',
      '2016(口コミ総合評価)',	'2016(待遇面の満足度)',	'2016(社員の士気)',	'2016(風通しの良さ)',	'2016(社員の相互尊重)',	'2016(20代成長環境)',	'2016(人材の長期育成)',	'2016(法令順守意識)',	'2016(人事評価の適正感)',	'2016(有給休暇消化率)',	'2016(残業時間(月間))',
      '2017(口コミ総合評価)',	'2017(待遇面の満足度)',	'2017(社員の士気)',	'2017(風通しの良さ)',	'2017(社員の相互尊重)',	'2017(20代成長環境)',	'2017(人材の長期育成)',	'2017(法令順守意識)',	'2017(人事評価の適正感)',	'2017(有給休暇消化率)',	'2017(残業時間(月間))',
      '2018(口コミ総合評価)',	'2018(待遇面の満足度)',	'2018(社員の士気)',	'2018(風通しの良さ)',	'2018(社員の相互尊重)',	'2018(20代成長環境)',	'2018(人材の長期育成)',	'2018(法令順守意識)',	'2018(人事評価の適正感)',	'2018(有給休暇消化率)',	'2018(残業時間(月間))',
      '2019(口コミ総合評価)',	'2019(待遇面の満足度)',	'2019(社員の士気)',	'2019(風通しの良さ)',	'2019(社員の相互尊重)',	'2019(20代成長環境)',	'2019(人材の長期育成)',	'2019(法令順守意識)',	'2019(人事評価の適正感)',	'2019(有給休暇消化率)',	'2019(残業時間(月間))',
      '2020(口コミ総合評価)',	'2020(待遇面の満足度)',	'2020(社員の士気)',	'2020(風通しの良さ)',	'2020(社員の相互尊重)',	'2020(20代成長環境)',	'2020(人材の長期育成)',	'2020(法令順守意識)',	'2020(人事評価の適正感)',	'2020(有給休暇消化率)',	'2020(残業時間(月間))',
      '2021(口コミ総合評価)',	'2021(待遇面の満足度)',	'2021(社員の士気)',	'2021(風通しの良さ)',	'2021(社員の相互尊重)',	'2021(29代成長環境)',	'2021(人材の長期育成)',	'2021(法令順守意識)',	'2021(人事評価の適正感)',	'2021(有給休暇消化率)',	'2021(残業時間(月間))',
      ]

company_list=[]
URL_list=[]
df=pd.DataFrame(columns=cols)
now=datetime.datetime.today().strftime("%Y{}%m{}%d{}").format(*"年月日")
Loop_cnt=0

#事前に調査したおすすめ企業名のデータセットの取得
URL_df=pd.read_csv("C:\\Users\\名前\\Documents\\URL_LIST_Openwork企業一覧.csv")

#データセットの加工
keys=[]
values=[]
for i in range(len(URL_df)):
  keys.append(URL_df,iloc[i,0])
  values.append(URL_df,iloc[i,1])

URL_dict=dict(zip(keys,values))

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--user-agent="+user_agent)
wd=webdriver.Chrome(executable_path=r"chromedriver.exe",options=chrome_options)


#スクレイピング######################################
for URLs in URL_dict:
  companyName=URLs        #会社名
  URL=URL_dict[URLs]      #企業URL

  wd.get(URL)
  sleep(4)

  html=wd.page_source

  try:
    Split_html=html.split("getData()")[2]

  except:
    #認証が出たら認証処理を動かす
    TrustForm=wd.find_element_by_class_name("textarea")
    TrustForm.send.keys(input"認証キーを入力してください：")
    TrustBtn=wd.find_element_by_class_name("button.button-usuallyBlue.w-100p.mt-15.placeholder_submit")
    TrustBtn.click()

    #情報を取り出す
    html=wd.page_source
    Split_html=html.split("getData()")[2]

  #datasetごとにsplit
  Split_data=Split_html.split("data:[")   #datasetの1～11番目を取得

  data_beauty=[]

  for i in range(len(Split_data)):
    if 0<i<12:
      #格納用リストに追加
      data_beauty.append(Split_data[i].split('],"unit')[0])

    source=[]
    for i in range(len(data_beauty)):
      split_beauty=[]
      split_beauty=data_beauty[i].split(",")
      source.append(split_beauty)

    df_list=[]

    df_list.append(companyName)
    df_list.append(URL)
    df_list.append(now)

    for i in range(len(source)):
      for j in range(len(source[i])):
        df_list.append(source[i][j])

    #データフレームに転記
    df.loc[Loop_cnt]=df_list
    Loop_cnt+=1

wd.close()


#データの保存######################################
df.to_csv("Openwork企業分析.csv",index=False,encoding="utf_8_sig")