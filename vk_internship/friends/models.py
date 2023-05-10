from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'


class Friends(models.Model):
    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='user'
        )
    friend = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='friend'
        )

    def __str__(self) -> str:
        return self.friend.username

    class Meta:
        db_table = 'friends'
        verbose_name_plural = 'Friends'


class Invites(models.Model):
    from_user = models.OneToOneField(
        'Users',
        on_delete=models.CASCADE,
        related_name='from_user'
        )
    to_user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
        related_name='to_user'
    )

    def __str__(self) -> str:
        return f'{self.from_user} -> {self.to_user}'

    class Meta:
        db_table = 'invites'
        verbose_name_plural = 'Invites'
