import camelot

tabla = camelot.read_pdf('Cuauhtemo.pdf', pages='12', flavor='stream')

tabla.export('Cuauhtemo.csv', f='csv', compress=True)
tabla[0].to_csv('Cuauhtemo.csv')

