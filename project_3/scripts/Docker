tax_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" jupyter/datascience-notebook && touch $@
	python tax.py $@

patients_data_graph.csv:
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" jupyter/datascience-notebook && touch $@
	python patientsdata.py $@

taxplot.png: tax_data_graph.csv
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" jupyter/datascience-notebook && touch $@
	Rscript tax_graph.R $@

agedist.png: patients_data_graph.csv
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" jupyter/datascience-notebook && touch $@
	Rscript patients_data_graph.R $@

../results/Project3.html: taxplot.png agedist.png
	docker run -d --rm -v "$(pwd):$(pwd)" -w "$(pwd)" jupyter/datascience-notebook && touch $@
	Rscript -e "library(rmarkdown); rmarkdown::render('Project3.Rmd', 'html_document')"  && mv Project3.html ../results

runall: ../results/Project3.html tax_data_graph.csv patients_data_graph.csv taxplot.png agedist.png Rplots.pdf 
	rm tax_data_graph.csv patients_data_graph.csv taxplot.png agedist.png Rplots.pdf 


	

	
