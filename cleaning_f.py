# manupilate columns

def column_edit(DataFrame):
	columns = DataFrame.columns
	DataFrame.columns = DataFrame.columns.str.lower()
	DataFrame.columns = DataFrame.columns.str.replace(" ", "_")
	DataFrame.rename(columns= {'st': 'state'}, inplace=True)
