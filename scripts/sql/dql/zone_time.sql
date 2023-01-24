SELECT
    TO_CHAR(to_timestamp(EXTRACT(EPOCH FROM timezone('UTC', CURRENT_TIMESTAMP)::timestamptz) + gmt_offset), 'yyyy-mm-dd HH24:MI:SS') AS local_time
FROM time_zone
WHERE time_start <= (EXTRACT(EPOCH FROM timezone('UTC', CURRENT_TIMESTAMP)::timestamptz ) ) AND zone_name LIKE %s
LIMIT 1
;