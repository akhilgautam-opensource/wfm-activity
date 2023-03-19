from django.db import models

# Create your models here.
class WfmActivity(models.Model):
    '''Model for wfm activity table'''
    activityid = models.CharField(db_column='Id', max_length=16, null=False)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    agentlist = models.CharField(db_column='AgentList', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(db_column='Activity', max_length=150, blank=True, null=True)  # Field name made lowercase.
    connid = models.CharField(db_column='ConnID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loop = models.IntegerField(db_column='Loop', blank=True, null=True)  # Field name made lowercase.
    interactionid = models.CharField(db_column='InteractionId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mediatype = models.CharField(db_column='MediaType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cutoff = models.IntegerField(db_column='Cutoff', null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WFM_Activity'
