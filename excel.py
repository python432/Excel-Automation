import pandas as pd
from tkinter import messagebox

info = messagebox.showinfo('Information', 'THIS TOOL IS MADE BY PYTHON432',)
input_file = 'transactions.xlsx'
df = pd.read_excel(input_file)
credit_df = df[df['Type'] == 'credit']
debit_df = df[df['Type'] == 'debit']
credit_file = 'credits.xlsx'
credit_df.to_excel(credit_file, index=False)
debit_file = 'debits.xlsx'
debit_df.to_excel(debit_file, index=False)
print("Credits and debits have been saved in separate Excel files!")
