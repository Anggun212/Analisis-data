<b>Setup Environment</b>

mkdir proyek_analisis_data

cd proyek_analisis_data

python -m venv env

env\Scripts\activate

pip freeze > requirements.txt

pip install pandas numpy matplotlib seaborn streamlit

type requirements.txt 


 <b>Run streamlit</b>

 cd proyek_analisis_data
 
 streamlit run dashboard2.py
