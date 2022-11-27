import psycopg2
from contextlib import redirect_stdout


def GetData():
    conn = psycopg2.connect(
        database="organizer", user='solokhovir', password='12345678', host='localhost', port=''
    )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM public.web_todo''')
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    with open('data.txt', 'w') as f:
        with redirect_stdout(f):
            print(*result, sep='\n')



GetData()
# "\n".join(op)