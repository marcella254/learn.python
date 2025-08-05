# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:22:04 2024

@author: Marcella
"""

import pandas as pd
import numpy as np
data=pd.DataFrame({'ID':[1,2,3,4,5,6,7,8,9,10],
                   'Name':['John Doe','Jane Smith',
                'Bob Johnson','Alice Brown','Charly Davis','EVE','123','Sarah',
                'Michael','LISA'],
                   'Age':[28,34,' ',29,45,22,30,40,37,29],
                 'Gender':['M','F','M','Female','m','F','Male',' ','M','F'],
                 'Email':['john.doe@example.com','jane.smith@example',
                 'bob.johnson@domain.com','alice.brown@web.net',
            'charly.davies@domain','eve@sample.org','john.doe@example.com',
                 'sarah@example.com','michael@web.net','lisa@sample.org'],
         'Join_Date':['2021-05-12','2020/06/15','2019-07-20','2021-05-25',
        '2018-12-01','2023-01-10','2020-02-15','2021-03-05',
                              '2019/07/01','2020-02-20'],
                 'Score':[85,np.nan,90,'78%',92,88,87,95,80,75]})
print(data)
data.info()
#cleaning score column
data['Score'].unique()
data['Score']=data['Score'].replace({'78%':78})
type(data['Score'])
data.info()

#data['Score']=data['Score'].astype(int)

#cleaning age column
data['Age'].unique()
data['Age']=data['Age'].replace({' ':np.nan})
data.info()

#gender
data['Gender'].unique()
data['Gender']=data['Gender'].replace({' ':np.nan,'M':'male','F':'female','Female':'female',
                                       'Male':'male','m':'male'})
print(data)
data['Gender'].unique()
data['Gender']=data['Gender'].astype('category')
data.info()

#join_date
data['Join_Date'].unique()
data['Join_Date']=data['Join_Date'].replace({'2020/06/15':'2020-06-15',
                                             '2019/07/01':'2019-07-01'})
print(data)
data.info()
#data['Join_Date']=data['Join_Date'].astype(int)
data['Join_Date']=pd.to_datetime(data['Join_Date'])
print(data)
data.info()

#email
data['Email'].unique()
data['Email']=data['Email'].replace(['john.doe@example.com','jane.smith@example',
                 'bob.johnson@domain.com','alice.brown@web.net',
            'charly.davies@domain','eve@sample.org','john.doe@example.com',
                 'sarah@example.com','michael@web.net','lisa@sample.org'],
            ['john.doe@gmail.com','jane.smith@gmail.com',
                             'bob.johnson@gmail.com','alice.brown@gmail.com',
                        'charly.davies@gmail.com','eve@gmail.com','john.doe@gmail.com',
                             'sarah@gmail.com','michael@gmail.com','lisa@gmail.com'])
print(data)

#name
data['Name'].unique()
data.info()
data['Name']=data['Name'].replace(['EVE','123','LISA'],['Eve','John Doe','Lisa'])
print(data)
data.info()
data

data.to_excel('C:\\Users\\marcella\\Documents\\output2.xlsx',index=True)







