from django.db import models

# Create your models here.
class MyToDoList(models.Model):
    '''データベーステーブル作成のmodelクラス定義'''
    #通し番号
    id = models.AutoField(primary_key=True)
    #見出しCharFiledは必ずmax_length設定を
    title = models.CharField(max_length=200)
    #todolist内容
    contents = models.TextField()
    #記入日auto_now_add=Trueはそのタイミングを記録。通常default=False
    entryDate = models.DateField(auto_now_add=True)
    #締め切り
    deadline = models.DateField()
    #Django Adminで確認するとき、見出しとして表示されるデータのこと
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        # db_table = "マイリスト"
        verbose_name = "WZZ's Todolist"
        verbose_name_plural = verbose_name