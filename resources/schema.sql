--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

-- Started on 2023-05-31 22:11:28 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE academia;
--
-- TOC entry 4356 (class 1262 OID 16618)
-- Name: academia; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE academia WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


ALTER DATABASE academia OWNER TO postgres;

\connect academia

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16620)
-- Name: lotacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lotacao (
    id integer NOT NULL,
    num_pessoas smallint NOT NULL,
    data timestamp without time zone NOT NULL,
    temperatura smallint NOT NULL,
    umidade_relativa smallint NOT NULL,
    precipitacao smallint NOT NULL,
    indice_uv smallint NOT NULL
);


ALTER TABLE public.lotacao OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16619)
-- Name: lotacao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lotacao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lotacao_id_seq OWNER TO postgres;

--
-- TOC entry 4357 (class 0 OID 0)
-- Dependencies: 214
-- Name: lotacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lotacao_id_seq OWNED BY public.lotacao.id;


--
-- TOC entry 4206 (class 2604 OID 16623)
-- Name: lotacao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lotacao ALTER COLUMN id SET DEFAULT nextval('public.lotacao_id_seq'::regclass);


--
-- TOC entry 4208 (class 2606 OID 16625)
-- Name: lotacao lotacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lotacao
    ADD CONSTRAINT lotacao_pkey PRIMARY KEY (id);


-- Completed on 2023-05-31 22:11:28 -03

--
-- PostgreSQL database dump complete
--

