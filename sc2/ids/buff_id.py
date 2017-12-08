# DO NOT EDIT!
# This file was automatically generated by "generate_id_constants.py"

import enum

class BuffId(enum.Enum):
    INVALID = 0
    GRAVITONBEAM = 5
    GHOSTCLOAK = 6
    BANSHEECLOAK = 7
    POWERUSERWARPABLE = 8
    QUEENSPAWNLARVATIMER = 11
    GHOSTHOLDFIRE = 12
    GHOSTHOLDFIREB = 13
    EMPDECLOAK = 16
    FUNGALGROWTH = 17
    GUARDIANSHIELD = 18
    TIMEWARPPRODUCTION = 20
    NEURALPARASITE = 22
    STIMPACKMARAUDER = 24
    SUPPLYDROP = 25
    STIMPACK = 27
    PSISTORM = 28
    CLOAKFIELDEFFECT = 29
    CHARGING = 30
    SLOW = 33
    CONTAMINATED = 36
    BLINDINGCLOUDSTRUCTURE = 38
    ORACLEREVELATION = 49
    VIPERCONSUMESTRUCTURE = 59
    BLINDINGCLOUD = 83
    MEDIVACSPEEDBOOST = 89
    PURIFY = 97
    ORACLEWEAPON = 99
    IMMORTALOVERLOAD = 102
    LOCKON = 116
    SEEKERMISSILE = 120
    TEMPORALFIELD = 121
    VOIDRAYSWARMDAMAGEBOOST = 122
    ORACLESTASISTRAPTARGET = 129
    PARASITICBOMB = 132
    PARASITICBOMBUNITKU = 133
    PARASITICBOMBSECONDARYUNITSEARCH = 134
    LURKERHOLDFIREB = 137
    CHANNELSNIPECOMBAT = 145
    TEMPESTDISRUPTIONBLASTSTUNBEHAVIOR = 146
    CARRYMINERALFIELDMINERALS = 271
    CARRYHIGHYIELDMINERALFIELDMINERALS = 272
    CARRYHARVESTABLEVESPENEGEYSERGAS = 273
    CARRYHARVESTABLEVESPENEGEYSERGASPROTOSS = 274
    CARRYHARVESTABLEVESPENEGEYSERGASZERG = 275

for item in BuffId:
    globals()[item.name] = item
