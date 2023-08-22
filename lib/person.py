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
        self._name = ""
        self._job = ""
        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) == str and (1 <= len(value) <= 25):
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job_value):
        if job_value in APPROVED_JOBS:
            self._job = job_value
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)


guido = Person("Hala", "ITC")
print(type(guido))
