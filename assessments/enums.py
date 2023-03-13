from django.db import models


class AssessmentCategories(models.TextChoices):
    """Categories for Assessment"""

    PROGRAMMING = 'PROGRAMMING', 'Programming'
    PERSONALITY = 'PERSONALITY', 'Personality'
    COGNITIVE = 'COGNITIVE', 'Cognitive'
    LANGUAGE = 'LANGUAGE', 'Language'


class AssessmentTypes(models.TextChoices):
    """Types choices for Assessment"""

    MCQ = "MCQ", "MCQ"
    SHORT_ANSWER = "SHORT_ANSWER", "Short Answer"
    TRUE_FALSE = "TRUE_FALSE", "True False"


class AssessmentDifficulties(models.TextChoices):
    """Difficulty levels for Assessment"""
    
    ENTRY_LEVEL = 'ENTRY_LEVEL', 'Entry Level'
    INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
    EXPERT = 'EXPERT', 'Expert'