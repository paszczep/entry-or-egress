SELECT
    worker_id as "id",
    name_surname as "name"
FROM
    work.users
WHERE
    id_dec = :card_number
LIMIT 1
;