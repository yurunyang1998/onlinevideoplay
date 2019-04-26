import flask as fl
import  sqlite3




def get_db():
    if not hasattr( fl.g ,"sqlite_de"):
        fl.g._database;

def connect_df():
    rv = sqlite3.connect()