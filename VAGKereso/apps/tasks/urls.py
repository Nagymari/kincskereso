from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Első feladat - A költő
    path('kolto/', views.kolto, name='kolto'),

    # Második feladat - Formalitás
    path('formalitas/', views.kolto, name='formalitas'),

    # Harmadik feladat - Reliving
    path('reliving/', views.kolto, name='reliving'),


    # Első ág - Keresés
    path('kereses/', views.kolto, name='kereses'),

    # Első feladat - Solar
    path('kereses/solar/', views.kolto, name='solar'),

    # Második feladat - A kód
    path('kereses/kod/', views.kolto, name='kod'),

    # Harmadik feladat - Ősmagyarok dicsősége
    path('kereses/osmagyarok-dicsosege/', views.kolto, name='osmagyarok-dicsosege'),

    # Negyedik feladat - Iker
    path('kereses/iker/', views.kolto, name='iker'),


    # Második ág - Logika
    path('logika/', views.kolto, name='logika'),

    # Első feladat - A jászma
    path('logika/jatszma/', views.kolto, name='jatszma'),

    # Második feladat - Iker 2
    path('logika/iker-2/', views.kolto, name='iker-2'),

    # Harmadik feladat - Nézőpont
    path('logika/nezopont/', views.kolto, name='nezopont'),

    # Negyedik feladat - Szótenger
    path('logika/szotenger/', views.kolto, name='szotenger'),


    # Harmadik ág - Művészet
    path('muveszet/', views.kolto, name='muveszet'),

    # Első feladat - A piac
    path('muveszet/piac/', views.kolto, name='piac'),

    # Második feladat - A festmény
    path('muveszet/festmeny/', views.kolto, name='festmeny'),

    # Harmadik feladat - A darab
    path('muveszet/darab/', views.kolto, name='darab'),

    # Negyedik feladat - A ritmus
    path('muveszet/ritmus/', views.kolto, name='ritmus'),


    # Negyedik ág - Irodalom
    path('irodalom/', views.kolto, name='irodalom'),

    # Első feladat - A mű
    path('irodalom/mu/', views.kolto, name='mu'),

    # Második feladat - A zseni
    path('irodalom/zseni/', views.kolto, name='zseni'),

    # Harmadik feladat - Egy kutya
    path('irodalom/egy-kutya/', views.kolto, name='egy-kutya'),

    # Negyedik feladat - A tragédiák diktátora
    path('irodalom/tragediak-diktatora/', views.kolto, name='tragediak-diktatora'),


    # Utolsó előtti feladat - Az utolsó játszma
    path('utolso-jatszma/', views.kolto, name='utolso-jatszma'),

    # Utolsó feladat - A tekercs
    path('tekercs/', views.kolto, name='tekercs')
]
