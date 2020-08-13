import csv
import pymysql

connection = pymysql.connect('localhost','root','','litsql')
connection.autocommit(True)

with connection.cursor() as cursor:
    #sql = "INSERT INTO `customer_save` (`email`, `password`) VALUES (%s, %s)"
    sql = "INSERT INTO `customer_save` "
    with open('customer.csv') as csv_file:
        line_count=0
        csv_reader=csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            if line_count==0:
                temp1='('
                temp2=' VALUES ('
                for i in row:
                    temp1+='`'+i+'`'+', '
                    temp2+='%'+'s, '
                temp1=temp1[:len(temp1)-2]
                temp1+=')'
                temp2=temp2[:len(temp2)-2]
                temp2+=')'
                sql+=temp1+temp2
                line_count+=1
            else:
                print(row)
                print(cursor.execute(sql,row))
        print(line_count)