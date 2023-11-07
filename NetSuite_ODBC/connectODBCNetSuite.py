import pandas as pd
import json
import os
from NetSuite_Connector.ODBC import ODBC
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

try:
    connections = ODBC(
        account_id=str(os.getenv("ACCOUNTID_NETSUITE")),
        user_email=str(os.getenv("EMAILID_NETSUITE")),
        role_id=str(os.getenv("ROLEID_NETSUITE")),
        dsn=str(os.getenv("DSN_NETSUITE_ODBC")),
        password=str(os.getenv("PASSWORD_NETSUITE"))
    )
    dataNetsuite = connections.query(f"SELECT * from {str(os.getenv('TABLE_NETSUITE'))}")
    df_netsuite =  pd.read_json(dataNetsuite.response)
except (Exception) as e:
    print(e)

try:
    engine = create_engine('postgresql+psycopg2://'+str(os.getenv("USERNAME_DB_POSTGRE"))+':'+str(os.getenv("PASSWORD_DB_POSTGRE")) \
                           +'@'+str(os.getenv("HOST_NAME_DB_POSTGRE"))+':'+os.getenv("PORT_DB_POSTGRE")+'/'+str(os.getenv("DB_NAME_DB_POSTGRE")))
    df_netsuite.to_sql(str(os.getenv("DB_NAME_DB_POSTGRE")), engine, if_exists='replace', index=False)
    print('Running successfully', df_netsuite.shape[0],' data to postgres')
except (Exception) as e:
    print(e)