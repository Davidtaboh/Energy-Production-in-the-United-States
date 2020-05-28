import pandas as pd














def energy_label(row):
    if row['ENERGY SOURCE']=='Natural Gas':
        return 'Conventional'
    elif row['ENERGY SOURCE']=='Petroleum':
        return 'Conventional'
    elif row['ENERGY SOURCE']=='Coal':
        return 'Conventional'
    elif  row['ENERGY SOURCE']=='Other Biomass':
        return 'Conventional'
    elif  row['ENERGY SOURCE']=='Hydroelectric Conventional':
        return 'Green Energy'
    elif row['ENERGY SOURCE']=='Wood and Wood Derived Fuels':
        return 'Conventional'
    elif row['ENERGY SOURCE']=='Other':
        return 'N/A'
    elif row['ENERGY SOURCE']=='Wind':
        return 'Green Energy'
    elif row['ENERGY SOURCE']=='Nuclear':
        return 'Green Energy'
    elif row['ENERGY SOURCE']=='Solar Thermal and Photovoltaic':
        return 'Green Energy'
    elif row['ENERGY SOURCE']=='Pumped Storage':
        return 'Green Energy'
    elif row['ENERGY SOURCE']=='Geothermal':
        return 'Green Energy'
    elif row['ENERGY SOURCE'] == 'Other Gases':
        return 'Conventional'
    else:
        return 'N/A'


"""
    This function will remove the unneccesary columns from the data as well as condense it to be most usefull
    the end result will be a total of 29*3 rows
    each row represents a single year and a single energy source, and shows its total output
    for example:

        1990, Clean Energy, 500000 MwH
        1990, Dirty Energy, 100000MwH
        1990, Unknown, 25000MwH
        1991, Clean Energy, 600000Mwh
        ....
        ...

"""
def Stage0Clean():
    data = pd.read_csv("Energy_data.csv", header='infer',converters={})



"""
    This function will remove the unneccesary columns from the data as well as condense it to be most usefull
    the end result will be a total of 29*3 rows
    each row represents a single year and a single energy source, and shows its total output
    for example:
    
        1990, Clean Energy, 500000 MwH
        1990, Dirty Energy, 100000MwH
        1990, Unknown, 25000MwH
        1991, Clean Energy, 600000Mwh
        ....
        ...

"""
def Stage1Clean():
    Keep_columns=['year_energy','generation_megawatthours','energy_type']
    data=pd.read_csv("Energy_data.csv",header='infer')
    keep=data[Keep_columns]
    as_csv=keep.to_csv(index=False).splitlines() #get data as a list of rows
    header=as_csv.pop(0)
    out_dict={}
    for row in as_csv:
        row=row.split(",")  #split each row by a comma value
        if row:
            year=int(row[0])
            mwh=int(row[1])
            style=row[2]
            if year in out_dict:
                if style in out_dict[year]:
                    out_dict[year][style]+=mwh
                elif style not in out_dict[year]:
                    out_dict[year][style] = mwh
            elif year not in out_dict:
                out_dict[year]={style:mwh}

"""
    Now to plot:
    data=pd.read_csv("cleaned_data.csv")
    data.plot.scatter(x='year',y='total')
    data.plot.scatter(x='year',y='conventional')
    data.plot.scatter(x='year',y='green')
    data.plot.scatter(x=['year','year','year'],y=['total','conventional','green'])
    test_data=data.assign(Percentage=1.0*  data['green']/data['total'])
"""

