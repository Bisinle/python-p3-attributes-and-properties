#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing",
]


class Person:
    def __init__(self, name="Sonia", job="Admin"):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
        if job in APPROVED_JOBS:
            self._job = job

        else:
            print("Job must be in list of approved jobs.")

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and (1 <= len(value) <= 25):
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job_value):
        if job_value in APPROVED_JOBS:
            self._job = job_value.title()
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)


guido = Person("Hala", "ITC")
print(type(guido))
