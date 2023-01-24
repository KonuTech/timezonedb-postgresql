-- Table: public.country

DROP TABLE IF EXISTS public.country;

CREATE TABLE IF NOT EXISTS public.country
(
    country_code character(2) COLLATE pg_catalog."default",
    country_name character varying(45) COLLATE pg_catalog."default"
);

-- Index: country_code_idx

DROP INDEX IF EXISTS public.country_code_idx;

CREATE INDEX IF NOT EXISTS country_code_idx
    ON public.country USING btree
    (country_code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

-- copy country (country_code, country_name)
--     FROM 'C:\Users\KonuTech\PycharmProjects\timezonedb-postgresql\ingest\country.csv'
--     DELIMITER ','
--     CSV ENCODING
--     'UTF8'
--     QUOTE '\"'
--     ESCAPE ''''
-- ;
