# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Project - democracia de un tavo homosexual
Area - IT; B-E Develpment
Date - Tuesday, June 3, 2016
"""

from __future__ import unicode_literals

from django.db import models

"""
Score model
This will save the users scores with the party they chose
"""
class Score( models.Model ) :
    
    score = models.IntegerField(default=0, blank=False)
    nombre = models.CharField(max_length=200, default = '', blank=False)
    partido = models.CharField(max_length=200, default = '', blank=False)
    
    def __unicode__( self ) :
        """
        To string function
        """
        return ( "Nombre {0}; Score :{1}; Partido {2}" ).format( self.nombre, self.score, self.partido )
    # End of unicode function
    
# End of Score model class