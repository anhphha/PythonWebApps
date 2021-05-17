from datetime import datetime
import psycopg2 as post_gress
from influxdb import InfluxDBClient, DataFrameClient

class Backend:
    def __init__(self, hostname, port, username, db_name, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.db_name = db_name
        self.password = password

        self.client = post_gress.connect(host=self.hostname, port=self.port, database=self.db_name,
                                         password=password, username=self.username)

    # def get_name(self):
    #     return self.name
    #
    # def get_time(self):
    #     curent_time = datetime.utcnow()
    #     current_time_str = curent_time.strftime("%m/%d/%Y, %H:%M:%S")
    #     return current_time_str
    #

    def load_data(self):
        query = ''

        self.client.execute()
        query_result = self.client.execute(query)

        # pre-processing query_result
        processed = '' # do query result procerss

        return processed

    def result_manger(self):
        data = self.load_data()

        # convert to json

        data_json # convert to json
        return data_json
