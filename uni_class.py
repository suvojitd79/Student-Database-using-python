
def main():
     
    class student:

        std = []
   
        def __init__(self,name,id,cgpa):
            self.name = name
            self.id = id
            self.cgpa = cgpa

        def showId(self):
            return self.id

        def result(self):
            if(self.cgpa > 8.5):
                print("Great score")
            elif(self.cgpa > 7 and self.cgpa < 8.5):
                print("Keep it up")
            else:
                print("Not gonna pass")
    
        def details(self):
            print(f'STUDENT ID: {self.id}\nSTUDENT NAME: {self.name}\nCGPA: {self.cgpa}\nPROGRESS REPORT:',end='')+self.result()
            






    def insert():
        if 1:
            x = input('Enter the name of the student: ')
            y = input('Enter the id of the student: ')
            z = input('Enter the cgpa of the student: ')
            while not(z.isdigit() and int(z)<10):
                z = input('Enter a correct cgpa')
            if float(z)<5:
                print(f'Hey {x}, You better work on your studies')
            data = student(x,y,float(z))
            student.std.append(data.__dict__)
            print(f'id no {y} has been added')
            
            
       
           

       
    
    def search():
        found = 0
        try:
            x= input('Enter your id: ')
            for data in student.std:
                if x == data['id']:
                    print('NAME: '+ data['name'])
                    print('CGPA: '+ str(data['cgpa']))
                    found=1

               # print(data['id'])
            if found ==0:
                print('Data not found')
                

        except:

            print('Ooops!Error')


    def decision(x):
        try:
            return{
            '1':insert(),

            '2':search(),

            '3':delete(),
        
            '4': exit()
              
            }[x]

        except:

            print('Invalid input')


    
    while True:
        y = input('Press 1 if you want to insert data\nPress 2 if you want to search data\nPress 3 if you want to delete a data\npress 4 if you want to exit\n')
        if y in ['1','2','3']:
                if y is '1':
                    insert()
                    print(student.std)
                    continue
                elif y is '2':
                    search()
                    continue
                else:
                    search()
                    continue
        else:
                x1=input('INVALID OPTION.PRESS * TO CONTINUE OR ELSE TO EXIT  :')
                if int(ord(x1))==42:
                    continue
                else:
                    break
                

if __name__=='__main__':
    main()














