# Movie Database

A Python Tkinter desktop app for storing movie records in a local MySQL database.

## Requirements

- Python 3 with Tkinter
- MySQL or MariaDB
- PyMySQL (`python3 -m pip install PyMySQL`)
- An existing database named `mydata` with a `movies` table containing `movie_id`, `movie_name`, `streaming_company`, `date_watched`, and `rating` columns, in that order

The database schema is not included in this repository. The app reads the `movies` table when it starts, so create it before running the app.

## Run

Set credentials for a MySQL user with access to the database. Use a dedicated user rather than the MySQL root account.

```sh
export DB_USER='your-mysql-user'
export DB_PASSWORD='your-mysql-password'
python3 main.py
```

The app connects to `localhost` and the `mydata` database by default. Set `DB_HOST` or `DB_NAME` to override either value.

## Security note

An earlier commit contained a database password. Change that password on your MySQL server before using the app. Removing it from the current source does not remove it from Git history.
