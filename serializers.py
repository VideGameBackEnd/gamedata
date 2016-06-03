# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Project - democracia de un tavo homosexual
Area - IT; B-E Develpment
Date - Tuesday, June 3, 2016
"""

# Imports
from rest_framework import serializers
# models
from .models import Score

class ScoreSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class serializer
    """
    class Meta :
        model = Score 
        fields = (
            'nombre',
            'partido',
            'score',
        )
    # End of meta class 
# End of score serializer class 