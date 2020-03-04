"""User model"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from djongo import models
from djongo.sql2mongo import SQLDecodeError
from pymongo.errors import BulkWriteError
from django.contrib.auth.models import User


def create_user(username, password, email):
    """
    Creates user instance and tries to add it into database.
    Returns:
        user instance if added successfully,
        None otherwise.
    """

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user
    except SQLDecodeError:
        return None


def get_by_username(username):
    """
    Returns:
        user instance if found,
        None otherwise.
    """
    try:
        return User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None


def change_password(username, new_password):
    """
    Method to change user password.
    Returns:
        user instance if password was changed,
        None otherwise.
    """
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None
    user.set_password(new_password)
    try:
        user.save()
        return user
    except SQLDecodeError:
        return None
