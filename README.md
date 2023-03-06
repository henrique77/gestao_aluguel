# Gestão de Aluguel utilizando Django e MySql

## Dependências

- [Docker Compose](https://docs.docker.com/compose/) version 1,25

Dentro do diretorio do projeto execute:

```

source venv/bin/activate 
```
Em seguida:
```

sudo docker run -p 3306:3306 --name=mysql-gestao -d mysql/mysql-server
```

```

docker-compose build
```

```

docker-compose up
```

```

sudo python3 manage.py runserver
```

Agora só acessar:
```

 http://127.0.0.1:8000/
```
