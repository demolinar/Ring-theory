from tabulate import tabulate 
import numpy as np

def rtable(zn, operation):
    """
    this function returns the addition or multiplication table
    
    """
    if operation == "*":
        table_zn = np.zeros((zn,zn),dtype=int)
        for i in range(len(table_zn)):
            for j in range(len(table_zn[i])):
                val = (j*i)%zn
                table_zn[i][j] = val
        print("\n","The Z_"+str(zn), " table with the opreration * is:")
        print(tabulate(table_zn))
    elif operation == "+":
        table_zn = np.zeros((zn,zn),dtype=int)
        for i in range(len(table_zn)):
            for j in range(len(table_zn[i])):
                val = (j+i)%zn
                table_zn[i][j] = val
        print("\n","The Z_"+str(zn), " table with the opreration + is:")
        print(tabulate(table_zn))

rtable(6, "*" )

rtable(16, "+" )
