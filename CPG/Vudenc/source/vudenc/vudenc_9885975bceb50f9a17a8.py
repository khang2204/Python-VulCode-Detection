import pymysql
from db_connect import *
from query_functions import *
def print_menu():...
print('\nQuery options:')
print('1:  List ETCs in the country __ having more than __ open beds.')
print(
    '2:  List average age & education of respondents whose sex=__ and live in __.'
    )
print(
    '3:  Count the respondents whose sex=__ and who have at least an education of __.'
    )
print(
    '4:  Display partner organizations with their longitude/latitude coordinates.'
    )
print(
    '5:  Display a chosen organization __ & codes of the ETCs it is working with.'
    )
print('6:  Display all distinct organization types.')
print(
    "7:  Display every respondent's (whose sex=__) info & their country's info."
    )
print(
    "8:  Display every ETC that isn't closed & its info/partner organization.")
print('9:  List countries in ascending order by GDP.')
print(
    '10: Count the respondents (with sex=__, education>=__, and country=__) who think their community was well organized.'
    )
print(
    '11: Show gender, age, education, and country of survey respondents ordered by age.'
    )
print('12: Show ETC names and Partner Orgs ordered by ETC names.')
print(
    '13: Show ETC name, Selected Partner Org, and Country GDP ordered by Country.'
    )
print('14: Show average age of selected gender of survey respondents.')
print(
    '15: Show average educaiton level of selected gender of survey respondents.\n'
    )
def run_another():...
opt = raw_input('Run another query? (y/n): ')
if opt == 'y' or opt == 'Y':
print_menu()
print('Goodbye.')
run_query_case()
def run_query_case():...
case = int(input('Enter query option number: '))
if case == 1:
etc_open_beds()
if case == 2:
run_another()
age_edu_sex_country()
if case == 3:
def main():...
run_another()
count_sex_educ()
if case == 4:
print('========= QUERY INTERFACE FOR EBOLA DATABSE =========\n')
run_another()
partner_lat_long()
if case == 5:
print('...Creating views')
run_another()
org_ETC_codes()
if case == 6:
create_view_SurveyResp_Country()
run_another()
distinct_org_types()
if case == 7:
create_view_etc_limited()
run_another()
respondent_country_info()
if case == 8:
print_menu()
run_another()
non_closed_ETC_partner()
if case == 9:
run_query_case()
run_another()
country_gdp()
if case == 10:
print("""
============== END PROGRAM ==============""")
run_another()
count_organized()
if case == 11:
main()
run_another()
surveyresp_country_byAge()
if case == 12:
run_another()
etc_limited_byName()
if case == 13:
run_another()
partner_org_limited_byCountry()
if case == 14:
run_another()
avg_age_resp()
if case == 15:
run_another()
avg_edu_resp()
print('Sorry, that is not an option.')
run_another()
run_another()
