from rest_framework import serializers

class CustomSerSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
