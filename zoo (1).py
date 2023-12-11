# 11.1
# zoo.py

def hours():
  print('Open 9-5 daily')

import zoo
zoo.hours()

# 11.2
import zoo as menagerie
menagerie.hours()

# 16.8
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///books.db')
connection = engine.connect()

result = connection.execute("SELECT title FROM book ORDER BY title")
for row in result:
    print(row['title'])

connection.close()
