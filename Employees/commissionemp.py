
class CommissionEmp():
    """This is commission employee class"""
    
    def __init__(self, emp_no=111, name='bingo', gross_sale=10, comm_rate=0.1):
        
        self._emp_no = emp_no
        self._name = name
        self.gross_sale = gross_sale
        self.comm_rate = comm_rate
    
    @property
    def emp_no(self):
        return self._emp_no
    
    @property
    def name(self):
        return self._name
    
    @property
    def gross_sale(self):
        return self._gross_sale
    
    @property
    def comm_rate(self):
        return self._comm_rate
    
    @gross_sale.setter
    def gross_sale(self, gross_sale):
        
        if gross_sale < 0:
            raise ValueError("Base salary has to be positive")
        else:
            self._gross_sale = gross_sale
        
    @comm_rate.setter
    def comm_rate(self, comm_rate):
        
        if not (0 <= comm_rate <= 1):
            raise ValueError("Please enter valid commission rate")
        else:
            self._comm_rate = comm_rate
            
        
        
    def earnings(self):
        """Returns Earnings of Employee"""
        return self.comm_rate * self.gross_sale
 

    def __str__(self):
        return f"Employee name is {self.name}, Employee-ID is {self.emp_no}, Employee earnings is {self.earnings()}"


