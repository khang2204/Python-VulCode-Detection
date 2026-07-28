def main():...
print('========= QUERY INTERFACE FOR EBOLA DATABSE =========\n')
print('...Creating views')
create_view_SurveyResp_Country()
create_view_etc_limited()
print_menu()
run_query_case()
print("""
============== END PROGRAM ==============""")
