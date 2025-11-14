FROM rocker/r-base:latest
RUN R -e "install.packages(c('readxl'), repos='http://cran.rstudio.com/')"
WORKDIR /app
COPY patients_hw.R .
RUN mkdir /output
CMD ["Rscript", "/app/patients_hw.R"]
