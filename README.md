# Gestão de Aluguel utilizando Django e MySql

## Dependências

É necessário que tenha instalado o [Docker Compose](https://docs.docker.com/compose/) version 1.25 ou superior.

Primeiro copie o repositório para sua máquina local:

```

git clone https://github.com/henrique77/gestao_aluguel.git
```

Dentro do diretorio do projeto execute:

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
