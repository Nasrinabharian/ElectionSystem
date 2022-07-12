import sqlite3
from sqlite3 import Error

DATABASE = 'voting.db'


def create_tables():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS CitizenshipRegistration
                 (fullname varchar(50)  NOT NULL,
                 natural_code nvarchar(10)  NOT NULL,
                 birthdate date);''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS [Candidate](
                        candidate_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        fullname varchar(50) not null,
                        natural_code nvarchar(10) not null,
                        birthdate date,
                        birthplace varchar(50),
                        gender varchar(7),
                        phone_number varchar(20),
                        email varchar(60),
                        [user_name] varchar(20),
                        number_of_votes int,

                        foreign key([user_name])
                            references user([user_name])
                            on delete cascade
                        CHECK (gender in ('Male', 'Female')));''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS [Volunteer](
                        volunteer_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                        fullname varchar(50) not null,
                        natural_code nvarchar(10) not null,
                        birthdate date,
                        birthplace varchar(50),
                        gender varchar(7),
                        phone_number varchar(20),
                        email varchar(60),
                        [user_name] varchar(20),

                        foreign key([user_name])
                            references user([user_name])
                            on delete cascade
                        CHECK (gender in ('Male', 'Female')));''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS [User](
                        fullname varchar(50) not null,
                        [username] varchar(20),
                        [password] varchar(20) not null,
                        natural_code nvarchar(10) not null,
                        email varchar(60),
                        [role] varchar(15),

                        primary key([username]),
                        CHECK([role] in ('Normal User', 'Manager')));''')

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_into_CitizenshipRegistration_table(fullname, natural_code, birthdate):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''INSERT INTO CitizenshipRegistration VALUES ('{}', '{}', '{}')'''.format(fullname, natural_code,
                                                                                       birthdate)
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_into_Candidate_table(fullname, natural_code, phone_number, email):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''INSERT INTO Candidate (fullname, natural_code, phone_number, email, number_of_votes)
         VALUES ('{}', '{}', '{}', '{}', {})'''.format(
            fullname, natural_code, phone_number, email, 0
        )
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def increase_vote(cand_ID):
    conn = None
    try: 
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''UPDATE Candidate SET number_of_votes = number_of_votes + {} WHERE candidate_ID = {}'''.format(1, cand_ID)
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_into_Volunteer_table(fullname, natural_code, phone_number, email):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''INSERT INTO Volunteer (fullname, natural_code, phone_number, email)
             VALUES ('{}', '{}', '{}', '{}')'''.format(
            fullname, natural_code, phone_number, email
        )
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def delete_from_Volunteer_table(natural_code1):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''DELETE FROM Volunteer 
             WHERE Volunteer.natural_code='{}' '''.format(
            natural_code1
        )
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_into_User_table(fullname, password, natural_code, email, role):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''INSERT INTO User (fullname, password, natural_code, email, role)
                 VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(
            fullname, password, natural_code, email, role
        )
        cursor.execute(s)
        conn.commit()
        print("Record created successfully")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def search_into_CitizenshipRegistration_table():
    conn = None
    output = []
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''SELECT * FROM CitizenshipRegistration'''
        cursor.execute(s)
        rows = cursor.fetchall()
        cols = [col[0] for col in cursor.description]
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            output.append(d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return output


def search_into_Candidate_table():
    conn = None
    output = []
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''SELECT * FROM Candidate'''
        cursor.execute(s)
        rows = cursor.fetchall()
        cols = [col[0] for col in cursor.description]
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            output.append(d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return output


def search_into_Volunteer_table():
    conn = None
    output = []
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''SELECT * FROM Volunteer'''
        cursor.execute(s)
        rows = cursor.fetchall()
        cols = [col[0] for col in cursor.description]
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            output.append(d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return output


def search_into_User_table():
    conn = None
    output = []
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''SELECT * FROM User'''
        cursor.execute(s)
        rows = cursor.fetchall()
        cols = [col[0] for col in cursor.description]
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            output.append(d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return output


def search_user_by_username(username):
    users = search_into_User_table()
    for user in users:
        if user['username'] == username:
            return user
    return None


def search_user_by_natural_code(natural_code):
    users = search_into_User_table()
    for user in users:
        if user['natural_code'] == natural_code:
            return user
    return None


def search_Citizen_by_natural_code(natural_code):
    citizens = search_into_CitizenshipRegistration_table()
    for citizen in citizens:
        if citizen['natural_code'] == natural_code:
            return citizen
    return None


def check_username_password(username, password):
    users = search_into_User_table()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False


def check_username_duplicate(username):
    users = search_into_User_table()
    for user in users:
        if user['username'] == username:
            return True
    return False


if __name__ == '__main__':
    # create_tables()
    insert_into_Candidate_table('d', 's', 'e', 'y')
    output = search_into_Candidate_table()
    print(output)
    list = search_into_Candidate_table()

    print(list)

    # insert_into_CitizenshipRegistration_table('reyhane abtahi', '1273040430', '1378-08-11')
    output = search_into_CitizenshipRegistration_table()
    print(output)

    # insert_into_Candidate_table('reyhane abtahi', '1273040430', '1378-08-11', 'Isfahan', 'Female', '09913789632',
    #                             'test@gmail.com', 'reyhan_abt')
    output = search_into_Candidate_table()
    print(output)

    # insert_into_Volunteer_table('reyhane abtahi', '1273040430', '1378-08-11', 'Isfahan', 'Female', '09913789632',
    #                             'test@gmail.com', 'reyhan_abt')
    output = search_into_Volunteer_table()
    print(output)

    # insert_into_User_table('reyhane abtahi', 'reyhan_abt', '2486', '1273040430', 'test@gmail.com', 'Normal User')
    output = search_into_User_table()
    print(output)
