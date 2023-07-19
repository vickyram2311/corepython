from multiprocessing.pool import MapResult

def register(name,location,prefix="mr"):
    if location == "salem":
        print(prefix,name,"has approved in",location)
    elif location == "chennai":
        print(prefix,name,"has gone under waiting state since its",location)
    else: print("business not approved")

register("zealous tech corp","salem")
register("annamalai automobile","chennai","mr.")
register("has been completed","sss")
