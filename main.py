import sqlite3
import fastapi
import tomli
import uvicorn

from metricsmodels import RecordingMetrics

CFG_PATH = "config.toml"
app = fastapi.FastAPI()


def launch_server():
    uvicorn.run("main:app", port=8009, reload=True)


@app.post('/recordings')
def insert_recording_metrics(request: RecordingMetrics):

    def connect_to_db():

        def get_db_path_from_config():
            with open(CFG_PATH, mode="rb") as cfg:
                config = tomli.load(cfg)
                return config['db_path']

        db_path = get_db_path_from_config()

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        return conn, cur

    db_conn, cursor = connect_to_db()

    insert_query = f"""
        INSERT INTO recording
        (recording_id, create_time, start_time)
        VALUES ("{request['recording_id']}", "{request['create_time']}", "{request['start_time']}");"""

    cursor.execute(insert_query)

    db_conn.commit()

    test_query = "SELECT * FROM recording"
    cursor.execute(test_query)
    result = cursor.fetchall()
    print(format(result))


def main():
    launch_server()


if __name__ == '__main__':
    main()
