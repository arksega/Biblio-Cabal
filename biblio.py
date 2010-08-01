# -*- coding: utf-8 -*-

import yaml
f=open('biblio.yaml')
obras=yaml.load(f)
f.close()

#Indicar una llave para ordenar
obras.sort( key = lambda elemento: elemento[ 'Autor' ] )

print('<table width="95%" cellspacing="0" cellpadding="5" style="margin:2%; border:thin solid #000000; text-align:center;">')
print('<tr style="background-color: #aaaaaa"><th>Título</th><th>Autor</th><th>Año</th><th>Editorial</th><th>Reseña</th></tr>')

for obra in obras:
  if( obras.index( obra )%2 == 0):
    print('<tr style="background-color:#eeeeee ;">')
  else:
    print('<tr style="background-color:#ffffff ;">')

  print( '<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format( obra[ 'Título' ], obra[ 'Autor' ], obra[ 'Año' ],obra[ 'Editorial' ] ,obra['Reseña']) )
  print('</tr>')
print('</table>') 
