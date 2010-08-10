# -*- coding: utf-8 -*-

import yaml
f = open( 'biblio.yaml' )
obras = yaml.load( f )

def genera( llave, nombre_archivo ):
  salida = open( nombre_archivo, 'w' )

  #Indicar una llave para ordenar
  obras.sort( key = lambda elemento: elemento[ llave ] )
  print( '<table width="95%" cellspacing="0" cellpadding="5" style="margin:2%; border:thin solid #000000; text-align:center;">', file = salida )
  print( '<tr style="background-color: #aaaaaa"><th>Título</th><th>Autor</th><th>Año</th><th>Editorial</th><th>Reseña</th></tr>', file = salida)  
  
  for obra in obras:
    if( obras.index( obra )%2 == 0 ):
      print( '<tr style="background-color:#eeeeee ;">', file = salida )
    else:
      print( '<tr style="background-color: #ffffff;">', file = salida )  
    print( '<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format( obra[ 'Título' ], obra[ 'Autor' ], obra[ 'Año' ],obra[ 'Editorial' ] ,obra[ 'Reseña' ] ), file = salida )
    print( '</tr>', file = salida )
  print( '</table>', file = salida )

genera( 'Autor', 'autor.html' )
genera( 'Título', 'titulo.html' )
genera( 'Año', 'anio.html' )
