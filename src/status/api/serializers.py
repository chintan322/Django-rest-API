from rest_framework import serializers

from status.models import Status

'''
Serializers -> JSON
Serializers -> Validate Data
'''

# class CustomeSerializers(serializers.Serializer):
#     content     = serializers.CharField()
#     email       = serializers.EmailField()

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    # def validate_content(self, value):
    #     if len(value) > 1000:
    #         raise serializers.ValidationError("this is way too long/")
    #     return value

    def validate(self,data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data