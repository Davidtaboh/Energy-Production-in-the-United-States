import numpy as np
import pandas as pd

from flask import Flask, jsonify, render_template, request
from sqlalchemy import func


import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import or_


app = Flask(__name__)

#Noaman
# rds_connection_string = "postgres://NoamanJameel:Noamanj1919@localhost/Energy_db"
# engine = create_engine(rds_connection_string)

# Luke
# path_string = "postgres:postgres@localhost:5432/energy"
# engine = create_engine(f'postgresql+psycopg2://{path_string}')

#Erica
# path_string = "ericamatrese:Harrisburg1@localhost:5432/energy"
# engine = create_engine(f"postgresql://{path_string}")

#Jonathan
rds_connection_string = "postgres://postgres:postgres@localhost:5432/test_db"
engine = create_engine(rds_connection_string)
 

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# energyData = Base.classes.energy_data

session = Session(engine)

# @app.route('/')
# def welcome():

#     return (
#          f"Welcome Energy Production API <br/>"
#         f"Available Routes:<br/>"
#         f"/api/v1.0/Landing<br/>"
#         f"/api/v1.0/Comparison<br/>"
#         f"/api/v1.0/Data<br/>"
#         f"/api/v1.0/Visualization1<br/>"
#         f"/api/v1.0/Visualization2<br/>"
#         f"/api/v1.0/Visualization3<br/>"
#         f"/api/v1.0/Visualization4<br/>"

#     )

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/comparisons')
def comparisons():

    return render_template('comparisons.html')

@app.route('/data')
def data():

    return render_template('data.html')    

@app.route('/visualization1')
def visualization1():

    return render_template('visualization1.html')

@app.route('/visualization2')
def visualization2():

    return render_template('visualization2.html')

@app.route('/visualization3')
def visualization3():

    return render_template('visualization3.html')

@app.route('/visualization4')
def visualization4():

    return render_template('visualization4.html')

@app.route('/visualization5')
def visualization5():

    return render_template('visualization5.html')


    # Green & Conventional Energy Total 1990-2018 By State // Bargraph
#     green_energy = session.query(energyData.state_id, energyData.energy_type, func.sum(energyData.generation_megawatthours)).\
#         filter(energyData.energy_type == 'Green Energy').group_by(energyData.state_id, energyData.energy_type).order_by(energyData.state_id).all()

#     green_energy_total = []
    
#     for state_id, energy_type, generation_megawatthours in green_energy:
#         energy_dict ={}
#         energy_dict["State"] = state_id
#         energy_dict['Energy Type'] = energy_type
#         energy_dict['Energy Prodcued'] = generation_megawatthours
        
#         green_energy_total.append(energy_dict)
        
#     conv_energy = session.query(energyData.state_id, energyData.energy_type, func.sum(energyData.generation_megawatthours)).\
#         filter(energyData.energy_type == 'Conventional').group_by(energyData.state_id, energyData.energy_type).order_by(energyData.state_id).all()

#     conv_energy_total = []
    
#     for state_id, energy_type, generation_megawatthours in conv_energy:
#         energy_dict ={}
#         energy_dict["State"] = state_id
#         energy_dict['Energy Type'] = energy_type
#         energy_dict['Energy Prodcued'] = generation_megawatthours

#         conv_energy_total.append(energy_dict)
    
    
#     # Green Vs Conventional Energy of Per Year For Country // Linegraph

#     green_country_year = session.query(energyData.year_energy, func.sum(energyData.generation_megawatthours), energyData.energy_type).\
#         filter(energyData.energy_type == 'Green Energy').group_by(energyData.year_energy,energyData.energy_type).\
#             order_by(energyData.year_energy)
    
#     green_total_country = []
#     for year_energy, energy_type, generation_megawatthours in green_country_year:
#         energy_dict = {}
#         energy_dict["Year"] = year_energy
#         energy_dict["Energy Type"] = energy_type
#         energy_dict['Energy Produced'] = generation_megawatthours
        
#         green_total_country.append(energy_dict)

    
#     conv_country_year = session.query(energyData.year_energy, func.sum(energyData.generation_megawatthours), energyData.energy_type).\
#         filter(energyData.energy_type == 'Conventional').group_by(energyData.year_energy,energyData.energy_type).\
#             order_by(energyData.year_energy)
    
#     conv_country_total = []
#     for year_energy, energy_type, generation_megawatthours in conv_country_year:
#         energy_dict = {}
#         energy_dict["Year"] = year_energy
#         energy_dict["Energy Type"] = energy_type
#         energy_dict['Energy Produced'] = generation_megawatthours

#         conv_country_total.append(energy_dict)

#     # MAP - Total Energy Production By State From 1990 2018/ This is For Leaflet Map

#     map_energy = session.query(energyData.state_id, func.sum(energyData.generation_megawatthours)).\
#         group_by(energyData.state_id).order_by(energyData.state_id)
        
#     map_state = []

#     for state_id, generation_megawatthours in map_energy:
#         energy_dict = {}
#         energy_dict["State"] = state_id
#         energy_dict["Energy Produced"] = generation_megawatthours

#         map_state.append(energy_dict)

    
#     return jsonify({'Bargraph':{'Green Energy':green_energy_total,'Conventional Energy':conv_energy_total}, 
#     'Linegraph':{'Country Green Energy':green_total_country,'Country Conventional Energy': conv_country_total}, 
#     'Map':{'Total Energy By State':map_state}})
    

if __name__ == '__main__':
    app.run(debug=True)
