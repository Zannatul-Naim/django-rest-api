from django.db import models

choice_sizes = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)

choice_friendliness = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

choice_trainability = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

choice_sheddingamount = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

choice_exerciseneeds = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Breed(models.Modes):
    name = models.CharField(max_length=23)
    size = models.CharField(max_length=7, choices=choice_sizes)
    friendliness = models.IntegerField(choices=choice_friendliness)
    trainability = models.IntegerField(choices=choice_trainability)
    sheddingamount = models.IntegerField(choices=choice_sheddingamount)
    excerciseneeds = models.IntegerField(choices=choice_exerciseneeds)

    def __int__(self):
        return self.name


choice_gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class Dog(models.Model):
    name = models.CharField(max_length=22)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=choice_gender)
    color = models.CharField(max_length=10)
    favouritefood = models.CharField(max_length=10)
    favouritetoy = models.CharField(max_length=10)

    def __str__(self):
        return self.name
