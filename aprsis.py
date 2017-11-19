#! /usr/bin/env python
#
# Freeradius APRS-IS passcode generator
# Geoffroy GRAMAIZE <geoffroy+dev@gramaize.eu>
#

import radiusd

#
# APRS-IS password generation routine
#

def aprsis_hash(callsign):
    rootCall = callsign.split("-")[0].upper() + '\0'
    
    hash = 0x73e2
    i = 0
    length = len(rootCall)
    
    while (i+1 < length):
        hash ^= ord(rootCall[i])<<8
        hash ^= ord(rootCall[i+1])
        i += 2
    
    return int(hash & 0x7fff)

def log(level, s):
  """Log function."""
  radiusd.radlog(level, '  aprsis.py: ' + s)

#
# Freeradius module routines
# 

def instantiate(p):
    p = p
    return radiusd.RLM_MODULE_OK

def detach():
    return radiusd.RLM_MODULE_OK

def authenticate(p):
    p = p
    return radiusd.RLM_MODULE_OK

def authorize(authData):
    # Extract the data we need.
    userName = None
    
    for t in authData:
        if t[0] == 'User-Name':
            userName = t[1]

    # Don't do anything if user-name not found
    if userName is None:
        return radiusd.RLM_MODULE_NOOP

    log(radiusd.L_DBG, 'Generating Cleartext-Password for User: ' + userName)
    log(radiusd.L_DBG, 'Cleartext-Password: ' + str(aprsis_hash(userName)))

    config = ( ('Cleartext-Password', ':=', str(aprsis_hash(userName)) ), )

    return (radiusd.RLM_MODULE_UPDATED, (), config )

