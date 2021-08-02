def residue_class(a,b,size): #a+bZ = {..cant prescision..}
    """
    This function calculates the class of the remainder
    a+bZ = { }
    
    
    """
    residue_list = []
    a_valpos = a
    a_valneg = a
    residue_list.append(a)
    for i in range(size):
        a_valneg += b
        a_valpos -= b
        residue_list.append(a_valneg)
        residue_list.insert(0, a_valpos)
    print(residue_list)

residue_class(3,18,4) 
