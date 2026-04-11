BEGIN TRANSACTION;

-- Step 1: Create a new table without `is_added_to_api` and with `game_date`
CREATE TABLE padagoodu_new (
    id INTEGER PRIMARY KEY,
    iteration INTEGER NOT NULL,
    center_letter TEXT NOT NULL,
    letters TEXT NOT NULL,
    count INTEGER NOT NULL,
    game_date DATE UNIQUE  -- Allows NULL for unassigned games
);

-- Step 2: Copy data from the old table, setting game_date to NULL
INSERT INTO padagoodu_new (id, iteration, center_letter, letters, count, game_date)
SELECT id, iteration, center_letter, letters, count, NULL FROM padagoodu;

-- Step 3: Drop the old table
DROP TABLE padagoodu;

-- Step 4: Rename the new table to `padagoodu`
ALTER TABLE padagoodu_new RENAME TO padagoodu;

COMMIT;
