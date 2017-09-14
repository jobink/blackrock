import sys
import json
import csv
from string import Template


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("\nUsage: python csvtojson.py <csv_in_file_path> <json_out_file_path> <json_template_file_path>\n")
    else:
        #Reading arguments
        csv_file_path = sys.argv[1]
        json_file_path = sys.argv[2]
        json_templ_path = sys.argv[3]
		
	#open the file
	templ_file = open( json_templ_path )
	#read it
	src = Template( templ_file.read() )

	with open(csv_file_path) as f_input, open(json_file_path, 'w') as f_output:
		reader = csv.reader(f_input)
		header = next(reader)  # store the headers and advance reader pointer
		#csv_output = csv.writer(f_output)
		f_output.write("{")
		for rows in reader:
			title = rows[0]
			subtitle = rows[1]
			list = [rows[3], rows[4], rows[5]]
			d={ 'title':title, 'subtitle':subtitle, 'list':'\n'.join(list) }
			#do the substitution
			result = src.substitute(d)
			print(result)
			f_output.write(result)
			f_output.write(",")
		
		f_output.write("}")
		
	print ("Just completed writing json file" )
