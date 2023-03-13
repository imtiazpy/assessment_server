from rest_framework.serializers import ModelSerializer

from assessments.models import Assessment
from questions.api.serializers import MCQuestionSerializer, TFQuestionSerializer, SAQuestionSerializer

class PublicAssessmentListSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'description', 'type', 'difficulty', 'category', 'duration', 'slug', )
        read_only_fields = ('id', 'slug', )

  

class PublicAssessmentRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Assessment
        fields = ('id', 'title', 'description', 'type', 'difficulty', 'category', 'duration', 'slug', )
        read_only_fields = ('id', 'slug', )


    def to_representation(self, instance):
        """
        The function takes in an instance of the model, and returns a dictionary of the data that will
        be serialized
        
        :param instance: The object instance that the serializer is being called on
        :return: The data is being returned in the form of a dictionary.
        """
        data = super().to_representation(instance)
        if instance.type == 'MCQ':
            data['questions'] = MCQuestionSerializer(instance.mc_questions.all(), many=True).data
        elif instance.type == 'TRUE_FALSE':
            data['questions'] = TFQuestionSerializer(instance.tf_questions.all(), many=True).data
        elif instance.type == 'SHORT_ANSWER':
            data['questions'] = SAQuestionSerializer(instance.sa_questions.all(), many=True).data
        return data