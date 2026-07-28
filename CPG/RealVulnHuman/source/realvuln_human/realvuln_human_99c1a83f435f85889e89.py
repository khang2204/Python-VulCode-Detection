formatted = dict()
        for i in range(num_cols):
            formatted[cols[i]] = [item[i] for item in raw]
        return formatted
    except:
        return dict()

@classmethod
def hits_by_ip(cls, ip, col='*'):
    table_name = cls.objects.model._meta.db_table
    cmd = "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC" % (
        col, table_name, ip)
    with connection.cursor() as cursor:
        cursor.execute(cmd)
        raw = cursor.fetchall()
    formatted = Analytics.format_raw_sql(cmd, raw, col)
    return formatted

# defined in railsgoat but not used, expects valid column name
@classmethod
def count_by_col(cls, col):
    return cls.objects.values(col).count()

# expects field type to be string
