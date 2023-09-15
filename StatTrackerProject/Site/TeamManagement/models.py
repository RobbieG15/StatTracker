from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, firstName = "", lastName = "", password = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            firstName = firstName,
            lastName = lastName,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None):

        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email = email, password = password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True
    )

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    has_organization = models.BooleanField(default = False)

    firstName = models.CharField(
        verbose_name = 'First Name',
        max_length = 255,
        null = True,
        blank = True,
    )

    lastName = models.CharField(
        verbose_name = 'Last Name',
        max_length = 255,
        null = True,
        blank = True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstName + ' ' + self.lastName

    def get_first_name(self):
        return self.firstName

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = UserManager()

class Organization(models.Model):

    org_type_choices = [
        'Football',
    ]

    state_choices = [
        'Ohio',
    ]

    @classmethod
    def create(cls, school_name, org_type, city, state, owner):
        org = cls(
            school_name = school_name,
            org_type = org_type,
            city = city,
            state = state,
            owner = owner,
        )

        return org

    school_name = models.CharField(
        verbose_name = 'School Name',
        max_length = 255,
    )

    org_type = models.CharField(
        max_length = 255,
    )

    city = models.CharField(
        verbose_name = 'City',
        max_length = 255,
    )

    state = models.CharField(
        verbose_name = 'State',
        max_length = 255,
    )

    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

class Team(models.Model):

    @classmethod
    def create(cls, team_name, org):
        team = cls(
            team_name = team_name,
            org = org,
        )

        return team

    team_name = models.CharField(
        verbose_name = 'School Name',
        max_length = 255,
    )

    org = models.ForeignKey(
        Organization, 
        on_delete = models.CASCADE,
    )

class Player(models.Model):

    @classmethod
    def create(cls, first_name, last_name, number, team):
        player = cls(
            first_name = first_name,
            last_name = last_name,
            number = number,
            team = team
        )

        return player

    first_name = models.CharField(
        verbose_name = 'First Name',
        max_length = 255,
    )

    last_name = models.CharField(
        verbose_name = 'Last Name',
        max_length = 255,
    )

    number = models.IntegerField(
        primary_key = True,
        unique = True,
    )

    team = models.ForeignKey(Team, on_delete = models.CASCADE)

class Game(models.Model):

    @classmethod
    def create(cls, org, homeTeam, awayTeam, dateTime):
        game = cls(
            org = org,
            homeTeam = homeTeam,
            awayTeam = awayTeam,
            dateTime = dateTime
        )

        return game

    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='homeTeam')
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='awayTeam')
    dateTime = models.DateTimeField()



class FootballStat(models.Model):

    @classmethod
    def create(cls, game, player):
        footballStat = cls(
            game = game,
            player = player
        )

        return footballStat


    # Passing (attempts, completions, yards, touchdowns)
    attemptsPassing = models.IntegerField(default=0)
    completionsPassing = models.IntegerField(default=0)
    yardsPassing = models.IntegerField(default=0)
    touchdownsPassing = models.IntegerField(default=0)

    # Recieving
    targets = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)
    yardsRecieving = models.IntegerField(default=0)
    touchdownsRecieving = models.IntegerField(default=0)

    # Rushing (carries, yards, touchdowns)
    carries = models.IntegerField(default=0)
    yardsRushing = models.IntegerField(default=0)
    touchdownsRushing = models.IntegerField(default=0)

    # Defense (tackles, TFLs, Sacks, forced fumbles, fumble recoveries, interceptions, touchdowns)
    tackles = models.IntegerField(default=0)
    TFLs = models.IntegerField(default=0)
    sacks = models.IntegerField(default=0)
    forcedFumbles = models.IntegerField(default=0)
    fumbleRecoveries = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    touchdownsDefense = models.IntegerField(default=0)

    # Game
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    # Player
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
