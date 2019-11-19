project3_docker:
	docker build -t project3_docker .

tax_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" project3_docker && touch $@
	python tax.py $@

patients_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" project3_docker && touch $@
	python patientsdata.py $@

taxplot.png: tax_data_graph.csv
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" project3_docker && touch $@
	Rscript tax_graph.R $@

agedist.png: patients_data_graph.csv
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" project3_docker && touch $@
	Rscript patients_data_graph.R $@
