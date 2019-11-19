#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-
from bottle import *
from datetime import datetime
import requests
#home control menu
js=[('coffee','コーヒー'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('TV', 'TV'), ('cup', 'CH+'), ('cdwn', 'CH-'), ('vup', 'Vol+'), ('vdwn', 'Vol-'), ('vcut', '消音'), ('bs', 'bs'), ('cs', 'cs'), ('bs1', 'bs1'), ('bs2', 'bs2'), ('bs3', 'bs3'), ('bs4', 'bs4'), ('bs5', 'bs5'), ('bs6', 'bs6'), ('bs7', 'bs7'), ('bs8', 'bs8'), ('bs9', 'bs9'), ('bs10', 'bs10'), ('bs11', 'bs11'), ('bs12', 'bs12'), ('inUp', 'inUp'), ('inDwn', 'inDwn'), ('ent', 'ent'), ('on', '全灯'), ('off', '消灯'), ('fav', 'お好'), ('small', '保安灯'), ('lup', '明'), ('ldwn', '暗'), ('ac', '冷房'), ('acoff', '停止'), ('heeting', '暖房'), ('Joshitsu', '除湿'), ('ron', 'ラジオ'), ('r1', 'R1'), ('r2', 'R2'), ('r3', 'R3'), ('r4', 'R4'), ('r5', 'R5'), ('r6', 'R6'), ('r7', 'R7'), ('r8', 'R8'), ('r9', 'R9'), ('r0', 'R0'), ('R+', '+'), ('R-', '-'), ('r>', '>')]

@route('/')
@view('index')
def home():
    return dict(
        year=datetime.now().year,app="/app"
    )

@route('/home')
@view('home')
def home1():
    return dict(
        year=datetime.now().year,js=js,app="/app"
    )
@route('/contact')
@view('contact')
def contact():
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year,app="/app"
    )
@route('/about')
@view('about')
def about():
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year,app="/app"
    )
#MQ to beebottle
def mq(idx):
    url='https://api.beebotte.com/v1/data/write/HomeControl/cmd?token=xxxxxxxxxxxxxxxxxxxxx'
    r=requests.post(url,{'data':idx})
@route('/click/<idx>')
def click(idx):
    #mq(idx)
    return idx
