from urllib.parse import urlparse
import psycopg2 as ps
result = urlparse("postgres://postgres:9ccfcf17f22e605d9a212c9fc24b8da5@dokku-postgres-postgre:5432/postgre")
result = urlparse("postgres://postgres:9ccfcf17f22e605d9a212c9fc24b8da5@dokku-postgres-pride-postgre:5432/pride_postgre")
result = urlparse("postgres://postgres:9ccfcf17f22e605d9a212c9fc24b8da5@dokku-postgres-postgre:5432/postgre")
result = urlparse("postgres://postgres:fe30d08eaad059a15ba971ea1668d523@dokku-postgres-pride-postgre:5432/pride_postgre")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port

print(username)
print(password)
print(database)
print(hostname)
print(port)

base = ps.connect(
    port=4557, host='185.251.88.183', user=username, password=password, database=database
)

cursor = base.cursor()
if base:
    print("Data base connected")

    
cursor.execute("SELECT * FROM ref")
user = cursor.fetchall()    

print(user)


base.close()


('PoroshinaNatalia', '{}', 0), ('GrasmikAlena', '{}', 0), ('SoloveychykDmityi', '{}', 0), ('SalamatinaOlesa', '{}', 0), ('SalamatinSergey', '{}', 0), ('VlasovaSvetlana', '{}', 0), ('MixailovaVera', '{}', 
0), ('LebedevaDaria', '{}', 0), ('KrivkoDiana', '{}', 0), ('SinevaMaria', '{}', 0), ('GevorkanIlona', '{}', 0), ('MaksimenkoSergey', '{}', 0), ('Dmitriystroi', '{}', 0), ('SavelevNikita', '{}', 0), ('KuksovaViktoria', '{}', 0), ('GevorkanIlia', '{}', 0), ('GerasimovaNatalia', '{}', 0), ('TestovaAnna', '{}', 0), ('Krivko Aleksandr', '{}', 0) 