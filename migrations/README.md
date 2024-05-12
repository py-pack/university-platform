# Install alembic

```shell
poetry add alembic
```

# Init alembic

```shell
alembic init migrations
```

# Create migratin

```shell
alembic revision --autogenerate -m "create table users"
```

# Push migrate

```shell
alembic upgrade heads
```


