'''EX output:
Enter the baby name you wish to research:  marion

Which gender list do you wish to research?
1.  Male
2.  Female
Enter selection:  3
ERROR:  must enter a 1 or a 2
Please re-enter:  1

For name:  Marion
Decade  Rank
======  ==========
1900    130
1910    118
1920    113
1930    138
1940    198
1950    269
1960    392
1970    501
1980    798
1990    Not ranked
'''

import os,re

def main():
    name = input('Enter the baby name you wish to research:  ').title()
    print('''          
Which gender list do you wish to research?
1.  Male
2.  Female'''
    )
    gender = input('Enter Selection:  ')
    while gender not in ['1','2']: gender = input('ERROR:  must enter a 1 or a 2\nPlease re-enter:  ')
    
    files = os.listdir()
    files = [file if '19' in file else None for file in files]
    while None in files: files.remove(None)
    maleYears,femaleYears = {},{}
    files.sort()
    for file in files:
        with open(file) as file:
            lines = file.read().split('\n')
            yr = re.findall('([0-9]{4})',lines[0])[0]
            maleYears[yr],femaleYears[yr] = {},{}
            for line in lines:
                line = line.split('\t')
                try: rank,maleName,maleNum,femaleName,femaleNum = line[0],line[1],line[2],line[3],line[4]
                except IndexError: continue
                maleYears[yr][maleName] = {
                    'rank': rank,
                    'number':maleNum
                }
                femaleYears[yr][femaleName] = {
                    'rank': rank,
                    'number': femaleNum
                }
    
    print(f'''
For name:  {name}
Decade  Rank
======  ==========''')
    
    for year,names in (maleYears if gender == '1' else femaleYears).items():
        try: rank = names[name]['rank']
        except KeyError: print(f"{year}\tNot ranked");continue
        print(f"{year}\t{rank}")
    



if __name__ == '__main__':
    main()