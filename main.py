#untuk membuat table
from tabulate import tabulate

#square root, untuk menghitung euclidean distance
from math import sqrt



class Membership:
    database_user = {
        'Sumbul': 'Platinum', 
        'Ana': 'Gold', 
        'Cahya': 'Platinum'
    }
    
    table_membership = {
        'Platinum' : ['Platinum', 15, 'Voucher Makanan + Voucher Ojek Online + Voucher Liburan + Cashback maksimal 30%'],
        'Gold' : ['Gold', 10, 'Voucher Makanan + Voucher Ojek Online'],
        'Silver' : ['Silver', 8, 'Voucher Makanan + Voucher Ojek Online']
    }
    table_req = {
        'Platinum' : ['Platinum', 8, 15],
        'Gold' :['Gold', 6, 10],
        'Silver' : ['Silver', 5, 7]
    }
    def __init__ (self, username):
        self.username = username
        
        
    def check_all_membership(self):
        table = [value for key, value in self.table_membership.items()]
        header = ['Membership', 'Diskon (%)', 'Benefit']
        print(tabulate(table, header))
        
        
    def check_requirement (self):
        table = [value for key, value in self.table_req.items()]
        header = ['Membership', 'Monthly Expense', 'Monthly Income']
        print(tabulate(table, header))
    
    
    def predict_membership (self, username, monthly_expense, monthly_income):
        distance = {}
        
        for key, value in self.table_req.items():
            temp = sqrt((monthly_expense - self.table_req[key][1])**2 \
                    + (monthly_income-self.table_req[key][2])**2)
            distance[key] = temp
        
        print(f'Hasil perhitungan Euclidean Distance dari user {username} adalah {distance}')
        
        for key, value in distance.items():
            if value == min(distance.values()):
                self.database_user[username] = key
                return key
          
        
    def check_membership (self, username):
        if username in self.database_user.keys():
            return self.database_user[username]
        
        
    def final_price (self, username, list_harga):
        total = sum(list_harga)
        
        try:
            if username in self.database_user.keys():
                membership_type = self.database_user[username]
                
                if membership_type != '':
                    discount = self.table_membership[membership_type][1] / 100
                
                    return (1-discount) * total
                
                else:
                    raise Exception(f'Lakukan prediksi membership pada user {username}')
            
            
            else:
                raise Exception ('User tidak ditemukan')
        
        except Exception as e:
            print (e)

nizar = Membership('nizar')
nizar.check_all_membership()
nizar.check_requirement()
print(nizar.predict_membership('nizar', 9, 12))
print(nizar.final_price('nizar', [200_000, 300_000, 500_000]))            