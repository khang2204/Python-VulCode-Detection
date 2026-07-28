def get_reference_feedback(self):...
sql = (
    'CREATE OR REPLACE VIEW feedback_reference_result AS SELECT article_hash, is_relevant, feedback_label, COUNT(*) AS count FROM feedback_reference GROUP BY article_hash, is_relevant, feedback_label'
    )
self.cur.execute(sql)
self.conn.commit()
sql = (
    'CREATE OR REPLACE VIEW feedback_reference_max AS (SELECT article_hash, is_relevant, feedback_label, count FROM feedback_reference_result WHERE count = (SELECT MAX(count) FROM feedback_reference_result i WHERE i.article_hash = feedback_reference_result.article_hash))'
    )
self.cur.execute(sql)
self.conn.commit()
sql = (
    'SELECT log_query.id, log_query.query_text, log_query.query_search, article_reference.article_content, feedback_reference_max.is_relevant, feedback_reference_max.feedback_label FROM feedback_reference_max LEFT JOIN article_reference ON article_reference.article_hash = feedback_reference_max.article_hash LEFT JOIN log_query ON log_query.id = article_reference.id_query'
    )
self.cur.execute(sql)
self.conn.commit()
feedbacks = {}
for row in self.cur.fetchall():
feedback = {}
return feedbacks
feedback['query_text'] = row['query_text']
feedback['query_search'] = row['query_search']
feedback['article_content'] = row['article_content']
feedback['is_relevant'] = row['is_relevant']
feedback['feedback_label'] = row['feedback_label']
if not row['id'] in feedbacks:
feedbacks[row['id']] = []
feedbacks[row['id']].append(feedback)
