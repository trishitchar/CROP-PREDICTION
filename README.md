virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# step-by-step
0. install python
1. python -m venv venv
2. .\venv\Scripts\activate
3. pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter Pillow
4. jupyter notebook



1. pip show Pillow [inside any venv present or not]


## from requirements.txt
```python
python -m venv venv
```
```python
.\venv\Scripts\activate
```
```python
pip install -r requirements.txt --force-reinstall
```
```python
jupyter notebook
```

