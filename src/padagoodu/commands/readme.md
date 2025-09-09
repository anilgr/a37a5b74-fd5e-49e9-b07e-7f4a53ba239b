# Padagoodu Database

## Overview
This database stores information about the `padagoodu` game, tracking iterations, letters, and game dates. The schema was recently modified to remove `is_added_to_api` and add `game_date`.

## Table Schema
The `padagoodu` table has the following structure:

| Column         | Type      | Constraints           | Description |
|---------------|----------|----------------------|-------------|
| id           | INTEGER  | PRIMARY KEY          | Unique identifier for each entry |
| iteration    | INTEGER  | NOT NULL             | Iteration number of the game |
| center_letter | TEXT     | NOT NULL             | Central letter for the game |
| letters      | TEXT     | NOT NULL             | Available letters for the game |
| count        | INTEGER  | NOT NULL             | Number of possible words |
| game_date    | DATE     | UNIQUE (nullable)    | Assigned game date |

## Basic SQL Operations

### Insert Data
```sql
INSERT INTO padagoodu (id, iteration, center_letter, letters, count, game_date)
VALUES (1, 1, 'A', 'ABCDE', 10, '2025-03-12');
```

### Select Data
Retrieve all records:
```sql
SELECT * FROM padagoodu;
```
Retrieve records for a specific `game_date`:
```sql
SELECT * FROM padagoodu WHERE game_date = '2025-03-12';
```

### Update Data
Update `game_date` for a specific game:
```sql
UPDATE padagoodu SET game_date = '2025-03-13' WHERE id = 1;
```

### Delete Data
Delete a specific record:
```sql
DELETE FROM padagoodu WHERE id = 1;
```
Delete all records:
```sql
DELETE FROM padagoodu;
```

### Count Entries
Count total rows:
```sql
SELECT COUNT(*) FROM padagoodu;
```

### Find Games Without a Date
```sql
SELECT * FROM padagoodu WHERE game_date IS NULL;
```

### Get Unique Game Dates
```sql
SELECT DISTINCT game_date FROM padagoodu;
```

## Table Migration Steps
The migration steps taken to update the schema:

1. Create a new table `padagoodu_new` without `is_added_to_api` and with `game_date`.
2. Copy existing data into `padagoodu_new`, setting `game_date` to `NULL`.
3. Drop the old `padagoodu` table.
4. Rename `padagoodu_new` to `padagoodu`.

```sql
BEGIN TRANSACTION;

CREATE TABLE padagoodu_new (
    id INTEGER PRIMARY KEY,
    iteration INTEGER NOT NULL,
    center_letter TEXT NOT NULL,
    letters TEXT NOT NULL,
    count INTEGER NOT NULL,
    game_date DATE UNIQUE
);

INSERT INTO padagoodu_new (id, iteration, center_letter, letters, count, game_date)
SELECT id, iteration, center_letter, letters, count, NULL FROM padagoodu;

DROP TABLE padagoodu;
ALTER TABLE padagoodu_new RENAME TO padagoodu;

COMMIT;
```

## License
This project is licensed under the MIT License.

