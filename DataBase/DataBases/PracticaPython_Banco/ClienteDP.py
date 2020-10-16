
class ClienteDP:

    # Constructores
    def __init__(this):
        this.nocta  = ""
        this.nombre = ""
        this.tipo   = ""
        this.saldo  = 0

    def __init__(this, datos):
        if(datos == ""):
            this.nocta  = ""
            this.nombre = ""
            this.tipo   = ""
            this.saldo  = 0
        else:
            st = datos.split("_")
            
            this.nocta  = st[0]
            this.nombre = st[1]
            this.tipo   = st[2]
            this.saldo  = int(st[3])

    # Accesors (geters)
    def getNocta(this):
        return this.nocta

    def geNombre(this):
        return this.nombre

    def getTipo(this):
        return this.tipo

    def getSaldo(this):
        return this.saldo

    # Mutators (seters)
    def setNocta(this,ncta):
        this.nocta = ncta

    def setNombre(this,name):
        this.nombre = name

    def setTipo(this,tcta):
        this.tipo = tcta

    def setSaldo(this,cantidad):
        this.saldo = cantidad

    # Metodos
    def toString(this):
        return this.nocta+"_"+this.nombre+"_"+this.tipo+"_"+str(this.saldo)

    def toStringSql(this):
        return "'"+this.nocta+"','"+this.nombre+"','"+this.tipo+"','"+str(this.saldo)+"'"
