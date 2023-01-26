import pandas as pd
import sqlite3

def download_sql (SQLname, op_string):
    ''' connect SQL '''
    conn = sqlite3.connect(SQLname)
    # op_string="SELECT Pump, Test, TargetP_psi, TargetQL_bpd, TargetQG_bpd, [HG_%], Qw_bpd, Qg_bpd, RPM, dpAve_psi "
    #                             + "FROM All_pump "
    #                             + "WHERE Pump LIKE 'GC%' "
    #                             #  + "Where WC = 0 "
    #                             + "ORDER BY RPM, Test, TargetP_psi, TargetQL_bpd, TargetQG_bpd"
    #                             + ";"
    df_data = pd.read_sql_query(op_string, conn)
    ''' close database '''
    conn.commit()   #apply changes to the database
    conn.close()
    return df_data

def new_pd_to_table(SQLname, table_name, df_data):
    ''' connect SQL '''
    conn = sqlite3.connect(SQLname)
    df_data.to_sql(table_name, conn, if_exists="replace", index=False)

    ''' close database '''
    conn.commit()   #apply changes to the database
    conn.close()

def insert_pd_to_table(SQLname, table_name, df_data):
    ''' connect SQL '''
    conn = sqlite3.connect(SQLname)
    df_data.to_sql(name=table_name, con=conn, if_exists='append', index=False)
    ''' close database '''
    conn.commit()   #apply changes to the database
    conn.close()

def connect_db(db):
    """
    :param db: the data base name in text
    :return: a connection with database and a cursor
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return conn, c

def disconnect_db(conn):
    """
    :param conn: a sqlite database connection
    :return: None
    """
    conn.commit()   #apply changes to the database
    conn.close()
