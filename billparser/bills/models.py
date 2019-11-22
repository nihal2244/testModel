from django.db import models

class User(models.Model):
    user_auth=(
        ('1',"EndUser"),
        ('2',"InterUser")
    )
    user_name=models.CharField(null=True,max_length=10)
    auth=models.CharField(max_length=1,choices=user_auth)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Bills(models.Model):
    invoice=models.CharField(max_length=10,null=True)
    vender=models.CharField(max_length=10,null=True)
    buyer=models.CharField(max_length=10,null=True)
    bill_date=models.DateField(auto_now=True)
    bill_items=models.TextField(null=True)
    bill_path=models.FileField(upload_to=user_directory_path)
    digitized=models.BooleanField(default=False)
    
    def __str__(self):
        return self.invoice

class BillRelation(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    bill_id=models.ForeignKey(Bills, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id
