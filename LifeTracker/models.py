from django.db import models

# Create your models here.
class LifeSection(models.Model):
    '''
    A life Section is a very broad area of life in which MetaGoals, Goals, etc. are understood within a certain context
    (e.g. work life, personal life)
    '''


class MetaGoal(models.Model):
    '''
    A MetaGoal is a large goal that encompasses many todos and/or other goals (e.g. Getting into medical school).
    It's a Goal of Goals.
    '''


    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()


class Goal(models.Model):
    '''
    A Goal is an objective that encompasses a collection of smaller tasks and can be associated with other goals in a
    MetaGoal.
    '''

    def __str__(self):
        return self.name

    metaGoal = models.ForeignKey(MetaGoal, on_delete= models.CASCADE, blank= True, null= True)

    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()


class Task(models.Model):
    '''
    A task is an individual todo item that can exist alone (i.e. pay rent) or support a goal (i.e. send an email for the
    Goal of getting into medical school)
    '''

    def __str__(self):
        return self.name

    goal = models.ForeignKey(Goal, on_delete= models.CASCADE, blank= True, null= True)

    name = models.CharField(max_length=255, unique= True)
    description = models.TextField()


class Checklist_Item(models.Model):
    '''
    An item in the checklist for a Task.
    '''

    def __str__(self):
        return self.name

    task = models.ForeignKey(Task, on_delete= models.CASCADE, blank= True, null= True)

    name = models.CharField(max_length=255, unique= True)
    progress = models.BooleanField(choices=((1, 'Not Started'), (2, 'In Progress'), (3, 'Done')),
                                   default=1)




