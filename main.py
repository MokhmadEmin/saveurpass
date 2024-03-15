import sqlite3
from colorama import Fore, init
from bitarray import bitarray

init() # connect colorama


# connecting to database
db_connect = sqlite3.connect("database.db")
db_cursor = db_connect.cursor()


# start text
print(Fore.GREEN + """
█▀ ▄▀█ █░█ █▀▀   █░█ █▀█   █▀█ ▄▀█ █▀ █▀
▄█ █▀█ ▀▄▀ ██▄   █▄█ █▀▄   █▀▀ █▀█ ▄█ ▄█

""")
print(Fore.WHITE + "SaveUrPass - it is a command, local, safe and open password manager.\n")
print(Fore.LIGHTRED_EX + "Commands:")
print(Fore.WHITE + f'''
CREATE
DELETE <service name>
PUT <service name>
SHOW <service name>
SHOW ALL
EXIT
	''')


# encription
def encoder(text):
    binary = ' '.join(format(ord(i), '08b') for i in text)
    return binary


def decoder(bins):
    bts = bitarray(bins)
    ascs = bts.tobytes().decode('ascii')
    return ascs


def decode_binary_list(binary_list):
    decoded = []
    for item in binary_list:
    	item = (item[0], decoder(item[1]), decoder(item[2]), decoder(item[3]), decoder(item[4]))
    	decoded.append(item)
    return decoded



# commands
def create(auth_url: str, programm: str, nickname: str, password: str):
	db_cursor.execute(f'INSERT INTO passwords(auth_url, programm, nickname, password) VALUES (?, ?, ?, ?);',
		(encoder(auth_url), encoder(programm), encoder(nickname), encoder(password))
	)
	db_connect.commit()


def delete(service: str):
	db_cursor.execute(f'DELETE FROM passwords WHERE programm = "{encoder(service)}"')
	db_connect.commit()


def put(auth_url: str, programm: str, nickname: str, password: str):
	db_cursor.execute(f'''UPDATE passwords
		SET auth_url = "{encoder(auth_url)}",
		nickname = "{encoder(nickname)}",
		password = "{encoder(password)}"
		WHERE programm = "{encoder(programm)}"''')
	db_connect.commit()


def show(service: str):
	res = None

	if service == "ALL":
	    res = db_cursor.execute(f"SELECT * FROM passwords").fetchall()
	    return decode_binary_list(res)
	else:
		res = db_cursor.execute(f'SELECT * FROM passwords WHERE programm = "{encoder(service)}"').fetchone()
		return (res[0], decoder(res[1]), decoder(res[2]), decoder(res[3]), decoder(res[4]))


# programm cycle
while True:
	try:
		command = input(">")

		if command == "CREATE":
			auth_url = input("url of registartion(optional): ")
			programm = input("programm: ")
			nickname = input("nickname: ")
			password = input("password: ")
			create(auth_url, programm, nickname, password)

		if command.startswith(f"DELETE ") and command.replace(f"DELETE ", "") != "":
			delete(command.replace(f"DELETE ", ""))


		if command.startswith(f"PUT ") and command.replace(f"PUT ", "") != "":
			auth_url = input("url of registartion(optional): ")
			nickname = input("nickname: ")
			password = input("password: ")
			put(auth_url, command.replace(f"PUT ", ""), nickname, password)

		if command.startswith(f"SHOW ") and command.replace(f"SHOW ", "") != "":
			print(show(command.replace(f"SHOW ", "")))


		if command == "EXIT":
			exit()
	except TypeError:
		print("404")

db_cursor.close()
