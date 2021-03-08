from django.db import models
from user.models import Doctor, Patient, User
from django.core.validators import RegexValidator


class Drug(models.Model):
    """
    Here we define Drug model(table) for database.
    """
    STRENGTH_UNIT_CHOICES = (
        ("M", "mg"),
        ("G","gm"),
        ('N', "ng"),
        ('MC', "mcg")
    )
    PREPARATION_CHOICES = (
        ("T", "Tab."),
        ("C", "Cap."),
        ("I", 'Inj.'),
        ("D", 'Drops')
    )
    ROUTE_CHOICES = (
        ("T", "Topical"),
        ("O", "Oral"),
        ("R", 'Rectal'),
        ("V", 'Vaginal'),
        ("I", 'Inhalation')
    )
    DOSE_UNIT_CHOICES = (
        ("M", "ml"),
        ("U", "unit"),
        ("TS", 'table spoon'),
        ("T", 'tea spoon')
    )
    DIRECTION_CHOICES = (
        ("B", "Before meals"),
        ("A", "After meals")
    )
    FREQUENCY_CHOICES = (
        ("IR", "If required"),
        ("I", "Immediately"),
        ("OD", 'Once a day'),
        ("TWD", 'Twie a day'),
        ("THD", 'Thrice a day')
    )
    DURATION_UNIT_CHOICES = (
        ("D", "Days"),
        ("W", 'Weeks'),
        ("Y", 'Years')
    )
    name = models.CharField(max_length=100)
    strength = models.IntegerField(default=500, verbose_name="strength/power")
    strength_unit = models.CharField(
        default="mg", max_length=3, choices=STRENGTH_UNIT_CHOICES, verbose_name="strength unit"
    )
    preparation = models.CharField(
        default="T", max_length=1, choices=PREPARATION_CHOICES, verbose_name="preparation"
    )
    route = models.CharField(
        default="T", max_length=1, choices=ROUTE_CHOICES, verbose_name="route"
    )
    dose = models.IntegerField(default=50, verbose_name="dose")
    dose_unit = models.CharField(
        default="M", max_length=2, choices=DOSE_UNIT_CHOICES, verbose_name="dose unit"
    )
    direction = models.CharField(
        default="A", max_length=1, choices=DIRECTION_CHOICES, verbose_name="direction"
    )
    frequency = models.CharField(
        default="TWD", max_length=3, choices=FREQUENCY_CHOICES, verbose_name="frequency"
    )
    durations = models.IntegerField(default=1, verbose_name="duration" )
    duration_unit = models.CharField(
        default='W', max_length=1, choices=DURATION_UNIT_CHOICES, verbose_name="duration unit"
    )

    class Meta:
        verbose_name = "drug"
        verbose_name_plural = "drugs"


    def __str__(self):
        return self.name


class Precscription(models.Model):
    """
    Here we define Precscription model(table) for database.
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    drug = models.ManyToManyField(Drug)
    # TODO Over the counter medicine
    otc = models.CharField(max_length=100, verbose_name="over the counter medicine")

    class Meta:
        verbose_name = "precscription"
        verbose_name_plural = "precscriptions"

    def __str__(self):
        return self.patient.user.username


class Pharmacy(models.Model):
    """
    Here we define Pharmacy model(table) for database.
    """
    name = models.CharField(blank=True, max_length=100, verbose_name="pharmacy")
    drug = models.ManyToManyField(Drug)
    address = models.CharField(blank=True, max_length=200, verbose_name="address")
    pc_regex = RegexValidator(
        regex=r"^\d{5}$", message="Please use this format: 'XXXXX'."
    )
    postal_code = models.IntegerField(blank=True, null=True, validators=[pc_regex])
    city = models.CharField(blank=True, max_length=30, verbose_name="city")
    country = models.CharField(blank=True, max_length=30, verbose_name="country")

    class Meta:
        verbose_name = "pharmacy"
        verbose_name_plural = "pharmacies"

    def __str__(self):
        return self.name


class Order(models.Model) :
    """
    Here we define Order model(table) for database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user")
    precscriptions = models.ForeignKey(Precscription, on_delete=models.CASCADE, related_name="order_precscriptions")
    pharmacy = models.ForeignKey(Pharmacy, blank=True, null=True, on_delete=models.SET_NULL, related_name='pharmacy')
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return self.user.username