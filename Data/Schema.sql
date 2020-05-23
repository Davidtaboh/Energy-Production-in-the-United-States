DROP TABLE energy_data

CREATE TABLE energy_data (
	id SERIAL PRIMARY KEY,
	year_energy INT NOT NULL,
	state_id VARCHAR(25) NOT NULL,
	type_of_producer VARCHAR(255) NOT NULL,
	energy_source VARCHAR(255) NOT NULL,
	generation_megawatthours INT NOT NULL,
	energy_type VARCHAR(255) NOT NULL
)


CREATE TABLE income_data (
	id SERIAL PRIMARY KEY,
	year_income INT NOT NULL,
	state_id VARCHAR(25) NOT NULL,
	median_income INT NOT NULL
)

CREATE TABLE population_data (
	id SERIAL PRIMARY KEY,
	year_population INT NOT NULL,
	state_id VARCHAR(25) NOT NULL,
	population INT NOT NULL
)

select * from energy_data
select * from income_data
select * from population_data