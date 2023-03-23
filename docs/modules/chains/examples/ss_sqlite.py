from langchain import OpenAI, SQLDatabase, SQLDatabaseChain


def test():

    sqldb_str = "sqlite:////Users/scottschmidt/sqlitedbs/Chinook.db"
    db = SQLDatabase.from_uri(sqldb_str)
    llm = OpenAI(temperature=0)

    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, top_k=3)
    db_chain.run("What are some example tracks by composer Johann Sebastian Bach?")


if __name__ == "__main__":
    test()
