import pickle, os
import random

class Record:
    '''
    Objective : To create an object of type 'Record'
    '''

    def __init__(self):
        '''
        Objective : To initialize an Record object
        Input     : self   : (Implicit) Record object
                    key    : key value of the object Record
                    others : value corresponding to that key
        Output    : None
        '''
        othersSize = 5
        self.key= random.randint(10000,20000)
        self.others= str(self.key)*othersSize
    
    def generatekey(self):
        '''Objective: to generate the key of record
        '''
        return self.key
    
    def __str__(self):
        '''
        Objective : To return a string of the values of the object Record
        Input     : self : (Implicit) Record object 
        OUTPUT    : a string representing the Record object
        '''

        return "\nKey: "+str(self.key) + "\nData: " +self.others


def main():

    '''
    Objective : To write records in file1
    Input     : None 
    Output    : None 
    '''

    f = open("file1.txt",'wb')
    for i in range(1,101):
        ob=Record()
        pickle.dump(ob,f)
    f.close()

    ''' f = open("file1.txt",'rb')
    for i in range(1,101):
        x=pickle.load(f)
        print(i,":",x)
    f.close()'''


    f = open("file1.txt",'rb')
    f1 = open("record1.txt",'wb')
    f2 = open("record2.txt",'wb')
    y=0
    while y!=101:
        try:
            blockSize=4
            lst1=[]
            for i in range(0,blockSize):
                x=pickle.load(f)
                lst1.append(x)
            lst1=sorted(lst1,key=lambda Record:Record.generatekey())
            for i in lst1:
                pickle.dump(i,f1)
        except:
            break
        try:
            lst2=[]
            for i in range(0,blockSize):
                x=pickle.load(f)
                lst2.append(x)
            lst2=sorted(lst2,key=lambda Record:Record.generatekey())
            for i in lst2:
                pickle.dump(i,f2)
        except:
            break
    
    f.close()
    f1.close()
    f2.close()

    f1 = open("record1.txt",'rb')
    try :
        for i in range(0,52):
            x=pickle.load(f1)
            print(i,":",x)
    except:
        pass
    f1.close()


    f2 = open("record2.txt",'rb')
    try:
        for i in range(0,48):
            x=pickle.load(f2)
            print(i,":",x)
    except:
        pass
    f2.close()

    
    choose=int(input("Choose the file:"))

    if choose==1:
        f=open("record1.txt",'rb')
    else:
        f=open("record2.txt",'rb')

    print("enter the range of record in file:")
    start=int(input("Start of range: "))
    end=int(input("End ofrange: "))
    
    pickle.load(f)
    size=f.tell()
    f.seek(0)
    f.seek((start-1)*size)
    for i in range(start,end+1):
        try:
            x=pickle.load(f)
            print(i)
            print(x)
        except:
            break




        
    

    
        
    

if __name__ == "__main__" :
    main()
                  
    

    

