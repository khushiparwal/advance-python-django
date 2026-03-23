from django.db import connection
class MarksheetService:
    def nextpk(self):
        pk = 0
        with connection.cursor() as cursor:
            q1 = 'select max(rollno) from sos_marksheet'
            cursor.execute(q1)
            result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def add(self,data):
        rollno = MarksheetService.nextpk(self)
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        q1 = "INSERT INTO sos_marksheet (rollno, name, physics, chemistry, maths) VALUES (%s, %s, %s, %s, %s)"
        data = (rollno,name,physics,chemistry,maths)
        cursor = connection.cursor()
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        rollno = data['rollno']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        cursor = connection.cursor()
        q1 = 'update sos_marksheet set name=%s, physics=%s, chemistry=%s, maths=%s where rollno=%s'
        data = (name,physics,chemistry,maths,rollno)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data updated successfully")

    def delete(self,rollno):
        cursor = connection.cursor()
        q1 = 'delete from sos_marksheet where rollno=%s'
        data=(rollno)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data deleted successfully")

    def findbyrollno(self,rollno):
        cursor = connection.cursor()
        q1 = 'select * from sos_marksheet where rollno=%s'
        data = rollno
        cursor.execute(q1, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4])
        connection.commit()
        connection.close()

    def search(self,data):
        rollno = data.get('rollno',0)
        name = data.get('name','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        cursor = connection.cursor()
        q1 = 'select * from sos_marksheet where 1=1'
        if name != '':
            q1 += " and name='"+name+"'"
        if rollno != 0:
            q1 += " and rollno="+str(rollno)
        if pageSize>0:
            offset = (pageNo-1)*pageSize
            q1 += " limit "+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4])
        connection.commit()
        connection.close()




