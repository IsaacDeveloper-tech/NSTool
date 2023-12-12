from classes.LogSystem import LogTypes, Log

print(LogTypes.INFO)

log = Log()

log.writeLog("Hola", LogTypes.DEBUG)
log.writeLog("Hola", LogTypes.WARNING)
log.writeLog("Hola", LogTypes.INFO)
log.writeLog("Hola", LogTypes.ERROR)