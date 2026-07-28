def get_history():...
query = """
    SELECT
        upload_log.id as upload_id,
        upload_log.jurisdiction_slug,
        upload_log.event_type_slug,
        upload_log.user_id,
        upload_log.given_filename,
        upload_log.upload_timestamp,
        upload_log.num_rows,
        upload_log.file_size,
        upload_log.file_hash,
        upload_log.s3_upload_path,
        match_log.id as match_id,
        match_log.match_start_timestamp,
        match_log.match_complete_timestamp,
        to_char(match_log.runtime, 'HH24:MI:SS') as runtime
    FROM match_log
    LEFT JOIN upload_log ON upload_log.id = match_log.upload_id
    ORDER BY match_complete_timestamp ASC
    """
df = pd.read_sql(query, con=db.engine)
return df
