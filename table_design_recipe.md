_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
Nouns:
album, title, release year, artist_id
```

## 2. Infer the Table Name and Columns

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year, artist_id |

Name of the table (plural): `albums`
Column names: `title`, `release_year`, `artist_id`

## 3. Decide the column types

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
id: SERIAL
title: VARCHAR
release_year: INT
artist_id: INT
```

## 4. Write the SQL

```sql

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR,
  release_year INTEGER,
  artist_id INTEGER
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_library_web < music_library.sql
```