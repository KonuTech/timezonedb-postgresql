-- Table: public.time_zone

CREATE TABLE IF NOT EXISTS public.time_zone
(
    zone_name character varying(35) COLLATE pg_catalog."default" NOT NULL,
    country_code character(2) COLLATE pg_catalog."default" NOT NULL,
    abbreviation character varying(6) COLLATE pg_catalog."default" NOT NULL,
    time_start bigint NOT NULL,
    gmt_offset integer NOT NULL,
    dst character(1) COLLATE pg_catalog."default" NOT NULL
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.time_zone
    OWNER to zfrlhhka;

-- Index: time_start_idx

DROP INDEX IF EXISTS public.time_start_idx;

CREATE INDEX IF NOT EXISTS time_start_idx
    ON public.time_zone USING btree
    (time_start ASC NULLS LAST)
    TABLESPACE pg_default;

-- Index: zone_name_idx

DROP INDEX IF EXISTS public.zone_name_idx;

CREATE INDEX IF NOT EXISTS zone_name_idx
    ON public.time_zone USING btree
    (zone_name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;



-- copy country (country_code, country_name)
--     FROM 'C:\Users\KonuTech\PycharmProjects\timezonedb-postgresql\ingest\time_zone.csv'
--     DELIMITER ','
--     CSV ENCODING
--     'UTF8'
--     QUOTE '\"'
--     ESCAPE ''''
-- ;
