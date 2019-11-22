from django.db import models

class User(models.Model):
    user_auth=(
        ('1',"EndUser"),
        ('2',"InterUser")
    )
    userName=models.CharField(null=True,max_length=10)
    auth=models.CharField(max_length=1,choices=user_auth)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName


class Bills(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    invoice=models.CharField(max_length=10,null=True)
    vender=models.CharField(max_length=20,null=True)
    buyer=models.CharField(max_length=20,null=True)
    bill_date=models.DateField(auto_now=True)
    bill_items=models.TextField(null=True)
    bill_path=models.FileField(upload_to='billparser/bill collection', null=True)
    digitized=models.BooleanField(default=False)
    
    def __str__(self):
        return self.invoice

# class BillRelation(models.Model):
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#     bill_id=models.ForeignKey(Bills, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user_id
