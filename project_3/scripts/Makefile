mydocker:
	docker build -t mydocker .

tax_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" mydocker && touch $@
	python tax.py $@

patients_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" mydocker && touch $@
	python patientsdata.py $@

../results/Project3.html: patients_data_graph.csv tax_data_graph.csv
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" mydocker && touch $@
	Rscript -e "library(rmarkdown); rmarkdown::render('Project3.Rmd', 'html_document')"  && mv Project3.html ../results



	

	
