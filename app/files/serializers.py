from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    class Meta:
        model = File
        fields = "__all__"
        extra_fields = ["processed"]

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(FileSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields