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

def getRank(filename:str,name:str,gender:str) -> str:
    gender = int(gender)
    with open(filename) as file:
        lines = file.read().split('\n')
        for line in lines:
            line = line.split('\t')
            try:
                if name == line[1 if gender == 1 else 3]:
                    return line[0]
            except:
                return None

def main():
    name = input('Enter the baby name you wish to research:  ').title()
    print('''          
Which gender list do you wish to research?
1.  Male
2.  Female'''
    )
    gender = input('Enter selection:  ')
    while gender not in ['1','2']: gender = input('ERROR:  must enter a 1 or a 2\nPlease re-enter:  ')
    
    files = os.listdir()
    files = [file if '19' in file else None for file in os.listdir()]
    while None in files: files.remove(None)
    files.sort()
    
    print(f'''
For name:  {name}
Decade  Rank
======  ==========''')
    
    for file in files:
        rank,yr = getRank(file,name,gender),re.findall('([0-9]{4})',file)[0]
        if rank == None:
            print(f"{yr}\tNot ranked")
        else:
            print(f"{yr}\t{rank}")
        

if __name__ == '__main__':
    main()