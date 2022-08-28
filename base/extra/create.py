import pandas as pd
import datetime
from base.models.player import Player
from base.models.team import Team
from base.models.country import Country

# Importing the Csv file and loading it as a DAtaFrame
df = pd.read_csv('base/extra/south-africa-1996.csv')
partial_data = pd.DataFrame(
    df, columns=['No.', 'Pos.', 'Player', 'Date of birth'])

# Function to convert string to datetime
count = 0
for i in partial_data['Date of birth']:
    format = '%d %B %Y'  # The format
    new = datetime.datetime.strptime(i, format).date()
    partial_data.iloc[[count], [3]] = new
    count += 1
    print(new)
print(partial_data)

#Changing the data from a dataframe to a dictionary
dicto = partial_data.to_dict('records')
print(dicto)
count = 0
for i in range(len(dicto)):
    Player.objects.create(name=dicto[count]['Player'], 
                          position=dicto[count]['Pos.'],
                          date_of_birth=dicto[count]['Date of birth'],
                          jersey_number=dicto[count]['No.'],
                          team= Team.objects.get(id=3),
                          country = Country.objects.get(id=6))
    count += 1
    
# COUNTRY
# 1Cote d'Ivoire
# 2Cameroon
# 3Nigeria
# 4Egypt
# 5Zambia
# 6South Africa
# 7Tunisia
# 8Algeria
# 9Senegal

# TEAM
# 1Cote d'Ivoire1992
# 2Nigeria1994
# 3South Africa1996
# 4Egypt1998
# 5Cameroon2000
# 6Cameroon2002
# 7Tunisia2004
# 8Egypt2006
# 9Egypt2008
# 11Egypt2010
# 12Zambia2012
# 13Nigeria2013
# 14Cote d'Ivoire2015
# 15Cameroon2017
# 16Algeria2019
# 17Senegal2021