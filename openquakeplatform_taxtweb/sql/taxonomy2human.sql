-- HOWTO use it:
--  . install oq-platform-taxtweb python package system-wide
--  . use CREATE LANGUAGE plpython3u; to be able to run it
--  . load this function once in the database

CREATE OR REPLACE FUNCTION taxonomy2human (taxonomy text) RETURNS text AS 
    $$
        from openquakeplatform_taxtweb.utils.taxonomy2human import taxonomy2human as taxonomy2human_py

        return taxonomy2human_py(taxonomy)
    $$ 
	LANGUAGE plpython3u 
	IMMUTABLE 
	SECURITY INVOKER 
	RETURNS NULL ON NULL INPUT
	PARALLEL SAFE;

COMMENT ON FUNCTION taxonomy2human IS 
	'Returns an English language description of the given string in the GEM Taxonomy v2.0 format.';
