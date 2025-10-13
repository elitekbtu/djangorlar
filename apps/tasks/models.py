# Python modules + Third party modules

# Django modules
from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    UniqueConstraint, 
    PROTECT,
    CASCADE,
)


from django.contrib.auth.models import User

# Project modules
from ..abstract.models import AbstractBaseModel

# Constant variable
NAME_MAX_LEN = 100


class Project(AbstractBaseModel):
    """
    Project database (table) model.
    """

    name = CharField(
        max_length=NAME_MAX_LEN
    )

    author = ForeignKey(
        to=User,
        on_delete=PROTECT,
        related_name = "owner_projects"
    )

    users = ManyToManyField(
        to=User, 
        blank=True,
        related_name="joined_projects"
    )

    def __repr__(self):
        """
        Return the official string represention of the object.
        """
        return f"Project(id={self.id}, name={self.name})"

    def __str__(self):
        """
        Returns string representation of the object.
        """
        return self.name

class Task(AbstractBaseModel):
    """
    Task database (table) model.
    """

    NAME_MAX_LEN = 200
    STATUS_TODO = 1
    STATUS_TODO_LABEL = "To Do"
    STATUS_IN_PROGRESS = 2
    STATUS_IN_PROGRESS_LABEL = "In Progress"
    STATUS_DONE = 3
    STATUS_DONE_LABEL = "Done"

    STATUS_CHOICES = {
        STATUS_TODO: STATUS_TODO_LABEL,
        STATUS_IN_PROGRESS: STATUS_IN_PROGRESS_LABEL,
        STATUS_DONE: STATUS_DONE_LABEL,
    }

    name = CharField(
        max_length=NAME_MAX_LEN,
        db_index=True,
    )
    description = TextField(
        blank=True,
        default="",
    )
    status = IntegerField(
        default=STATUS_TODO,
        choices=STATUS_CHOICES,
    )
    parent = ForeignKey(
        to="self",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    project = ForeignKey(
        to=Project,
        on_delete=CASCADE,
    )
    assignees = ManyToManyField(
        to=User,
        through="UserTask",
        through_fields=("task", "user"),
        blank=True,
    )


class UserTask(AbstractBaseModel):
    """
    UserTask database (table) model.
    """

    task = ForeignKey(
        to=Task,
        on_delete=CASCADE,
    )
    user = ForeignKey(
        to=User,
        on_delete=CASCADE,
    )

    class Meta:
        """Customization of the model's meta data."""

        constraints = [
            UniqueConstraint(
                fields=["task", "user"],
                name="unique_task_user",
            ),
        ]