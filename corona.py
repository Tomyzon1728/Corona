# fastrack
# pip install covid library

from covid import Covid 

covid = Covid ( )
cases= covid.get_status_by_country_name("nigeria")
for result in cases:
    print(result,cases[result])