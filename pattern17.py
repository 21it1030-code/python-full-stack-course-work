n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n//2 and j<4) or (j==4 and i<n//2 and i!=0):
            print("*",end='')
        else:
            print(' ',end='')
    print()


'''
*********
*   *    
*   *    
*   *    
****     
*        
*        
*        
*  '''   
