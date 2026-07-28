from flask import request
from api import *
import faf.db as db
SELECT_ACHIEVEMENTS_QUERY = """SELECT
                    ach.id,
                    ach.type,
                    ach.total_steps,
                    ach.revealed_icon_url,
                    ach.unlocked_icon_url,
                    ach.initial_state,
                    ach.experience_points,
                    COALESCE(name_langReg.value, name_lang.value, name_def.value) as name,
                    COALESCE(desc_langReg.value, desc_lang.value, desc_def.value) as description
                FROM achievement_definitions ach
                LEFT OUTER JOIN messages name_langReg
                    ON ach.name_key = name_langReg.key
                        AND name_langReg.language = %(language)s
                        AND name_langReg.region = %(region)s
                LEFT OUTER JOIN messages name_lang
                    ON ach.name_key = name_lang.key
                        AND name_lang.language = %(language)s
                LEFT OUTER JOIN messages name_def
                    ON ach.name_key = name_def.key
                        AND name_def.language = 'en'
                        AND name_def.region = 'US'
                LEFT OUTER JOIN messages desc_langReg
                    ON ach.description_key = desc_langReg.key
                        AND desc_langReg.language = %(language)s
                        AND desc_langReg.region = %(region)s
                LEFT OUTER JOIN messages desc_lang
                    ON ach.description_key = desc_lang.key
                        AND desc_lang.language = %(language)s
                LEFT OUTER JOIN messages desc_def
                    ON ach.description_key = desc_def.key
                        AND desc_def.language = 'en'
                        AND desc_def.region = 'US'"""
@app.route('/achievements')...
"""docstring"""
language = request.args.get('language', 'en')
region = request.args.get('region', 'US')
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(SELECT_ACHIEVEMENTS_QUERY + ' ORDER BY `order` ASC', {
    'language': language, 'region': region})
return flask.jsonify(items=cursor.fetchall())
