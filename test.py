from datetime import datetime

from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.post("/report")
def upon_receiving_report(request: dict):

    # db_connection = sqlite3.connect("C:\\vayyar\\URInsights\\urinsights.db")
    db_connection = sqlite3.connect("C:\\code\\AnalyticsPrototypingDir\\testDB.db")
    cursor = db_connection.cursor()

    # insert_query = f"""INSERT INTO agent
    #                 (agent_id, agent_ip, agent_port, timestamp, agent_group, agent_password, controller_id)
    #                 VALUES ("{request['agent_id']}", "{request['agent_ip']}", {request['agent_port']},
    #                 "{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}", "{request['agent_group']}",
    #                 "{request['agent_password']}", {request['controller_id']});"""
    insert_query = f"""INSERT INTO TestTable (testField) VALUES ("{request['boot_str']}");"""
    print(insert_query)
    cursor.execute(insert_query)
    db_connection.commit()

    select_query = f"""SELECT * from TestTable;"""
    print(select_query)
    cursor.execute(select_query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    # cursor.close()


@app.get("/test")
def get_test():
    print("get request succeeded")
