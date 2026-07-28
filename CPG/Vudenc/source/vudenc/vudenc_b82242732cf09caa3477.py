def validate_answer(ans):...
too_long = len(ans) > max_ans_len
logging.info('validate_answer: %s returns %r', str(ans), not too_long)
return not too_long
