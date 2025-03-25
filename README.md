Set up environment

mkdir proyek_analisis_data

cd proyek_analisis_data

python -m venv env
env\Scripts\activate
pip install pandas numpy matplotlib seaborn streamlit
pip freeze > requirements.txt
type requirements.txt 

Run streamlit 

streamlit run Downloads\dashboard2.py
(sesuaikan dengan tempat file penyimpanan)
