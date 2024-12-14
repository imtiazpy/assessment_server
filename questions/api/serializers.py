from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from assessments.models import Assessment
from questions.models import MCQuestion, Choice, TFQuestion, Answer, SAQuestion

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ('id', )

class MCQuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = MCQuestion
        fields = ('id', 'content', 'assessment', 'choices')
        read_only_fields = ('id', )

    def validate_assessment(self, value):
        """
        When creating mcq
        If the assessment is not created by the user, raise a validation error
        :param value: The value that is being validated
        :return: The value of the assessment
        """
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create MCQ for this assessment")
        return value
    

class TFQuestionSerializer(ModelSerializer):
    class Meta:
        model = TFQuestion
        fields = '__all__'
        read_only_fields = ('id', )
    
    def validate_assessment(self, value):
        """
        When creating True False question
        If the assessment is not created by the user, raise a validation error
        :param value: The value that is being validated
        :return: The value of the assessment
        """
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create MCQ for this assessment")
        return value


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('id', )

class SAQuestionSerializer(ModelSerializer):
    answer = AnswerSerializer()
    
    class Meta:
        model = SAQuestion
        fields = ('id', 'content', 'assessment', 'answer', )
        read_only_fields = ('id', )
    

    def validate_assessment(self, value):
        """
        When creating Short answer question
        If the assessment is not created by the user, raise a validation error
        :param value: The value that is being validated
        :return: The value of the assessment
        """
        assessment = Assessment.objects.get(id=value.id)
        user = self.context['request'].user

        if assessment.created_by != user:
            raise serializers.ValidationError("You do not have permission to create MCQ for this assessment")
        return value
