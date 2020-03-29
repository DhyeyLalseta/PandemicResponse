from django.db import models


class Result(models.Model):
    """
    Model for hospital input

    Hospitals can input their address, patient capacity, wait time.
    Process for determining drive time will be created in future.
    """
    address = models.CharField(max_length=100)
    patient_capacity = models.PositiveIntegerField()
    wait_time = models.PositiveIntegerField()
    drive_time = models.PositiveIntegerField()

    def __str__(self):
        """
        Returns address of hospital.
        """
        return self.address
