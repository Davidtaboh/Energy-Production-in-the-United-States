Now to plot:
data=pd.read_csv("Energy_merged.csv")

year_group = data.groupby('year')

simple_energy = year_group.sum(year_group['conventional_energy])

simple_energy.plot.scatter(x='year',y='total')
simple_energy.plot.scatter(x='year',y='conventional')
simple_energy.plot.scatter(x='year',y='green')
simple_energy.plot.scatter(x=['year','year','year'],y=['total','conventional','green'])
simple_energy=data.assign(Percentage=1.0*  data['green']/data['total'])