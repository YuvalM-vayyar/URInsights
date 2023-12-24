import sqlite3
import fastapi
import tomli
import uvicorn

CFG_PATH = "config.toml"
app = fastapi.FastAPI()


def launch_server():
    uvicorn.run("main:app", port=8009, reload=True)
    # server_config = uvicorn.Config("main:app", port=5000, log_level="info")
    # server = uvicorn.Server(server_config)
    # await server.serve()
    # process = subprocess.Popen(['uvicorn', 'main:app', '--reload', '--port', '5000'], stdout=subprocess.PIPE)


@app.post('/metrics')
def insert_ur_data_to_db():

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

    # test
    print("START TEST")
    test_query = "SELECT * FROM agent"
    cursor.execute(test_query)
    result = cursor.fetchall()
    print(f'{format(result)}')


def main():
    launch_server()
    # server_config = uvicorn.Config("main:app", port=5001, log_level="info")
    # server = uvicorn.Server(server_config)
    # await server.serve()
    # print("hello world")


if __name__ == '__main__':
    main()
    # asyncio.run(main())
