CREATE TABLE annual_generation_state (
	year VARCHAR(4) NOT NULL,
	state VARCHAR(2) NOT NULL,
	type_producer VARCHAR(30) NOT NULL,
	energy_source VARCHAR(30) NOT NULL,
	generation INT NOT NULL
	);
Primary key (state), 
	Foreign key (state) references Median_Income (state),
	Foreign key (state) references population_data (state) 
	); 
	
CREATE TABLE Median_Income (
	year VARCHAR(4) NOT NULL,
	state4 VARCHAR(4) NOT NULL,
	state VARCHAR(2) NOT NULL,
	median_income INT NOT NULL
	);
	
Primary key (state, state4), 
	Foreign key (state) references annual_generation_state (state),
	Foreign key (state) references population_data (state), 
	Foreign key (state4) references population_data (state4) 
	);
	
CREATE TABLE population_data (
	year VARCHAR(4) NOT NULL,
	state VARCHAR(2) NOT NULL,
	state4 VARCHAR(4) NOT NULL,
	population INT NOT NULL
	);
	
Primary key (state, state4), 
	Foreign key (state) references annual_generation_state (state),
	Foreign key (state) references Median_Income (state) 
	Foreign key (state4) references Median_Income (state4) 
	);
