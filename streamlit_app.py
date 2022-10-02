import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select legacy_id from citibike_status")
my_catalog = my_cur.fetchall()
df = pd.DataFrame(my_catalog)

# temp write the dataframe to the page so I Can see what I am working with
streamlit.write(df)
# hdrs = pd.DataFrame(my_cur.description)

# df=pd.DataFrame(my_catalog,columns=hdrs['name'])
# #streamlit.write(df)
# # df = pd.DataFrame(my_catalog,columns=['id','legacy_id','station_status','bikes_available','bikes_disabled','rented_bikes','returned_bikes','ebikes','last_reported'])
# df.columns = map(lambda x: str(x).upper(), df.columns)
# # #streamlit.write(df.columns)
# # streamlit.write(df)

# id_list = df['ID'].values.tolist()
# #streamlit.write(id_list)

# option = streamlit.selectbox('Choose the station id to view the status:', list(id_list))
# if streamlit.button('show status'):
#           my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#           my_cur = my_cnx.cursor()
#           my_cur.execute("select * from station_status where 'ID' = '72' ")
#           res = my_cur.fetchall()
#           df2=pd.DataFrame(res,columns=hdrs['name'])
#           streamlit.write(df2)
          
