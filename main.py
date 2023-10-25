'''Write a loop that prints each country's population in country_pop.

Sample output with input:
'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800':
China has 1365830000 people.
India has 1247220000 people.
United States has 318463000 people.
Indonesia has 252164800 people.
'''

user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

for country in country_pop:
    pop = country_pop[country]
    print(f'{country} has {pop} people.')