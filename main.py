from flask import Flask, jsonify, request

app = Flask(__name__)

filterList = ["family", "genus"]

data = {
	"location A": [ {
		"scientific_name": "Physeter macrocephalus",
		"family": "Physeteridae",
		"genus": "Physeter",
	}, {
		"scientific_name": "Thunnus thynnus",
		"family": "Scombridae",
		"genus": "Thunnus"
	}], 
	"location B" : [{
		"scientific_name": "Thunnus maccoyii",
		"family": "Scombridae",
		"genus": "Thunnus",
	}]
}

@app.route("/")
def search():	
	filter = { f: request.args.get(f)
		for f in filterList
	}
	location = request.args.get("location")


	response = []

	if data.get(location):
		speciesList = data[location]
		for species in speciesList:
			flag = True
			for f in filterList:
				if filter[f] and species[f] != filter[f]:
					flag = False
					break
			if flag:
				response.append(species)
					

	print(response)
	response = jsonify(response)

	response.headers.add("Access-Control-Allow-Origin", "*")
	return response



if __name__ == '__main__':
	app.run()