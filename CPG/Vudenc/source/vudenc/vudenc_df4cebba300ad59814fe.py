async def insert_user_info(self, member_id: int, column: str, col_value):...
execute = f"""INSERT INTO user_info (member_id, {column}) 
                    VALUES ({member_id}, {col_value})
                    ON CONFLICT (member_id)
                        DO UPDATE SET {column} = {col_value};"""
await self.db_conn.execute(execute)
